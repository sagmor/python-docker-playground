from flask import Flask
import json
from service.docker import containers, Container

app = Flask(__name__)

@app.route("/containers")
def index():
    return json.dumps(containers())


@app.route("/containers/<name>")
def show(name):
    return json.dumps(Container(name).info())


@app.route("/containers/<id>/start", methods=['POST'])
def start(id):
    Container(id).start()
    return ""


@app.route("/containers/<name>/stop", methods=['POST'])
def stop(name):
    Container(name).stop()
    return ""

@app.errorhandler(500)
def internal_error(error):
    return json.dumps({'Error': str(error)}), 500


def run():
    app.run()
