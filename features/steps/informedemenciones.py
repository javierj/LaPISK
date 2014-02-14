__author__ = 'Javier'

import sure

"""
	Scenario encontrar hilos que mencionan un juego
		given Las noticias de LaBSK
		when solicito el informe del juego "EONS"
		then el informe contiene el hilo "EONS, para los creadores de universos"

"""
@given('Las noticias de LaBSK')
def given_labsk(context):
    pass

@when('solicito el informe del juego "{word}"')
def when_generating_report(context, word):
    informeBuilder = ReportBuilder()
    context.informe = dict()

@then('el informe contiene el hilo "{titulo_del_hilo}"')
def assert_titulo_del_hilo(context, titulo_del_hilo):
    hilo = None
    #assertEquals(, titulo_del_hilo)
    #assertEquals(True, False)
    context.informe['title'].should.equal(titulo_del_hilo)



# Exceptiones

failureException = AssertionError  # es del propio lenguage

def fail( msg=None):
    """Fail immediately, with the given message."""
    raise failureException, msg


def failIf(expr, msg=None):
    "Fail the test if the expression is true."
    if expr: raise failureException, msg

def failUnlessEqual(first, second, msg=None):
    """Fail if the two objects are unequal as determined by the '=='
       operator.
    """
    if not first == second:
        raise failureException, \
            (msg or '%r != %r' % (first, second))


assertEqual = assertEquals = failUnlessEqual