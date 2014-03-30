__author__ = 'Javier'


# doc: https://expects.readthedocs.org/en/0.2.0/
from expects import expect
from presenter.ReportStatsPresenter import ReportStatsPresenter
from LaBSKApi.reportstats import ReportStatsService
from LaBSKApi.MongoDB import MongoDB



def _create_presenter():
    return ReportStatsPresenter(ReportStatsService(MongoDB()))

"""
    Scenario: Estadisticas diarias de EDGE
		Given las estadisticas de lo que se habla cada dia
		When solicito las estadisticas del informe "Editorial EDGE Entertainment"
		Then el informe contiene informacion de la fecha "2014-3-26"
         And muestra "0" blogs, "324" asuntos y "1207" mensajes
         And muestra un incemento de "0" blogs, "0" asuntos y "0" mensajes
"""

@given('las estadisticas de lo que se habla cada dia')
def estadticas_de_lo_que_se_habla(context):
    context.stats_presenter = _create_presenter()

@when('solicito las estadisticas del informe "{nombre_informe}"')
def solicito_estadisticas_del_informe(context, nombre_informe):
    context.table_stats = context.stats_presenter.stats_from_report(nombre_informe)

@then('el informe contiene informacion de la fecha "{fecha}"')
def informe_contiene_informacion_fecha(context, fecha):
    rows = context.table_stats.rows
    found = False
    for row in rows:
        if row[0] == fecha:
            found = True
            break
    #print rows
    expect(found).to.be(True)


# Esto e suna mala prueba porque me ato a una representacon concreta
# Si cmabio las cosas de celda la prueba falla sin necesidad.
@then('muestra "{blogs}" blogs, "{asuntos}" asuntos y "{mensajes}" mensajes')
def muestra_blogs_asuntos_y_mensajes(context, blogs, asuntos, mensajes):
    row = context.table_stats.rows[0]
    #print cell, blogs, cell == blogs, context.table_stats.cell(1), context.table_stats.cell(2)
    expect(row[5]).to.equal(blogs)
    expect(row[3]).to.equal(asuntos)
    expect(row[1]).to.equal(mensajes)

@then('muestra un incemento de "{blogs}" blogs, "{asuntos}" asuntos y "{mensajes}" mensajes')
def incremento_de_blogs_asuntos_y_mensajes(context, blogs, asuntos, mensajes):
    row = context.table_stats.rows[0]
    expect(row[6]).to.equal(blogs)
    expect(row[4]).to.equal(asuntos)
    expect(row[2]).to.equal(mensajes)
