# mysql_role changelog

All notable changes to this project will be documented in this file.
This project adheres to [Semantic Versioning](http://semver.org/) and [Keep a changelog](https://github.com/olivierlacan/keep-a-changelog).
## Unrealeased

## [4.5.5](https://github.com/idealista/mysql_role/tree/4.5.5)
[Full Changelog](https://github.com/idealista/mysql_role/compare/4.5.4...4.5.5)
### Fixed
- *[#100](https://github.com/idealista/mysql_role/issues/100) update oracle repo gpg key* @ablopez

## [4.5.4](https://github.com/idealista/mysql_role/tree/4.5.4)
[Full Changelog](https://github.com/idealista/mysql_role/compare/4.5.3...4.5.4)
### Removed
- *[#94](https://github.com/idealista/mysql_role/issues/97) Remove variable in "vars" to make the variable in "defauts" work* @xtianae7

## [4.5.3](https://github.com/idealista/mysql_role/tree/4.5.3)
[Full Changelog](https://github.com/idealista/mysql_role/compare/4.5.2...4.5.3)
### Fixed
- *[#94](https://github.com/idealista/mysql_role/issues/94) update cache when installing dependencies* @ablopez


## [4.5.2](https://github.com/idealista/mysql_role/tree/4.5.2)
[Full Changelog](https://github.com/idealista/mysql_role/compare/4.5.1...4.5.2)
### Fixed
- *[#91](https://github.com/idealista/mysql_role/issues/91) defaulted http_agent parameter to null when downloading MySQL config deb* @xtianae7

## [4.5.1](https://github.com/idealista/mysql_role/tree/4.5.1)
[Full Changelog](https://github.com/idealista/mysql_role/compare/4.5.0...4.5.1)
### Fixed
- [#88](https://github.com/idealista/mysql_role/issues/88) *Fix password-less root user creation* @santi-eidu
## [4.5.0](https://github.com/idealista/mysql_role/tree/4.5.0)
[Full Changelog](https://github.com/idealista/mysql_role/compare/4.4.0...4.5.0)
### Added
- [#85](https://github.com/idealista/mysql_role/issues/85) *Replaced hardcoded filenames by variables in config tasks; small improvement in mysql.service template* @frantsao
### Fixed
- [#85](https://github.com/idealista/mysql_role/issues/85) *Fix no_log in user creation* @frantsao

## Unreleased

## [4.4.0](https://github.com/idealista/mysql_role/tree/4.4.0)
[Full Changelog](https://github.com/idealista/mysql_role/compare/4.3.0...4.4.0)
### Added
- [#82](https://github.com/idealista/mysql_role/issues/82) *Provide options to install non-default mysql versions* @blalop

## [4.3.0](https://github.com/idealista/mysql_role/tree/4.3.0)
[Full Changelog](https://github.com/idealista/mysql_role/compare/4.2.0...4.3.0)
### Fixed
- [#79](https://github.com/idealista/mysql_role/issues/79) *Fixed .my.cnf template* @frantsao
### Added
- [#79](https://github.com/idealista/mysql_role/issues/79) *Improved python3 support in tests* @frantsao
- [#79](https://github.com/idealista/mysql_role/issues/79) *Updated tests dependencies* @frantsao

## [4.2.0](https://github.com/idealista/mysql_role/tree/4.2.0)
[Full Changelog](https://github.com/idealista/mysql_role/compare/4.1.1...4.2.0)
### Added
- [#76](https://github.com/idealista/mysql_role/issues/70) *[FEATURE] Add Debian11 support* @vsuarez
- [#77](https://github.com/idealista/mysql_role/pull/77) *[FEATURE] keyserver depends now depends on OS* @vsuarez
### Changed
- Drop stretch support.
- Bumped pipenv/dev dependencies.

## [4.1.1](https://github.com/idealista/mysql_role/tree/4.1.1)
[Full Changelog](https://github.com/idealista/mysql_role/compare/4.1.0...4.1.1)
### Added
- [#70](https://github.com/idealista/mysql_role/issues/70) *[FEATURE] Role reshaping* @marcelogalmor

## [4.1.0](https://github.com/idealista/mysql_role/tree/4.1.0)
[Full Changelog](https://github.com/idealista/mysql_role/compare/4.0.0...4.1.0)
### Added
- [#64](https://github.com/idealista/mysql_role/issues/64) *[FEATURE] parameterize mariadb/mysql version to install* @emepege
- [#59](https://github.com/idealista/mysql_role/issues/59) *Travis and molecule tests should be improved* @emepege
## [4.0.0](https://github.com/idealista/mysql_role/tree/4.0.0) (17/07/2019)
[Full Changelog](https://github.com/idealista/mysql_role/compare/3.0.0...4.0.0)
### Changed
- [#61](https://github.com/idealista/mysql_role/issues/61) *Parametrize more options in services* @pablogcaldito

### Fixed
- [#57](https://github.com/idealista/mysql_role/issues/57) *Fix debian 10 issue ensuring service is started on boot* @pablogcaldito
- [#12](https://github.com/idealista/mysql_role/pull/12-new) *Remount task removed due known problems, explained in readme in case need to be used*
- [#12](https://github.com/idealista/mysql_role/pull/12-new) *Tests to confirm configuration was applied added* @dgalcantara

## [3.0.0](https://github.com/idealista/mysql_role/tree/3.0.0) (17/07/2019)
[Full Changelog](https://github.com/idealista/mysql_role/compare/2.2.1...3.0.0)
### Fixed 
- [#50](https://github.com/idealista/mysql_role/pull/50) *Add MariaDB Debian packages support* @frantsao
### Changed
- [#50](https://github.com/idealista/mysql_role/pull/50) *Fix files and directories permissions* @frantsao

## [2.2.2](https://github.com/idealista/mysql_role/tree/2.2.1) (08/03/2019)
[Full Changelog](https://github.com/idealista/mysql_role/compare/2.2.0...2.2.1)
### Fixed 
- [#45](https://github.com/idealista/mysql_role/pull/45) *Fixed Oracle expired key* @jnogol

### Changed
- *Change "yes" for true due to linter recommendation* @jnogol

## [2.2.1](https://github.com/idealista/mysql_role/tree/2.2.1) (21/01/2019)
[Full Changelog](https://github.com/idealista/mysql_role/compare/2.2.0...2.2.1)
### Fixed 
- [#43](https://github.com/idealista/mysql_role/pull/43) *Fixed users default privileges* @vide

## [2.2.0](https://github.com/idealista/mysql_role/tree/2.2.0) (16/01/2019)
[Full Changelog](https://github.com/idealista/mysql_role/compare/2.1.0...2.2.0)
### Changed
- [#39](https://github.com/idealista/mysql_role/issues/39) *Using '_' instead of '-' in role name* @dortegau

### Added
- [#41](https://github.com/idealista/mysql_role/pull/41) *Manage replicate_ignore_table special case* @vide

## [2.1.0](https://github.com/idealista/mysql_role/tree/2.1.0) (04/04/2018)
[Full Changelog](https://github.com/idealista/mysql_role/compare/2.0.0...2.1.0)
### Added
- [#35](https://github.com/idealista/mysql_role/issues/35) *Provide additional settings as option files included in playbook* @dortegau

### Fixed
- [#34](https://github.com/idealista/mysql_role/issues/34) *Adding default value for mysql_datadir variable* @dortegau

## [2.0.0](https://github.com/idealista/mysql_role/tree/2.0.0) (22/03/2018)
[Full Changelog](https://github.com/idealista/mysql_role/compare/1.3.0...2.0.0)
### Changed
- [#29](https://github.com/idealista/mysql_role/issues/29) *Options file could be modified adding or removing system variables without requiring a new release* @dortegau

## [1.3.0](https://github.com/idealista/mysql_role/tree/1.3.0) (15/03/2018)
[Full Changelog](https://github.com/idealista/mysql_role/compare/1.2.3...1.3.0)
### Added
- [#26](https://github.com/idealista/mysql_role/issues/26) *Adding the ability to configure SQL mode* @dortegau

### Changed
- [#25](https://github.com/idealista/mysql_role/issues/25) *Migrating to Molecule 2.10.1* @dortegau

### Fixed
- [#24](https://github.com/idealista/mysql_role/issues/24) *Fixing my.cnf template (providing value to 'explicit_defaults_for_timestamp')* @dortegau

## [1.2.3](https://github.com/idealista/mysql_role/tree/1.2.3) (09/03/2018)
[Full Changelog](https://github.com/idealista/mysql_role/compare/1.2.0...1.2.3)
### Fixed
- [#21](https://github.com/idealista/mysql_role/issues/21)*Using my.cnf file provided as template instead of installation default file (mysql.cnf)* @dortegau
- *Fixing typo in config filename and changing invalid config values* @dortegau

## [1.2.0](https://github.com/idealista/mysql_role/tree/1.2.0) (10/08/2017)
[Full Changelog](https://github.com/idealista/mysql_role/compare/1.1.0...1.2.0)
### Added
- *Integration with TravisCI and Ansible Galaxy* @jnogol
- *Added variable in remounting task in tasks/service.yml* @jnogol

## [1.1.0](https://github.com/idealista/mysql_role/tree/1.1.0) (06/07/2017)
[Full Changelog](https://github.com/idealista/mysql_role/compare/1.0.0...1.1.0)
### Added
- *Enabling support for Debian 9* @dortegau

## [1.0.0](https://github.com/idealista/mysql_role/tree/1.0.0) (13/03/2017)
### Fixed
- *Certificate error downloading mysql* @jmonterrubio

## [0.0.1]
### Added
- *First release*
