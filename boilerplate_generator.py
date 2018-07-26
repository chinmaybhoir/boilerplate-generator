"""
    Author: Chinmay Bhoir
    Created on: 25/7/18 6:51 PM
"""

import os, sys
import argparse
import subprocess
from flask_uwsgi import flask_uwsgi_scripts

parser = argparse.ArgumentParser(description="Boilerplate project structure generator")
parser.add_argument('dirname',
                    help='Give the directory name under which the code will be structured')
parser.add_argument('--python-uwsgi',
                    action='store_true',
                    help='Create project for python-flask-uwsgi based applications')


def write_file(data, directory, filename):
    print("path ", directory, " exists?:", os.path.exists(directory))
    if not os.path.exists(directory):
        cmd = ['mkdir']
        cmd += ["-p"]
        cmd.append(directory)
        subprocess.call(cmd, shell=False)
    with open(directory+"/"+filename, 'w') as fp:
        fp.write(data)


def main():
    args = parser.parse_args()
    dirname = args.dirname
    if args.python_uwsgi is True:
        requirements_script = flask_uwsgi_scripts.REQUIREMENTS_SCRIPT
        uwsgi_ini_script = flask_uwsgi_scripts.UWSGI_INI_SCRIPT
        server_flask_script = flask_uwsgi_scripts.SERVER_FLASK_SCRIPT
        write_file(requirements_script, dirname, "requirements.txt")
        write_file(uwsgi_ini_script, dirname, "uwsgi_ini.ini")
        write_file(server_flask_script, dirname, "server_flask.py")


if __name__ == '__main__':
    main()
