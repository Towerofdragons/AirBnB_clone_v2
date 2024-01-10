#!/usr/bin/python3
"""
A Fabric script that generates a .tgz archive from web_static
"""

from fabric.api import run
from fabric.api import local
import datetime


def do_pack():
    """
    Create .tgz archive of web_static for future deployment.
    """

    time = datetime.datetime.now()
    local("mkdir -p versions")
    filename = f"web_static_{time.year}{time.month}{time.day}{time.hour}{time.minute}{time.second}"
    local(f'tar -cvzf versions/{filename}.tgz web_static')
    return filename + ".tgz"
