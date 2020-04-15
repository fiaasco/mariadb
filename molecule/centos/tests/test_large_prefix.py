testinfra_hosts = ["ansible://mariadb-centos7"]


def test_mariadb_el7_config(host):
    innodb7 = host.file('/etc/my.cnf.d/innodb.cnf')
    assert not innodb7.contains('innodb_large_prefix=1')


testinfra_hosts = ["ansible://mariadb-centos8"]


def test_mariadb_el8_config(host):
    innodb8 = host.file('/etc/my.cnf.d/innodb.cnf')
    assert not innodb8.contains('innodb_large_prefix=1')
