import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_mariadb_package(host):
    """ check if packages are installed
    """
    assert host.package('mariadb').is_installed
    assert host.package('mariadb-server').is_installed
    assert host.package('openssl').is_installed


def test_mariadb_server_config(host):
    f = host.file('/etc/my.cnf.d/mariadb-server.cnf')
    assert f.exists
    f = host.file('/etc/my.cnf.d/innodb.cnf')
    assert f.exists


def test_mariadb_service(host):
    """ Testing whether the service is running and enabled
    """
    assert host.service('mariadb').is_enabled
    assert host.service('mariadb').is_running


def test_databases(host):
    """ Test client
    """
    with host.sudo():
        pcs = host.run('mysql -u root -e "show full processlist"')
        assert 'show full processlist' in pcs.stdout
