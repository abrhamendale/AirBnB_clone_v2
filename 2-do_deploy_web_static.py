#!/usr/bin/python3
"""
Web_static
"""
import os
from fabric.api import *
from fabric.operations import run, put, sudo
env.hosts = ['54.242.195.19', '54.236.50.27']


def do_deploy(archive_path):
    """Deploys web_static to the web servers"""
    if (os.path.isfile(archive_path) is False):
        return False
    try:
        arcname = archive_path.split("/")[-1]
        arcpath = ("/data/web_static/releases/" + arcname.split(".")[0])
        put(archive_path, "/tmp/")
        run("sudo mkdir -p {}".format(arcpath))
        run("sudo tar -xzf /tmp/{} -C {}".format(arcname, arcpath))
        run("sudo rm /tmp/{}".format(arcname))
        run("sudo mv {}/web_static/* {}/".format(arcpath, arcpath))
        run("sudo rm -rf {}/web_static".format(arcpath))
        run('sudo rm -rf /data/web_static/current')
        run("sudo ln -s {} /data/web_static/current".format(arcpath))
        return True
    except:
        return False
