# MySQL Role

Ansible role to install and configure mysql and create databases and users

To test it

```bash
molecule test
```

To check the installation

```bash
molecule converge
molecule login

vagrant@mysql:~$ mysql -u root -pvagrant

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

You can configure mysql options under my.cnf overriding options from default vars file. Set at least mysql_root_user and mysql_root_password:

```yaml
mysql_root_user: core         # Change mysql root user
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
