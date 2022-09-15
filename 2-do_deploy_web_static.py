#!/usr/bin/python3
"""Deployment process: Stage 2"""
import datetime
from os import path
from fabric.api import run, put, local, env

env.hosts = ['35.196.3.36', '204.236.195.39']


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


def do_deploy(archive_path):
    """Recieves an archive pack and deploys it to the web server"""
    if not path.exists(archive_path):
        return False
    archive_nom = archive_path.split('/')[1]
    archive_nom_noext = archive_path.split('/')[1].split('.')[0]
    to_path = '/data/web_static/releases/' + archive_nom_noext
    up_path = '/tmp/' + archive_nom
    put(archive_path, up_path)
    run('mkdir -p ' + to_path)
    run('tar -xzf ' + up_path + ' -C ' + to_path)
    run('rm ' + up_path)
    run('mv ' + to_path + '/web_static/* ' + to_path + '/')
    run('rm -rf ' + to_path + '/web_static')
    run('rm -rf /data/web_static/current')
    run('ln -s ' + to_path + ' /data/web_static/current')
    return True
