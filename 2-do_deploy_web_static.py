#!/usr/bin/python3
"""Web_static"""
from fabric.api import *
from fabric.operations import run, put, sudo
import os

env.hosts = ['54.242.195.19', '54.236.50.27']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/school'

def do_deploy(archive_path):
    """Deplos web_static on the web servers."""
    if not os.path.exists(archive_path):
        return False
    path = '/data/web_static/releases/'
    dot = archive_path.split('.')[0]
    slash = dot.split('/')[1]
    arcname = path + slash
    try:
        put(archive_path, '/tmp')
        run('sudo ~/.sshschool mkdir -p {}'.format(arcname))
        run('sudo tar -xzf /tmp/{}.tgz -C {}'.format(slash, arcname))
        run('sudo rm -f /tmp/{}.tgz'.format(slash))
        run('sudo mv {}/web_static/* {}/'.format(arcname, arcname))
        run('sudo rm -rf {}/web_static'.format(arcname))
        run('sudo rm -rf /data/web_static/current')
        run('sudo ln -s {} /data/web_static/current'.format(arcname))
        return True
    except ValueError:
        local('echo "!!!!!"')
        return False
