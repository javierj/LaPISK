__author__ = 'Javier'


import unittest
from flask import Flask, request

app = Flask(__name__)
app.testing = True

@app.route('/action')
def action():
    print "Request", request.data
    print "Headers", request.headers
    return ""


class MyTestCase(unittest.TestCase):

    def test_get_with_path(self):
        with app.test_client() as c:
            rv = c.get('/action?vodka=42')
            print request.data
            assert 'vodka' in request.args # assertion OK
        print "Helo"

    def test_get_with_complete_url(self):
        with app.test_client() as c:
            rv = c.get('http://domain.com/action?vodka=42')
            assert 'vodka' in request.args # assertion error

    def test_post_with_complete_url(self):
        with app.test_client() as c:
            rv = c.post('http://domain.com/action?vodka=42', data={'gin': 43})
            assert 'gin' in request.form # assertion OK
            assert 'vodka' in request.args # assertion error


if __name__ == '__main__':
    unittest.main()
