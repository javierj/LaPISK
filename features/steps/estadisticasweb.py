__author__ = 'Javier'

# doc: https://expects.readthedocs.org/en/0.2.0/
from expects import expect
from LaBSKApi.statistics import Statistics
from tests.Harness import MockDatetime, MockMongo
from werkzeug.contrib.fixers import ProxyFix


##
# Fixtures


def create_stats():
    mockMongo = MockMongo()
    stats = Statistics(mockMongo)
    stats._datetime = MockDatetime(None)
    return stats

# This feature uses the before_scenario method in enviroment to set-up
# a flaskweb instance and overrides the render_template method



"""
   Scenario: Visita de la pagina principal
		Given un visitante que accede a la pagina principal a las '12:00' del '01/01/2013'
		When obtengo las estadisticas
		Then veo una visita a '/' a las '12:00' del '01/01/2014'
"""

@given('un visitante que accede a la pagina principal a las "{hora}" del "{fecha}"')
def given_visitante_que_accede_a_la_pagina_principal(context, hora, fecha):
    stats = create_stats()
    context.flaskweb.set_stats_module(stats)
    context.fecha_acceso_esperada = str(stats._datetime.set_datetime(fecha, hora))
    context.webapp.get('/')


@when('obtengo las estadisticas')
def obtengo_las_estadisticas(context):
    # Demo de como acceder al reder de flask
    # context.webapp.render_template("demo", a = 'a')
    # expect(context.render_context['a']).to.equal('a')
    pass

@then('veo una visita a "{url}" a la hora de la visita')
def veo_una_visita_a_main(context, url):
    context.webapp.get('/stats')
    expect(context.render_context).to.have.key('stats_list')
    visits = context.render_context['stats_list']
    expect(visits).to.have.length(1)
    expect(context.fecha_acceso_esperada).to.equal(visits[0].access_datetime)
    expect(url).to.equal(visits[0].url)

"""
    Scenario: Visitante de la pagina principal
		Given un visitante que accede a la pagina principal con la IP "0.0.0.0"
		When obtengo las estadisticas
		Then veo una visita a "/" desde la IP del visitante
"""

@given('un visitante que accede a la pagina principal con la IP "{ip}"')
def given_visitante_que_accede_a_la_pagina_principal(context, ip):
    stats = create_stats()
    context.flaskweb.set_stats_module(stats)
    context.ip_esperada = ip
    #context.webapp.wsgi_app = ProxyFix(context.webapp.wsgi_app)
    context.webapp.get('/', environ_base={'HTTP_X_FORWARDED_FOR': '128.0.0.1',
                                          'HTTP_CLIENT_IP': '129.0.0.1',
                                          'REMOTE_ADDR': "Not in use",
                                          'X-Client-IP': '0',
                                          'X-Original-User-IP': '22',
                                          'X-Forwarded-For': '42, 43, 44',
                                          'HTTP_X_FORWARDED_PROTO': 'a',
                                          'HTTP_X_FORWARDED_HOST': 'x'},
                       headers={'HTTP_X_FORWARDED_FOR': '128.0.0.1',
                                          'HTTP_CLIENT_IP': '129.0.0.1',
                                          'REMOTE_ADDR': "Not in use",
                                          'X-Client-IP': ip,
                                          'X-Original-User-IP': '22',
                                          'X-Forwarded-For': '42, 43, 44',
                                          'HTTP_X_FORWARDED_PROTO': 'a',
                                          'HTTP_X_FORWARDED_HOST': 'x'})

@then('veo una visita a "{url}" desde la IP del visitante')
def veo_una_visita_a_main(context, url):
    context.webapp.get('/stats')
    expect(context.render_context).to.have.key('stats_list')
    visits = context.render_context['stats_list']
    expect(visits).to.have.length(1)
    expect(url).to.equal(visits[0].url)
    expect(context.ip_esperada).to.equal(visits[0].ip)


"""
    Scenario: Visitante administrador
		Given el administrador accede a la pagina principal con la IP "188.78.230.48"
		When obtengo las estadisticas
		Then no veo ninguna visita desde la IP del administrador
"""

@given('el administrador accede a la pagina principal con la IP "{ip}"')
def el_administrador_que_accede_a_la_pagina_principal(context, ip):
    stats = create_stats()
    stats.add_ignore_ip(ip)
    context.flaskweb.set_stats_module(stats)
    context.ip_esperada = ip
    context.webapp.get('/',  headers={'X-Client-IP': ip})

@then('no veo ninguna visita desde la IP del administrador')
def no_veo_ninguna_visita(context):
    context.webapp.get('/stats')
    expect(context.render_context).to.have.key('stats_list')
    visits = context.render_context['stats_list']
    expect(visits).to.be.a(list)
    expect(visits).to.have.length(0)