#!/usr/bin/env python

from fabric.api import env
from fabric.api import sudo, roles, parallel, run

env.use_ssh_config = True
env.hosts = ["ip"]
env.user = 'ec2-user'
env.key_filename = '~/.ssh/my.pem'

env.roledefs = {
    'webserver': ['ip'],
    'database': ['ip']
}

# define a special group calle all so we can easily sent out commands to all servers
env.roledefs = [h for r in env.roledefs.values() for h in r]

# the packages that are required to run our application on the server groups
packages_required = {
    "webserver": ['httpd', 'php', 'ntp', 'php-mysql'],
    "database": ['mariadb-server']
}

# files that need to be downloaded from the labserver repo
download_files = {
    'database': ['http://labfiles.linuxacademy.com/python/fabric/sakila.sql',
                 'http://labfiles.linuxacademy.com/python/fabric/sakila-data.sql'],
    'webserver': ['http://labfiles.linuxacademy.com/python/fabric/index.php']
}


# this decorator will make the function following it run for all database group server
@roles('database')
def install_database():
    """
    Install the database application
    sudo is used when you need to run a cmd on the remote server as superuser
    """
    sudo('yum -y install %s' % ''.join(packages_required['database']), pty=True)
    # active MySql/MariaDb in the system control
    sudo('systemctl enable mariadb', pty=True)

    # start MySql/MariaDb using the system control
    sudo('systemctl start mariadb', pty=True)


@parallel
@roles('database')
def setup_database():
    pass


def host_type():
    run('uname -s')


def update_server():
    sudo("yum -y upgrade", pty=True)


if __name__ == "__main__":
    host_type()
