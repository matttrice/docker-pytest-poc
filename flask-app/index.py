from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route("/ping/<ping>")
def hello_world(ping):
    return f"{escape(ping)}"
