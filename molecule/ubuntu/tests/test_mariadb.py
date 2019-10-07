import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_mariadb_package(host):
    """ check if packages are installed
    """
    assert host.package('mariadb-server').is_installed
    assert host.package('mariadb-client').is_installed
    assert host.package('openssl').is_installed


def test_mariadb_server_config(host):
    f = host.file('/etc/mysql/mariadb.conf.d/50-server.cnf')
    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_mariadb_logdir(host):
    d = host.file('/var/log/mysql')
    assert d.is_directory


def test_mariadb_server_innodb_config(host):
    f = host.file('/etc/mysql/conf.d/innodb.cnf')
    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_mariadb_service(host):
    """ Testing whether the service is running and enabled
    """
    assert host.service('mysql').is_enabled
    assert host.service('mysql').is_running
