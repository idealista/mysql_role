![Logo](https://raw.githubusercontent.com/idealista/mysql_role/master/logo.gif)

# MySQL Ansible role

[![Build Status](https://travis-ci.org/idealista/mysql_role.png)](https://travis-ci.org/idealista/mysql_role)
[![Ansible Galaxy](https://img.shields.io/badge/galaxy-idealista.mysql__role-B62682.svg)](https://galaxy.ansible.com/idealista/mysql_role)

This ansible role installs an Oracle MySQL or MariaDB server in a debian environment.

- [Getting Started](#getting-started)
	- [Prerequisities](#prerequisities)
	- [Installing](#installing)
- [Usage](#usage)
- [Testing](#testing)
- [Built With](#built-with)
- [Versioning](#versioning)
- [Authors](#authors)
- [License](#license)
- [Contributing](#contributing)

## Getting Started

These instructions will get you a copy of the role for your Ansible playbook. Once launched, it will install an [MySQL Database](https://www.mysql.com/) or [MariaDB server](https://mariadb.org/) in a Debian system.

### Prerequisities

Ansible >= 2.9 version installed.
Inventory destination should be a Debian environment.

For testing purposes, [Molecule](https://molecule.readthedocs.io/) with Docker as driver and [Goss](https://goss.rocks/) as verifier.

### Installing

Create or add to your roles dependency file (e.g requirements.yml):

```
- src: idealista.mysql_role
  version: 4.5.0
  name: mysql
```

Install the role with ansible-galaxy command:

```
ansible-galaxy install -p roles -r requirements.yml -f
```

Use in a playbook:

```
---
- hosts: someserver
  roles:
    - role: mysql
```

## Usage


Installation tasks follows the install guide: https://dev.mysql.com/doc/mysql-apt-repo-quick-guide/en/

Look to the [defaults](defaults/main.yml) properties file to see the possible configuration properties.

Set at least mysql_root_user and mysql_root_password:

```yaml
mysql_root_user: mysql         # Change mysql root user
mysql_root_password: secret    # Change mysql root password
```

Add any number of databases and create users with privs on them

```yaml
mysql_databases:
   - name: example_DB
     encoding: utf8
   - name: anotherExample_DB

mysql_users:
   - name: admin_user
     host: 127.0.0.1
     password: secret
     priv: [ *.*:USAGE ]
   - name: example_user
     host: *
     password: secret
     priv: [ example_DB.*:ALL ]
```

### Selecting a major release version

Major releases of MySQL can be selected using `mysql_server_version`. You can see the available options in the MySQL Debian mirror.

## Testing

```
$ pipenv sync
$ pipenv run molecule test --all
```

To check the installation, example with Oracle's MySQL implementation:

```bash
$ pipenv run molecule converge --scenario-name=mysql
$ pipenv run molecule login --scenario-name=mysql

root@mysql:/# mysql -u root -ptesting

mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| test01             |
| performance_schema |
+--------------------+
4 rows in set (0.00 sec)
```

 ## Known Issues
  There is a problem while trying to remount /run using the role. If you need to assign a new size for mysql use this in your playbook
```yaml
- name: MySQL | Remounting /run
  shell: mount -t tmpfs tmpfs /run -o remount,size={{ mysql_remount_run_partition_size }}
  changed_when: false
  tags:
    skip_ansible_lint
  when: mysql_remount_run
```


## Built With

![Ansible](https://img.shields.io/badge/ansible-5.2.0-green.svg)
![Molecule](https://img.shields.io/badge/molecule-3.4.2-green.svg)
![Goss](https://img.shields.io/badge/goss-0.3.16-green.svg)

## Versioning

For the versions available, see the [tags on this repository](https://github.com/idealista/mysql_role/tags).

Additionaly you can see what change in each version in the [CHANGELOG.md](CHANGELOG.md) file.

## Authors

* **Idealista** - *Work with* - [idealista](https://github.com/idealista)

See also the list of [contributors](https://github.com/idealista/mysql_role/contributors) who participated in this project.

## License

![Apache 2.0 License](https://img.shields.io/hexpm/l/plug.svg)

This project is licensed under the [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) license - see the [LICENSE](LICENSE) file for details.

## Contributing

Please read [CONTRIBUTING.md](.github/CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.
