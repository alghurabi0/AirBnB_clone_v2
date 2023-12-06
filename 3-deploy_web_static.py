#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents of the
web_static folder.
"""


from fabric.api import local, env, put, run
from datetime import datetime
import os


env.hosts = ['54.144.146.250', '34.227.89.63']
env.user = 'ubuntu'  # Replace with the appropriate username
env.key_filename = '~/.ssh/school'


def do_pack():
    """
    Creates a .tgz archive from the contents of the web_static folder.
    """
    try:
        # Create the versions directory if it doesn't exist
        if not os.path.exists("versions"):
            local("mkdir versions")

        # Get the current date and time
        now = datetime.now()
        timestamp = now.strftime("%Y%m%d%H%M%S")

        # Create the archive filename
        archive_name = "web_static_{}.tgz".format(timestamp)

        # Compress the contents of the web_static folder
        local("tar -cvzf versions/{} web_static".format(archive_name))

        # Return the archive path if successful
        return "versions/{}".format(archive_name)
    except Exception as e:
        # Return None if an error occurs
        return None


def do_deploy(archive_path):
    """
    Distributes an archive to your web servers using the function do_deploy.
    """
    if not os.path.exists(archive_path):
        return False

    try:
        # Upload the archive to the /tmp/ directory of the web server
        put(archive_path, "/tmp/")

        # Extract the archive to the folder /data/wethout extension>
        filename = archive_path.split('/')[-1]
        folder = "/data/web_static/releases/{}".format(filename.split(".")[0])
        run("mkdir -p {}".format(folder))
        run("tar -xzf /tmp/{} -C {}".format(filename, folder))

        # Remove the uploaded archive from the web server
        run("rm /tmp/{}".format(filename))

        # Move contents to the new version folder and remove redunday
        run("mv {}/web_static/* {}".format(folder, folder))
        run("rm -rf {}/web_static".format(folder))

        # Remove the current symbolic link
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link to the new version directory
        run("ln -s {} /data/web_static/current".format(folder))

        print("New version deployed!")
        return True
    except Exception as e:
        return False


def deploy():
    """
    Calls do_pack() and do_deploy(archive_path) functions.
    """
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)


if __name__ == "__main__":
    deploy()
