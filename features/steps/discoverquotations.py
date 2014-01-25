from behave import *

from LaBSKApi.WebClient import WebClient

@given('la pagina de noticias de LaBSK con un listado de asuntos (pagina "{file}")')
def step_impl(context, file):
    context.file = file

@given('una pagina de mensajes LaBSK con un listado de mensajes del juego Fief')
def step_impl(context):
    context.webclient = WebClient("file:///C:/code/workspaces/Python/LaBSK-API/labsk_fief_last_page.html")
	
@given(u'con un mensaje que menciona en el titulo el juego "Sushi"')
def impl(context):
	pass
	
@when('detecto las menciones de "{word}"')
def step_impl(context, word):
	source = open(context.file)
	page = LaBSKThreadListPage(source)
	context.count = page.count(word)
	
@when('quiero saber las menciones del juego "{word}" dentro de los mensajes')
def step_impl(context, word):
	page = LaBSKMessagesPage(context.webclient)
	context.count = page.count(word)

@then('el resultado es {count} mencion (en la primera pagina)')
def step_impl(context, count):
	print "discoveryquiotations: ", context.count, " == ", count
	assert int(context.count) == int(count)
	
@then('el resultado es {count} mencion')
def assert_msgs_in_fief_game(context, count):
	print "Mensajes en Fief: ", context.count, " == ", count
	assert int(context.count) == int(count)

# Scenario: Buscar menciones en el cuerpo del mensajes de dos paginas

def load(self, url):
    self.url = "file:///C:/code/workspaces/Python/LaBSK-API/labsk_fief_last_page.html"
    print self.url

@given('dos paginas de mensajes LaBSK con un listado de mensajes del juego Fief')
def step_impl(context):
    WebClient.load = load
    context.webclient = WebClient("file:///C:/code/workspaces/Python/LaBSK-API/labsk_fief.html")

@when('quiero saber las menciones del juego "{word}" dentro de los mensajes visitanfo ambas paginas')
def step_impl(context, word):
	page = LaBSKMessagesPage(context.webclient)
	context.count = page.count(word)

@then('el resultado es {count} menciones')
def assert_msgs_in_fief_game(context, count):
	print "Mensajes en Fief (varias paginas): ", context.count, " == ", count
	assert int(context.count) == int(count)
