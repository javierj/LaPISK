__author__ = 'Javier'

from datetime import datetime
from expects import expect
from LaBSKApi.statistics import Statistics
from tests.Harness import MockDatetime

##
# Fixtures
mockMongo = None


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
    stats = Statistics(mockMongo)
    stats._datetime = MockDatetime(None)
    context.flaskweb.set_stats_module(stats)
    context.fecha_acceso = stats._datetime.set_datetime(fecha, hora)

    #context.flaskweb.g['s']  = Statistics(mockMongo)

    #context.fecha_acceso = context.webapp.datetime_module.set_datetime(fecha, hora)
    #context.statistics_module.register_access('/', context.fecha_acceso)
    context.webapp.get('/')


@when('obtengo las estadisticas')
def obtengo_las_estadisticas(context):
    # Demo de como acceder al reder de flask
    # context.webapp.render_template("demo", a = 'a')
    # expect(context.render_context['a']).to.equal('a')
    pass

@then('veo una visita a "{url}" a la hora de la visita')
def veo_una_visita_a_main(context, url):
    # change this line for a template dendering stats
    visits = context.flaskweb.stats_module.all_visits()

    expect(visits).to.have.length(1)
    expect(context.fecha_acceso).to.equal(visits[0].access_datetime)
    expect(url).to.equal(visits[0].url)


