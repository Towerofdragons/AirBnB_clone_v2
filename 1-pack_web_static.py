#!/usr/bin/python3
"""
A Fabric script that generates a .tgz archive from the contents of the
web_static folder of your AirBnB Clone repo, using the function do_pack.
"""
from fabric.api import local
from datetime import datetime

def do_pack():
    """
    Fab function to create a .tgz archive.
    """
    local("mkdir -p versions")
    current_time = datetime.now()
    cur_time = current_time.strftime("%Y%m%d%H%M%S")
    name = "web_static_{}.tgz".format(cur_time)
    result = local("tar -cvzf versions/{} web_static".format(name))
    if result.failed:
        return None
    return "versions/{}".format(name)
