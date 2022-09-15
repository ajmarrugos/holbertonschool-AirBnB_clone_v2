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
        put(archive_path, '/tmp/')

        file = archive_path.split('/')[-1].split('.')[0]
        run('mkdir -p /data/web_static/releases/{}/'.format(file))
        run('tar -xzf /tmp/{}.tgz -C /data/web_static/releases/{}'
            .format(file, file))
        run('rm /tmp/{}.tgz'.format(file))
        run('mv /data/web_static/releases/{}/web_static/* \
            /data/web_static/releases/{}'.format(file, file))
        run('rm -rf /data/web_static/releases/{}/web_static'.format(file))
        run('rm -rf /data/web_static/current')
        run('ln -s /data/web_static/releases/{}\
            /data/web_static/current'.format(file))
        return True

    except Exception as exc:
        print(exc)
        return False
