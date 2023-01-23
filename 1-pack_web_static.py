#!/usr/bin/python3
"""
Web static module
"""
from fabric.api import *
from datetime import datetime


def do_pack():
    """
    Generates a tgz archive of web_static
    """
    
    fname = 'web_static' +\
            datetime.now().strftime("%Y%m%d%H%M%S") + ".tgz"
    dname = 'versions/'

    local("mkdir -p " + dname)
    chk = local("tar -cvzf {}{} web_static".format(dname, fname))
    if chk.succeeded:
        return (dname + fname)
    else:
        return (None)
