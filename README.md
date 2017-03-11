![Logo](logo.gif)

# MySQL Ansible role

This ansible role installs a Prometheus Node Exporter in a debian environment.

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

These instructions will get you a copy of the role for your ansible playbook. Once launched, it will install an [MySQL Database](https://www.mysql.com/) in a Debian system.

### Prerequisities

Ansible 2.2.0.0 version installed.
Inventory destination should be a Debian environment.

For testing purposes, [Molecule](https://molecule.readthedocs.io/) with [Vagrant](https://www.vagrantup.com/) as driver (with [landrush](https://github.com/vagrant-landrush/landrush) plugin) and [VirtualBox](https://www.virtualbox.org/) as provider.

### Installing

Create or add to your roles dependency file (e.g requirements.yml):

```
- src: http://github.com/idealista-tech/mysql-role.git
  scm: git
  version: 1.0.0
  name: mysql-role
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
mysql_root_password: secret   # Change mysql root password
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

## Testing

```
molecule test
```

To check the installation

```bash
molecule converge
molecule login

vagrant@mysql:~$ mysql -u root -pdefault

mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| mysql_test         |
| performance_schema |
+--------------------+
4 rows in set (0.00 sec)
```

## Built With

![Ansible](https://img.shields.io/badge/ansible-2.2.0.0-green.svg)

## Versioning

For the versions available, see the [tags on this repository](https://github.com/idealista-tech/mysql-role/tags).

Additionaly you can see what change in each version in the [CHANGELOG.md](CHANGELOG.md) file.

## Authors

* **Idealista** - *Work with* - [idealista-tech](https://github.com/idealista-tech)

See also the list of [contributors](https://github.com/idealista-tech/mysql-role/contributors) who participated in this project.

## License

![Apache 2.0 Licence](https://img.shields.io/hexpm/l/plug.svg)

This project is licensed under the [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) license - see the [LICENSE.txt](LICENSE.txt) file for details.

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.
