import os
import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_automysqlbackup_config(host):
    """ check configuration
    """
    f = host.file('/etc/default/automysqlbackup')
    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'
    assert f.contains('BACKUPDIR="/var/lib/automysqlbackup"')
    assert f.contains('MAILADDR="admin@mole.cule"')


@pytest.mark.parametrize('db', ['molecule', 'molecule2'])
def test_automysqlbackup_outdir(host, db):
    """ check db dumps (side-effect)
    """
    d = host.file('/var/lib/automysqlbackup/daily/%s' % db)
    assert d.is_directory
