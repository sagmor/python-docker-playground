from json import dumps
from flask import Flask, url_for
from service.docker import containers, Container, NotFound

app = Flask(__name__)


def append_links(payload):
    payload = payload.copy()
    payload["_links"] = {
            "self": {"href": url_for("show", id=payload["id"])},
            "start": {"href": url_for("start", id=payload["id"]), "method": "POST"},
            "stop": {"href": url_for("stop", id=payload["id"]), "method": "POST"}
            }

    return payload


@app.route("/containers")
def index():
    return dumps([append_links(c) for c in containers()])


@app.route("/containers/<id>")
def show(id):
    return dumps(append_links(Container(id).info()))


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
        return dumps({'error': str(error)}), 404
    else:
        return dumps({'error': str(error)}), 500


def run():
    app.run()
