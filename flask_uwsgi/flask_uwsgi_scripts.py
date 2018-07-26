"""
    Author: Chinmay Bhoir
    Created on: 25/7/18 6:55 PM
"""

REQUIREMENTS_SCRIPT = """flask
flask_cors
"""

UWSGI_INI_SCRIPT = """[uwsgi]
#chdir = 
plugins = python3
protocol = http
#socket = /tmp/flask_server.sock
http-socket = 0.0.0.0:8000
wsgi-file = server_flask.py
callable = application
master = true
processes = 4
threads = 4
workers = 4
"""

SERVER_FLASK_SCRIPT = """from flask import Flask
from flask_cors import CORS

application = Flask(__name__)
CORS(application)

@application.route("/hello_world")
def hello_world():
    return "Hello World"
"""

