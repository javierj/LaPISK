from behave import *

from LaBSKApi.web import WebClient



@given('una pagina de mensajes LaBSK con un listado de mensajes del juego Fief')
def step_impl(context):
    context.webclient = WebClient("file:///C:/code/workspaces/Python/LaBSK-API/labsk_fief_last_page.html")


@when('quiero saber las menciones del juego "{word}" dentro de los mensajes')
def step_impl(context, word):
	page = LaBSKMessagesPage(context.webclient)
	context.report = page.count(word)

@then('el resultado es {count} mencion')
def assert_msgs_in_fief_game(context, count):
	print "Mensajes en Fief: ", len(context.report), " == ", count
	assert len(context.report) == int(count)

##########################################################################
# Scenario: Buscar menciones en el cuerpo del mensajes de dos paginas

def load(self, url):
    self.url = "file:///C:/code/workspaces/Python/LaBSK-API/labsk_fief_last_page.html"
    print self.url

@given('dos paginas de mensajes LaBSK con un listado de mensajes del juego Fief')
def step_impl(context):
    WebClient.load = load
    context.webclient = WebClient("file:///C:/code/workspaces/Python/LaBSK-API/labsk_fief.html")


@given(u'limite de {limit} paginas')
def set_limit(context, limit):
    context.limit = limit

@when('quiero saber las menciones del juego "{word}" dentro de los mensajes visitanfo ambas paginas')
def step_impl(context, word):
	page = LaBSKMessagesPage(context.webclient, pageslimit = context.limit)
	context.report = page.count(word)

@then('el resultado es {count} menciones')
def assert_msgs_in_fief_game(context, count):
    print "Mensajes en Fief (varias paginas): ", len(context.report), " == ", count
    #assert int(context.count) == int(count)
    assert len(context.report) == int(count)

##############################################################
# Scenario: Buscar menciones en el listado de asuntos (limite 1 por defecto)

class MockLaBSKMessagesPage(object):
    def count(self, word):
        return list()

class MockLaBSKMessagesPageFactory(object):
    def __init__(self):
        self.count = 0
    def create(self, url):
        self.count += 1
        print "MockLaBSKMessagesPageFactory: ", self.count, url
        return MockLaBSKMessagesPage()


@given(u'una pagina de mensajes LaBSK con {ignore} asuntos')
def step_impl(context, ignore):
    context.webclient = WebClient("file:///C:/code/workspaces/Python/LaBSK-API/labsk_moticias.html")

@given(u'uno de los asuntos menciona el juego {ignore}')
def ignore_step(context, ignore):
    pass

@when('quiero entrar en asuntos que no mencionen "{word}"')
def step_impl(context, word):
    mock = MockLaBSKMessagesPageFactory()
    page = LaBSKThreadListPage(context.webclient, mock)
    context.report = page.count(word)
    context.mockcount = mock.count


@then('entro en {count} asuntos a buscar menciones')
def assert_msgs_in_fief_game(context, count):
	print "Paginas vistas: ", context.mockcount, " == ", count
	assert int(context.mockcount) == int(count)


@then('el resultado es {count} mencion (en la primera pagina)')
def step_impl(context, count):
    print "discoveryquiotations: ", len(context.report), " == ", count
    assert len(context.report) == int(count)
