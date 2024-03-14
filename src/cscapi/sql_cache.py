import json
from dataclasses import asdict
from typing import List, Optional

from dacite import from_dict
from sqlalchemy import (
    Boolean,
    Column,
    Float,
    ForeignKey,
    Integer,
    TEXT,
    String,
    DateTime,
    func,
    create_engine,
    delete,
    update,
    event,
    or_,
)
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column,
    relationship,
    sessionmaker,
    joinedload,
    selectinload,
)

from sqlalchemy.engine import Engine
from sqlite3 import Connection as SQLiteConnection
from cscapi import cache


"""
By default, foreign key constraints are disabled in SQLite.
@see https://docs.sqlalchemy.org/en/20/dialects/sqlite.html#foreign-key-support
"""


@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    if isinstance(dbapi_connection, SQLiteConnection):
        cursor = dbapi_connection.cursor()
        cursor.execute("PRAGMA foreign_keys=ON")
        cursor.close()


class Base(DeclarativeBase):
    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class CacheItemDBModel(Base):
    __tablename__ = "cache_items_models"

    id = Column(Integer, primary_key=True, autoincrement=True)
    key = Column(String(128), unique=True)
    content = Column(TEXT, default=lambda: json.dumps([]))  # Stores JSON-serialized array
    expires_at = Column(DateTime(timezone=True), nullable=True)
    created_at = Column(DateTime(timezone=True), default=func.now())
    updated_at = Column(DateTime(timezone=True), default=func.now(), onupdate=func.now())

    def to_dict(self):
        d = super().to_dict()
        d["content"] = json.loads(self.content) if self.content else []
        return d


class CachedDecisionDBModel(Base):
    __tablename__ = "cached_decisions_models"

    id = Column(Integer, primary_key=True, autoincrement=True)
    identifier = Column(TEXT)
    scope = Column(TEXT)
    value = Column(TEXT)
    type = Column(TEXT)
    origin = Column(TEXT)
    expires_at = Column(DateTime(timezone=True), nullable=True)
    created_at = Column(DateTime, default=func.now())


class SQLCache(cache.CacheInterface):
    def __init__(self, connection_string="sqlite:///cscapi-cache.db") -> None:
        engine = create_engine(connection_string, echo=False)
        Base.metadata.create_all(engine)
        self.session = sessionmaker(bind=engine)

