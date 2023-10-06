#!/usr/bin/python3
"""
A Fabric script that creates and distributes an archive file
to web servers.
"""
from fabric.api import local, run, put, env
from datetime import datetime
import os


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


def do_deploy(archive_path):
    """
    Function to deploy an archive file using fabric.
    """
    if not os.path.exists(archive_path):
        return False
    env.host = ["54.196.42.35", "34.229.56.179"]
    try:
        archive_file = os.path.basename(archive_path)
        archive_name = archive_file.split(".")[0]

        upload = put(archive_path, "/tmp/")
        run("mkdir -p /data/web_static/releases/{}/".format(archive_name))
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".format(
            archive_file, archive_name))

        run("rm /tmp/{}".format(archive_file))
        run("mv /data/web_static/releases/{}/web_static/* "
            "/data/web_static/releases/{}/".format(
                archive_name, archive_name))
        run("rm -rf /data/web_static/current")
        run("ln -sf /data/web_static/releases/{}/ /data/web_static/current"
            .format(archive_name))
        return True
    except Exception as e:
        return False
