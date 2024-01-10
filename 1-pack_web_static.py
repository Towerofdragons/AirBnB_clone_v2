#!/usr/bin/python3
"""
A Fabric script that generates a .tgz archive from web_static
"""

from fabric.api import run
from fabric.api import local
import datetime
def do_pack():
    time = datetime.datetime.now()
    local("mkdir -p versions")
    filename = f"web_static_{time.year}{time.month}{time.day}{time.hour}{time.minute}{time.second}"
    local(f'tar -cvzf versions/{filename}.tgz web_static')


#web_static_<year><month><day><hour><minute><second>.tgz

"""
time = datetime.datetime.now()

print(time.year)
print(time.month)
print(time.day)
print(time.hour)
print(time.minute)
print(time.second)

filename = f"web_static_{time.year}{time.month}{time.day}{time.hour}{time.minute}{time.second}"
print(filename)
"""
