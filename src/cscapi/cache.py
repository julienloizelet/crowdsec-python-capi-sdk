from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List, Any, Optional


@dataclass
class CacheItem:
    """
    A cache item.

    Attributes:
        key (str): The unique key associated with the cache item.
        content (List[Any]): The content of the cache item.
        expires_at (int): The UNIX timestamp at which the cache item expires.
    """
    key: str
    content: List[Any]
    expires_at: int

    def __post_init__(self):
        if not isinstance(self.key, str):
            raise TypeError("key must be a string")
        if not isinstance(self.content, list):
            raise TypeError("content must be a list")
        if not isinstance(self.expires_at, int):
            raise TypeError("expires_at must be an int")


@dataclass
class CachedDecision:
    """
    A cached decision.

    Attributes:
        identifier (str): The unique identifier of the decision.
        scope (str): The scope of the decision such as "ip", "range", "country", and more.
        value (str): The value of the decision such as an IP, a range of IPs, a country, and more.
        type (str): The type of the decision such as "ban", "captcha", "bypass", and more.
        origin (str): The origin of the decision such as "capi", "lapi", and more.
        expires_at (int): The UNIX timestamp at which the decision expires.
    """
    identifier: str
    scope: str
    value: str
    type: str
    origin: str
    expires_at: int

    def __post_init__(self):
        if not isinstance(self.identifier, str):
            raise TypeError("identifier must be a string")
        if not isinstance(self.scope, str):
            raise TypeError("scope must be a string")
        if not isinstance(self.value, str):
            raise TypeError("value must be a string")
        if not isinstance(self.type, str):
            raise TypeError("type must be a string")
        if not isinstance(self.origin, str):
            raise TypeError("origin must be a string")
        if not isinstance(self.expires_at, int):
            raise TypeError("expires_at must be an int (timestamp)")


class CacheInterface(ABC):
    @abstractmethod
    def get_item(self, key: str) -> Optional[CacheItem]:
        """
        Retrieve an item from the cache.

        Args:
            key (str): The key of the item to retrieve.

        Returns:
            Optional[CacheItem]: The cache item if it exists, None in case of a cache miss.
        """
        raise NotImplementedError

    @abstractmethod
    def save(self, item: CacheItem) -> bool:
        """
        Save an item in the cache.

        Args:
            item (CacheItem): The item to save.

        Returns:
            bool: True if the item was saved, False otherwise.
        """
        raise NotImplementedError

    @abstractmethod
    def delete_items(self, keys: List[str]) -> bool:
        """
        Delete items from the cache.

        Args:
            keys (List[str]): The keys of the items to delete.

        Returns:
            bool: True if the items were deleted, False otherwise.
        """
        raise NotImplementedError

    @abstractmethod
    def clear(self) -> bool:
        """
        Delete all items from the cache.

        Returns:
            bool: True if the cache was cleared, False otherwise.
        """
        raise NotImplementedError
