__author__ = 'Javier'

from datetime import datetime
from expects import expect
from LaBSKApi.statistics import Statistics, Visit
from tests.Harness import create_datetime

##
# Fixtures

mockMongo = None

"""
     def setUp(self):
        #self.db_fd, flaskr.app.config['DATABASE'] = tempfile.mkstemp()
        flaskweb.app.config['TESTING'] = True
        self.app = flaskweb.app.test_client()
"""



"""
   Scenario: Visita de la pagina principal
		Given un visitante que accede a la pagina principal a las '12:00' del '01/01/2013'
		When obtengo las estadisticas
		Then veo una visita a '/' a las '12:00' del '01/01/2014'
"""

@given('un visitante que accede a la pagina principal a las "{hora}" del "{fecha}"')
def given_visitante_que_accede_a_la_pagina_principal(context, hora, fecha):
    context.statistics_module = Statistics(mockMongo)
    context.fecha_acceso = create_datetime(fecha, hora)
    context.statistics_module.register_access('/', context.fecha_acceso)

@when('obtengo las estadisticas')
def obtengo_las_estadisticas(context):
    pass

@then('veo una visita a "{url}" a la hora de la visita')
def veo_una_visita_a_main(context, url):
    visits = context.statistics_module.all_visits()
    expect(visits).to.have.length(1)
    expect(context.fecha_acceso).to.equal(visits[0].access_datetime())
    expect(url).to.equal(visits[0].url())
