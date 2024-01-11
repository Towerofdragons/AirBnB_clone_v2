#!/usr/bin/python3
"""
Distributes Archive to servers
"""

from fabric.api import *
import os
#from fabric.api import run
#from fabric.api import local
import datetime

#env.user = 'vagrant'
env.hosts = ['ubuntu@3.94.211.219', 'ubuntu@54.89.60.69']
#env.hosts = ['vagrant@127.0.0.1']

def do_pack():
    """
    Create .tgz archive of web_static for future deployment.
    """
    time = datetime.datetime.now()
    local("mkdir -p versions")
    filename = f"web_static_{time.year}{time.month}{time.day}{time.hour}{time.minute}{time.second}"
    local(f'tar -cvzf versions/{filename}.tgz web_static')
    return filename + ".tgz"


def do_deploy(archive_path):
    """
    Deploy Archive to servers, unpack and establish as relevant version.
    """
    if not os.path.exists(archive_path):
        return false

    arch_split_path = archive_path.split("/")
    arch_base_name = arch_split_path[-1]
    arch_file = arch_base_name
    arch_name_split = arch_file.split(".")
    arch_name = arch_name_split[0]

    #print(arch_name)

    try:

        put(archive_path, '/tmp/')
        arch_dir = f'/data/web_static/releases/{arch_name}'
        sudo(f'mkdir -p {arch_dir}')
        sudo(f'tar -zvxf /tmp/{arch_base_name} -C {arch_dir}')
        sudo(f"rm /tmp/{arch_base_name}")
        sudo("rm /data/web_static/current")
        sudo(f"ln -sf /data/web_static/releases/{arch_dir} /data/web_static/current")
        return True

    except Exception:
        return False
