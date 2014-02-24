"""
Demo for testing OpenShift with Flask.
"""

from flask import Flask, render_template
from pymongo import MongoClient
import os

app = Flask(__name__)

# Load default config and override config from an environment variable
app.config.update(dict(
    DEBUG=False,
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default'
))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)



@app.route("/")
def main():
    MONGODB_URI = os.environ['OPENSHIFT_MONGODB_DB_HOST']+":"+os.environ['OPENSHIFT_MONGODB_DB_PORT']
    Connection_URL = "mongodb://" + MONGODB_URI + "/"
    client = MongoClient(Connection_URL)
    client.phorumledge.authenticate("admin","9UsXjxnQelHf")
    return render_template('hello.html',
                           host="OpenShift",
                           db = client.phorumledge)

if __name__ == "__main__":
    app.run()