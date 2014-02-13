__author__ = 'Javier'

import unittest
from LaBSKApi.HTML2Objects import MsgFactory, AsuntoFactory, MsgPageFactory

from Harness import MockWebClient, HTMLFactory


class TestMsgFactory(unittest.TestCase):
    def setUp(self):
        self.fragment = HTMLFactory().msg()
        webclient = MockWebClient(HTMLFactory.msg_html())
        self.factory = MsgFactory(webclient)

    def test_user(self):
        res = self.factory.createMsg(self.fragment)
        self.assertEqual(res['user'], "flOrO")

    def test_date(self):
        res = self.factory.createMsg(self.fragment)
        self.assertEqual(res['date'], u' 25 de Octubre de 2013, 12:12:00 pm \xbb')

    """
    def test_body(self):
        res = self.factory.createMsg(self.fragment, "XX")
        self.assertEqual(res['body'], "XX")
    """

    def test_create_with_webclient(self):
        res = self.factory.create()
        self.assertEqual(res['date'], u' 25 de Octubre de 2013, 12:12:00 pm \xbb')
        self.assertEqual(res['user'], "flOrO")

    def test_create_list_of_msgs(self):
        msgs = self.factory.createListOfMsgs()
        self.assertEqual(len(msgs), 2)

    def test_create_list_of_msgs_includes_body(self):
        msgs = self.factory.createListOfMsgs()
        msg = msgs[1]
        self.assertEqual(msg['body'], u"Body")

    def test_change_url(self):
        webclient = MockWebClient(HTMLFactory.navigation_url())
        self.factory = MsgFactory(webclient)
        url = "xxxx"
        self.factory.changeUrl(url)

        self.assertEqual(url, webclient.url)




class TestAsuntoFactory(unittest.TestCase):
    def setUp(self):
        self.fragment = HTMLFactory().asunto()
        self.factory = AsuntoFactory()

    def test_title(self):
        res = self.factory.create(self.fragment)
        #print res['title']
        self.assertEqual(res['title'], u'Robinson Crusoe de Portal Games en espanol (al 95)')

    def test_link(self):
        res = self.factory.create(self.fragment)
        #print res['link']
        self.assertEqual(res['link'], u'http://labsk.net/index.php?topic=126314.0')

    def test_next_url(self):
        mockweb = MockWebClient(HTMLFactory.navigation_url())
        self.factory =  AsuntoFactory(mockweb)
        self.assertEqual(self.factory.nextUrl(), u'http://labsk.net/index.php?board=18.20')

    def test_next_url_is_empty_when_not_next_URL(self):
        mockweb = MockWebClient(HTMLFactory.tablamensajes_html())
        self.factory =  AsuntoFactory(mockweb)
        self.assertEqual(self.factory.nextUrl(), "")

    def test_create_asuntos(self):
        res = self.factory.createListOfAsuntos(HTMLFactory.tablamensajes())
        self.assertEquals(2, len(res))
        self.assertEqual(res[0]['title'], u'1936 guerra civil -  D6')
        self.assertEqual(res[1]['title'], u'Temporada de Regionales 2014 de Edge')

    def test_create_webclient(self):
        mockweb = MockWebClient(HTMLFactory.tablamensajes_html())
        self.factory =  AsuntoFactory(mockweb)
        res = self.factory.createListOfAsuntos()
        self.assertEquals(2, len(res))
        self.assertEqual(res[0]['title'], u'1936 guerra civil -  D6')
        self.assertEqual(res[1]['title'], u'Temporada de Regionales 2014 de Edge')

    def test_change_url(self):
        webclient = MockWebClient(HTMLFactory.navigation_url())
        self.factory = AsuntoFactory(webclient)
        url = "xxxx"
        self.factory.changeUrl(url)

        self.assertEqual(url, webclient.url)


class TestMsgPageFactory(unittest.TestCase):

    def test_create_process(self):
        factory = MsgPageFactory()
        url = 'url__'
        thread = {'link':url}
        msgpage = factory.create(thread)

        self.assertEquals(msgpage.webclient.url, url)

if __name__ == '__main__':
    unittest.main()
