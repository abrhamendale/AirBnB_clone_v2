#!/usr/bin/python3
"""Web_static"""
from fabric.contrib import files
from fabric.api import env, put, run
import os

env.hosts = ['54.242.195.19', '54.236.50.27']


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
        run('mkdir -p {}'.format(arcname))
        run('tar -xzf /tmp/{}.tgz -C {}'.format(slash, arcname))
        run('rm -f /tmp/{}.tgz'.format(slash))
        run('mv {}/web_static/* {}/'.format(arcname, arcname))
        run('rm -rf {}/web_static'.format(arcname))
        run('rm -rf /data/web_static/current')
        run('ln -s {} /data/web_static/current'.format(arcname))
        return True
    except:
        return False
