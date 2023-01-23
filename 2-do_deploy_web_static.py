#!/usr/bin/python3
"""
Web_static
"""
from fabric.api import *

def do_deploy(archive_path):
    """
    Distributes an archive to the web servers
    """
    if archive_path is None:
        return False
    with cd ("/tmp"):
        put("/versions/*" "./")
    run ("tar -xf $(archive_path).tar -C /opt/files

