# Changelog

## [1.0.3] (2022-10-23)
### Added
- Support white light on motion switch through imouapi
- `linkagewhitelight` now among the switches enabled by default
- Support for SelectEntity and `nightVisionMode` select
- Support storage used through `storageUsed` sensor
- Support for push notifications through `pushNotifications` switch
- Options for configuring push notifications
### Changed
- Bump imouapi version: 1.0.2 → 1.0.4
- Redact device id and entry id from diagnostics

## [1.0.2] (2022-10-19)
### Changed
- Bump imouapi version: 1.0.1 → 1.0.2

## [1.0.1] (2022-10-16)
### Added
- Download diagnostics capability

## [1.0.0] (2022-10-15)
### Changed
- Bump imouapi version: 0.2.2 → 1.0.0
- Entity ID names are now based on the name of the sensor and not on the description

## [0.1.4] (2022-10-08)
### Added
- Test suite
### Changed
- Bump imouapi version: 0.2.1 → 0.2.2

## [0.1.3] (2022-10-04)
### Changed
- Bump imouapi version: 0.2.0 → 0.2.1

## [0.1.2] (2022-10-03)
### Added
- All the switches are now made available. Only a subset are then enabled in HA by default.
- Sensors' icons and default icon
### Changed
- Bump imouapi version: 0.1.5 → 0.2.0 and adapted the code accordingly
- Introduced `ImouEntity` class for all the sensors derived subclasses

## [0.1.1] (2022-09-29)
### Changed
- Bump imouapi version: 0.1.4 → 0.1.5
- Improved README

## [0.1.0] (2022-09-29)
### Added
- First release for beta testing
