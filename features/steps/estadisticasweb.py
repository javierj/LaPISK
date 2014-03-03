__author__ = 'Javier'

from datetime import datetime
from expects import expect
from LaBSKApi.statistics import Statistics
from tests.Harness import MockDatetime, MockMongo

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
    context.webapp.get('/')

@then('veo una visita a "{url}" desde la IP del visitante')
def veo_una_visita_a_main(context, url):
    context.webapp.get('/stats')
    expect(context.render_context).to.have.key('stats_list')
    visits = context.render_context['stats_list']
    expect(visits).to.have.length(1)
    expect(context.ip_esperada).to.equal(visits[0].ip)
    expect(url).to.equal(visits[0].url)
