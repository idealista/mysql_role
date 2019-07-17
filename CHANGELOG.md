# mysql_role changelog

All notable changes to this project will be documented in this file.
This project adheres to [Semantic Versioning](http://semver.org/) and [Keep a changelog](https://github.com/olivierlacan/keep-a-changelog).

## [Unreleased](https://github.com/idealista/mysql_role/tree/develop)
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
