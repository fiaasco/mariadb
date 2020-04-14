testinfra_hosts = ["ansible://mariadb-centos7"]


def test_mariadb_el7_config(host):
    f = host.file('/etc/my.cnf.d/innodb.cnf')
    assert f.contains('innodb_large_prefix=1')


testinfra_hosts = ["ansible://mariadb-centos8"]


def test_mariadb_el8_config(host):
    f = host.file('/etc/my.cnf.d/innodb.cnf')
    assert not f.contains('innodb_large_prefix=1')
