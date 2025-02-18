# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/) and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## SemVer public API

The [public API](https://semver.org/spec/v2.0.0.html#spec-item-1)  for this project is defined by the set of 
functions provided by the `src/cscapi` folder.

--- 

## [0.2.1](https://github.com/crowdsecurity/python-capi-sdk/releases/tag/v0.2.1) - 2024-02-09
[_Compare with previous release_](https://github.com/crowdsecurity/python-capi-sdk/compare/v0.2.0...v0.2.1)


### Fixed

- Decrease `machine_id` database length to 128 characters for Mysql compatibility ([#17](https://github.com/crowdsecurity/python-capi-sdk/pull/17)) and ([#18](https://github.com/crowdsecurity/python-capi-sdk/pull/18))

---

## [0.2.0](https://github.com/crowdsecurity/python-capi-sdk/releases/tag/v0.2.0) - 2024-02-09
[_Compare with previous release_](https://github.com/crowdsecurity/python-capi-sdk/compare/v0.1.0...v0.2.0)


### Changed

- Update `create_signal` function to accept datetime object for the `created_at` argument ([#16](https://github.com/crowdsecurity/python-capi-sdk/pull/16))

---

## [0.1.0](https://github.com/crowdsecurity/python-capi-sdk/releases/tag/v0.1.0) - 2024-02-08
[_Compare with previous release_](https://github.com/crowdsecurity/python-capi-sdk/compare/v0.0.2...v0.1.0)

### Changed

- **Breaking change**: Change method name `CAPIClient::has_valid_scenarios` to `CAPIClient::_has_valid_scenarios`

### Added

- Add `CAPIClient::prune_failing_machines_signals` method for deleting signals from failing machines ([#14](https://github.com/crowdsecurity/python-capi-sdk/pull/14))


---

## [0.0.2](https://github.com/crowdsecurity/python-capi-sdk/releases/tag/v0.0.2) - 2024-02-07
[_Compare with previous release_](https://github.com/crowdsecurity/python-capi-sdk/compare/v0.0.1...v0.0.2)


### Fixed

- Enable foreign key constraints only in SQLite connections ([#13](https://github.com/crowdsecurity/python-capi-sdk/pull/13))

---

## [0.0.1](https://github.com/crowdsecurity/python-capi-sdk/releases/tag/v0.0.1) - 2024-02-06

- Initial release
