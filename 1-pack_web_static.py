#!/usr/bin/python3
"""Deployment process: Stage 1"""
import datetime
from fabric.api import local


def do_pack():
    """Returns the file path if has been correctly generated.
    Otherwise, returns none"""
    local("mkdir -p versions")
    date = datetime.strftime(datetime.now(), '%Y%m%d%H%M%S')
    file = local("tar -cvzf versions/web_static_{}.tgz web_static"
                 .format(datetime.strftime(datetime.now(), '%Y%m%d%H%M%S')))
    if file.failed:
        return None
    return ("versions/web_static_{}.tgz".format(date))
