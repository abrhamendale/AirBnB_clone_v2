#!/usr/bin/python3
"""
Web static module
"""
from fabric.api import *

def do_pack():
    """
    Generates a tgz archive of web_static
    """
    run("mkdir -p versions")
    d = web_static_$(date +'%Y%m%d%m%3S')
    with cd ("/verions"):
        arch = local("tar -czf eval(d) web_static tgz")
    if arch.succeeded:
        return '/versions/$(d)'
    else:
        return None
