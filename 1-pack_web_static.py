#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents of the
web_static folder.
"""


from fabric.api import local
from datetime import datetime
import os


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


if __name__ == "__main__":
    result = do_pack()
    if result:
        print("{} -> {}\n\nDone.".format(result, os.path.getsize(result)))
    else:
        print("Packaging failed.")
