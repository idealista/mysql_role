import pytest


@pytest.fixture()
def AnsibleDefaults(Ansible):
    return Ansible("include_vars", "defaults/main.yml")["ansible_facts"]


def test_mysql_packages(Package):
    assert Package("mysql-apt-config").is_installed
    assert Package("python-mysqldb").is_installed
    assert Package("mysql-common").is_installed
    assert Package("mysql-server").is_installed


def test_mysql_service(File, Service, Socket):
    assert File("/etc/init.d/mysql")
    assert Service("mysql").is_enabled
    assert Service("mysql").is_running
    assert Socket("tcp://127.0.0.1:3306")


def test_mysql_database(Command, AnsibleDefaults):
    BD = "echo \'show databases;\'|mysql -u root -pdefault|grep -w test01"
    User = "echo \'show databases;\'|mysql -u testing -ptesting|grep -w test01"
    assert Command(BD).rc is 0
    assert Command(User).rc is 0
