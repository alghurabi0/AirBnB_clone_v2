#!/usr/bin/python3
"""
Fabric script that deletes out-of-date archives.
"""

from fabric.api import env, local, run
from datetime import datetime
from os.path import exists


env.hosts = ['54.144.146.250', '34.227.89.63']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/school'  # Replace with the path to your private key


def do_clean(number=0):
    """
    Deletes unnecessary archives in the versions and releases folders.
    """
    try:
        number = int(number)
        if number < 0:
            return False
        if number == 0 or number == 1:
            number = 1
        else:
            number += 1

        # Clean versions folder
        local("ls -lt versions | grep -v ^total | awk 'NR>{}' | xargs -I {{}} rm versions/{{}}".format(number))

        # Clean releases folder on each server
        run("ls -lt /data/web_static/releases | grep -v ^total | awk 'NR>{}' | xargs -I {{}} rm -rf /data/web_static/releases/{{}}".format(number))

        return True
    except Exception as e:
        return False


if __name__ == "__main__":
    do_clean()
