__author__ = 'Javier'

from webgui import flaskweb

def before_scenario(context, scenario):
    print "---------------------"
    flaskweb.app.config['TESTING'] = True
    context.webapp = flaskweb.app.test_client()