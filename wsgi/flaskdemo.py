"""
Demo for testing OpenShift with Flask.
"""

from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash

app = Flask(__name__)

# Load default config and override config from an environment variable
app.config.update(dict(
    DEBUG=True,
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default'
))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)



@app.route("/")
def main():
    return render_template('hello.html', host="OpenShift")

if __name__ == "__main__":
    app.run()