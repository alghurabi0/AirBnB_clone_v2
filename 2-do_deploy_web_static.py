#!/usr/bin/python3
"""
Fabric script that distributes an archive to your web servers using the
function do_deploy.
"""

from fabric.api import env, put, run
from os.path import exists

env.hosts = ['54.144.146.250', '34.227.89.63']
env.user = 'ubuntu'  # Replace with the appropriate username
env.key_filename = '~/.ssh/school'


def do_deploy(archive_path):
    """
    Distributes an archive to your web servers using the function do_deploy.
    """
    if not exists(archive_path):
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


if __name__ == "__main__":
    # Replace the path with the actual path to your archive
    archive_path = 'versions/web_static_20231206161833.tgz'
    result = do_deploy(archive_path)
    if not result:
        print("Deployment failed.")
