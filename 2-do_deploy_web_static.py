#!/usr/bin/python3
"""Deployment process: Stage 2"""
import time
from os.path import exists
from fabric.api import run, put, local, env

env.hosts = ['35.196.3.36', '204.236.195.39']


def do_pack():
    """Returns the file path if has been correctly generated.
    Otherwise, returns none"""
    timest = time.strftime("%Y%m%d%H%M%S")
    try:
        local("mkdir -p versions")
        local("tar -cvzf versions/web_static_{}.tgz web_static/".
              format(timest))
        return ("versions/web_static_{:s}.tgz".format(timest))
    except Exception:
        return None


def do_deploy(archive_path):
    """Recieves an archive pack and deploys it to the web server"""
    if not exists(archive_path):
        return False

    try:
        file_n = archive_path.split("/")[-1]
        no_ext = file_n.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, no_ext))
        run('tar -xzf /tmp/{} -C {}{}/'.format(file_n, path, no_ext))
        run('rm /tmp/{}'.format(file_n))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, no_ext))
        run('rm -rf {}{}/web_static'.format(path, no_ext))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, no_ext))
        return True
    except:
        return False
