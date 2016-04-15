from flask import Flask
import json
from service.docker import containers, Container, NotFound

app = Flask(__name__)


@app.route("/containers")
def index():
    return json.dumps(containers())


@app.route("/containers/<id>")
def show(id):
    return json.dumps(Container(id).info())


@app.route("/containers/<id>/start", methods=['POST'])
def start(id):
    Container(id).start()
    return ""


@app.route("/containers/<id>/stop", methods=['POST'])
def stop(id):
    Container(id).stop()
    return ""


@app.errorhandler(500)
def internal_error(error):
    if type(error) is NotFound:
        return json.dumps({'error': str(error)}), 404
    else:
        return json.dumps({'error': str(error)}), 500


def run():
    app.run()
