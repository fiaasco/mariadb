import os

import testinfra.utils.ansible_runner
from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = ["ansible://mariadb-centos7"]


def test_mariadb_server_config(host):
    f = host.file('/etc/my.cnf.d/innodb.cnf')
    assert f.contains('innodb_large_prefix=1')
