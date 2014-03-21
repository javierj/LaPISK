__author__ = 'Javier'

#import sure
from LaBSKApi.MongoDB import MongoDB
from LaBSKApi.reports import ReportBuilder
from presenter.ReportPresenter import ReportPresenter
from expects import expect

# doc: https://expects.readthedocs.org/en/0.2.0/
#
# Helppers
#
def crea_informe(name="Name", keywords=None):
    return {'name': name, 'keywords': (keywords or [])}

def create_report(context):
    presenter = ReportPresenter(ReportBuilder(context.db))
    presenter.database = context.db
    return presenter

"""
	Scenario encontrar hilos que mencionan un juego
		given Las noticias de LaBSK
		when solicito el informe del juego "EONS"
		then el informe contiene el hilo "EONS, para los creadores de universos"

"""

@given('las noticias de LaBSK')
def given_labsk(context):
    #context.db = MockMongo()
    context.db = MongoDB(col="labsk_test")
    # cuendo uso MongoDB falla y no se por que
    # no es que me de un error la clase, sino que lanza una
    # excepcion y behave no puede tratarla bien y me sala otra
    # excepcion

@when('solicito el informe del juego "{word}"')
def when_generating_report(context, word):
    presenter = create_report(context)
    informe = crea_informe(keywords=[word])
    context.informe = presenter.report_and_stats(informe).report
    context.keyword = word


@then('el informe contiene el hilo "{titulo_del_hilo}"')
def assert_titulo_del_hilo(context, titulo_del_hilo):
    threads = context.informe[context.keyword]
    title = threads[0]['title']
    #title.should.equal(titulo_del_hilo)
    print threads
    expect(title).to.equal(titulo_del_hilo)


"""
    Scenario: encontrar hilos que mencionan una editorial
		Given las noticias de LaBSK
		When solicito el informe de la editorial "MasQueOca"
		Then el informe contiene "2" hilos distintos
"""
@when('solicito el informe de la editorial "{word}"')
def when_generating_report_from_editor(context, word):
    presenter = create_report(context)
    informe = crea_informe(keywords=[word])
    context.informe = presenter.report_and_stats(informe).report
    context.keyword = word

@then('el informe contiene "{numero}" hilos que la mencionan en el titulo')
def assert_hilos_del_informe(context, numero):
    count = int(numero)
    all_threads = context.informe[context.keyword]
    threads = [m for m in all_threads if context.keyword in m['title']]
    #threads.should.have.length_of(count)
    expect(threads).to.have.length(count)

@then('"{numero}" hilos que la mencionan en un mensaje')
def assert_hilos_con_mensajes(context, numero):
    count = int(numero)
    all_threads = context.informe[context.keyword]
    threads = [m for m in all_threads if context.keyword in m['title']]
    #threads.should.have.length_of(count + result)
    expect(all_threads).to.have.length(count + len(threads))
    #result.should.equal(0)

"""
	Scenario: encontrar mensajes que mencionan un juego
		Given las noticias de LaBSK
		When solicito el informe del juego "D&D"
		Then obtengo el hilo  con enlace "http://labsk.net/index.php?topic=127181.0"
        And "1" mensaje del usuairo "Ech-Pi-El"
"""
@then(u'obtengo el hilo con enlace "{URL}"')
def assert_Url(context, URL):
    keyword = context.keyword
    threads = context.informe[keyword]
    #threads.should.have.length_of(1)
    expect(threads).to.have.length(1)
    context.thread = threads[0]
    #context.thread['link'].should.equal(URL)
    expect(context.thread['link']).to.equal(URL)


@then(u'"{numero}" mensaje del usuairo "{usuario}"')
def assert_messages_and_user(context, numero, usuario):
    count = int(numero)
    #context.thread['msgs'].should.have.length_of(count)
    expect(context.thread['msgs']).to.have.length(count)
    msg = context.thread['msgs'][0]
    #msg['user'].should.equal(usuario)
    expect(msg['user']).to.equal(usuario)


"""
    Scenario: sin menciones del juego
		Given Las noticias de LaBSK
		When solicito el informe del juego "Castle Rising"
		Then el informe esta vacio
"""
@then(u'el informe esta vacio')
def assert_informe_vacio(context):
    threads = context.informe[context.keyword]
    #threads.should.have.length_of(0)
    expect(threads).to.have.length(0)

"""
   Scenario: sin mensajes anteriores al 2.013
   		Given Las noticias de LaBSK
		When solicito el informe de la palabra clave "ANTerpryse" del hilo http://labsk.net/index.php?topic=89024.0
		Then el informe contiene un mensaje de "2013"
"""

@when('solicito el informe de la palabra clave "{keyword}" del hilo http://labsk.net/index.php?topic=89024.0')
def when_generating_report_from_keyword(context, keyword):
    presenter = create_report(context)
    informe = crea_informe(keywords=[keyword])
    context.informe = presenter.report_and_stats(informe, data_filter = "2012").report
    #presenter.(informe).
    context.keyword = keyword

@then(u'el informe contiene un unico mensaje de "{year}"')
def assert_informe_contiene_2013(context, year):
    threads = context.informe[context.keyword]
    expect(threads).to.have.length(1)
    msgs = threads[0]['msgs']
    expect(msgs).to.have.length(1)
    # Esto no se como hacerlo en expect
    assert year in msgs[0]['date']

"""
    Scenario: estadistcas de mensajes e hijos
   		Given Las noticias de LaBSK
	    When solicito las estadisticas del juego "Grenadier" con enlace "http://labsk.net/index.php?topic=127181.0"
		Then el informe contiene "1" asunto y "3" mensajes
"""

@when('solicito las estadisticas del juego "{keyword}" con enlace "http://labsk.net/index.php?topic=127181.0"')
def when_generating_report_and_stats_from_keyword(context, keyword):
    presenter = create_report(context)
    informe = crea_informe(keywords=[keyword])
    context.report_and_stats = presenter.report_and_stats(informe)

@then(u'el informe contiene "{threads}" asunto y "{msgs}" mensajes')
def assert_informe_contiene_asuntos_y_mensajes(context, threads, msgs):
    reportstats = context.report_and_stats.report_stats
    text = reportstats.get_text()
    expect(text).to.have.length(2)
    expect(text[0]).to.equal(u'Asuntos encontrados: '+threads)
    expect(text[1]).to.equal(u'Mensajes encontrados: '+msgs)


"""
    find_title('Devir')
    find_one('http://labsk.net/index.php?topic=122738.0') -- Mensajes de 2013 y 2014.
    find_one('http://labsk.net/index.php?topic=121657.0') -- Solo mensajes de 2013

    Scenario: sin hilos anteriores al 2.013
   		Given Las noticias de LaBSK
		When solicito el informe de la palabra clave "Devir"
         And filtro por el anyo "2013"
         Then solo aparece "4" asuntos con mensajes del "2014"


		Then solo aparece el asunto "http://labsk.net/index.php?topic=122738.0" en el resultado
         And el asunto contiene "X" mensajes, todos de 2.014
"""

@when('solicito el informe de la palabra clave "{keyword}"')
def when_storing_keyword_in_context(context, keyword):
    context.keyword = keyword

@when('filtro por el anyo "{year}"')
def when_filterinf_by_year(context, year):
    presenter = create_report(context)
    query_informe = crea_informe(keywords=[context.keyword])
    context.report_and_stats = presenter.report_and_stats(query_informe, filter_year = year)

@then(u'solo aparece "{thread_count}" asuntos con mensajes del "{year}"')
def assert_solo_aparece_asunto(context, thread_count, year):
    report = context.report_and_stats.report
    expect(report[context.keyword]).to.have.length(int(thread_count))
    for t in report[context.keyword]:
        #print year, ', ', t['last_msg_date'], "<<<"
        #if t['last_msg_date'] <> " ":
        assert year in t['last_msg_date']
