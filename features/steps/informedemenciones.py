__author__ = 'Javier'

#import sure
from LaBSKApi.MongoDB import MongoDB
from presenter.ReportPresenter import ReportPresenter
from expects import expect


#
# Helppers
#
def crea_informe(name="Name", keywords=None):
    return {'name': name, 'keywords': (keywords or [])}

"""
	Scenario encontrar hilos que mencionan un juego
		given Las noticias de LaBSK
		when solicito el informe del juego "EONS"
		then el informe contiene el hilo "EONS, para los creadores de universos"

"""

@given('las noticias de LaBSK')
def given_labsk(context):
    #context.db = MockMongo()
    context.db = MongoDB()
    # cuendo uso MongoDB falla y no se por que
    # no es que me de un error la clase, sino que lanza una
    # excepcion y behave no puede tratarla bien y me sala otra
    # excepcion

@when('solicito el informe del juego "{word}"')
def when_generating_report(context, word):
    presenter = ReportPresenter()
    presenter.database = context.db
    informe = crea_informe(keywords=[word])
    context.informe = presenter.generateReport(informe)
    context.keyword = word


@then('el informe contiene el hilo "{titulo_del_hilo}"')
def assert_titulo_del_hilo(context, titulo_del_hilo):
    threads = context.informe[context.keyword]
    title = threads[1]['title']
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
    presenter = ReportPresenter()
    presenter.database = context.db
    informe = crea_informe(keywords=[word])
    context.informe = presenter.generateReport(informe)
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
    #print  context.informe
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

