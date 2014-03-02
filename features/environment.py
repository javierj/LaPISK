__author__ = 'Javier'

from webgui import flaskweb


my_context = None


def mock_render_template(template_name_or_list, **context):
    global my_context
    my_context.render_context = context


def before_scenario(context, scenario):
    print "---------------------"
    global my_context
    my_context = context
    flaskweb.app.config['TESTING'] = True
    context.webapp = flaskweb.app.test_client()
    context.webapp.render_template = mock_render_template
    context.flaskweb = flaskweb
