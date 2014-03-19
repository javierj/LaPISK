__author__ = 'Javier'

import unittest
from LaBSKApi.HTML2Objects import MsgFactory, AsuntoFactory, MsgPageFactory
from LaBSKApi.modelobjects import MsgModel, ThreadModel
from LaBSKApi.web import URL
from tests.Harness import MockWebClient, HTMLFactory
from bs4 import BeautifulSoup
from datetime import datetime


class TestMsgFactory(unittest.TestCase):
    def setUp(self):
        self.fragment = HTMLFactory().msg()
        webclient = MockWebClient(HTMLFactory.msg_html())
        self.factory = MsgFactory(webclient)
        self.msg_from_fragment = self.factory.createMsg(self.fragment)
        self.extected_content = u'Content\n'

    def test_user(self):
        self.assertEqual(self.msg_from_fragment['user'], "flOrO")

    def test_date(self):
        self.assertEqual(self.msg_from_fragment['date'],
                         u' 25 de Octubre de 2013, 12:12:00 pm \xbb')

    def test_body(self):
        msg = MsgModel(self.msg_from_fragment)
        self.assertIn("Parece ser que este juego de Asyncro Games",
                      msg.body())

    def test_id(self):
        self.assertEqual(self.msg_from_fragment['id'], "msg_1169262")

    def test_create_list_of_msgs(self):
        msgs = self.factory.createListOfMsgs()
        self.assertEqual(len(msgs), 2)

    def test_create_list_of_msgs_includes_body(self):
        msgs = self.factory.createListOfMsgs()
        msg = msgs[1]
        self.assertEqual(msg['body'], u"Body\n")

    def test_change_url(self):
        webclient = MockWebClient(HTMLFactory.navigation_url())
        self.factory = MsgFactory(webclient)
        url = "xxxx"
        self.factory.changeUrl(url)

        self.assertEqual(url, webclient.url)

    def test_msg_with_HTML_inside(self):
        self.factory = MsgFactory(MockWebClient(HTMLFactory.msg_html()))
        res = self.factory.createMsg(HTMLFactory.msg_with_html)
        self.assertEqual(res['user'], "LudoNoticias")
        msg = MsgModel(res)
        self.assertEqual(msg.body()[:10], "Osprey Pub")

    def test_get_content_recursively_no_tags(self):
        html = BeautifulSoup("Content")
        res = self.factory._get_content_recursively(html)
        self.assertEqual(self.extected_content, res)

    def test_get_content_recursively_one_tag(self):
        html = BeautifulSoup("<strong>Content</strong>")
        res = self.factory._get_content_recursively(html)
        self.assertEqual(self.extected_content, res)

    def test_get_content_recursively_two_tags(self):
        html = BeautifulSoup("<strong><i>Content</i></strong>")
        res = self.factory._get_content_recursively(html)
        self.assertEqual(self.extected_content, res)

    def test_get_content_recursively_list_of_tags(self):
        html = BeautifulSoup("<strong>Content</strong> <i>Content</i>")
        res = self.factory._get_content_recursively(html)
        self.assertEqual(u'Content\n \nContent\n', res)

    def test_get_content_recursively_empty(self):
        html = BeautifulSoup("")
        res = self.factory._get_content_recursively(html)
        self.assertEqual("", res)

    def test_get_date_when_date_is_hoy(self):
        html = BeautifulSoup("""<div class="smalltext">&#171; <strong>Respuesta #45 en:</strong> <strong>Hoy</strong> a las 12:05:56 pm &#187;</div>""")
        self.factory.date_manager.now = TestMsgFactory.mock_hoy
        res = self.factory._get_date(html)
        self.assertEqual(u"1 de Enero de 2014, a las 12:05:56 pm \xbb", res)

    @staticmethod
    def mock_hoy():
        return datetime(2014, 01, 01)



class TestAsuntoFactory(unittest.TestCase):
    def setUp(self):
        self.fragment = HTMLFactory().asunto()
        self.factory = AsuntoFactory()

    def test_title(self):
        res = self.factory.create(self.fragment)
        self.assertEqual(res['title'], u'Robinson Crusoe de Portal Games en espanol (al 95)')

    def test_link(self):
        res = self.factory.create(self.fragment)
        self.assertEqual(res['link'], u'http://labsk.net/index.php?topic=126314.0')

    def test_location(self):
        self.factory.urlobject = URL("Url", "Desc")
        thread = ThreadModel(self.factory.create(self.fragment))
        self.assertEqual(thread.location(), u'Desc')

    def test_location_is_empty_when_no_Urlobject_is_given(self):
        thread = ThreadModel(self.factory.create(self.fragment))
        self.assertEqual(thread.location(), "")

    def test_answers_y_views(self):
        thread = ThreadModel(self.factory.create(self.fragment))
        self.assertEqual(thread.answers(), 10)
        self.assertEqual(thread.views(), "490")

    def test_next_url(self):
        mockweb = MockWebClient(HTMLFactory.navigation_url())
        self.factory = AsuntoFactory(mockweb)
        self.assertEqual(self.factory.nextUrl(), u'http://labsk.net/index.php?board=18.20')

    def test_next_url_is_empty_when_not_next_URL(self):
        mockweb = MockWebClient(HTMLFactory.tablamensajes_html())
        self.factory = AsuntoFactory(mockweb)
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

    def test_when_change_url_descripcion_remains_the_same(self):
        webclient = MockWebClient(HTMLFactory.navigation_url())
        self.factory = AsuntoFactory(webclient)
        self.factory.urlobject = URL("Url", "Desc")
        self.factory.changeUrl("yyy")
        thread = ThreadModel(self.factory.create(self.fragment))
        self.assertEqual(thread.location(), u'Desc')

    def test_create_with_url(self):
        url = "xxx"
        factory = AsuntoFactory(url=url)

        self.assertEqual(url, factory.webclient.url)

    def test_append_if_valid_when_is_Valid(self):
        l = list()
        msg = {'tile': 'x', 'link': 'y'}
        self.factory.append_if_valid(l, msg)
        self.assertEquals(len(l), 1)

    def test_append_if_valid_when_is_not_Valid(self):
        l = list()
        msg = {'tile': "", 'link': ""}
        self.assertEquals(len(l), 0)
        self.factory.append_if_valid(l, msg)
        self.assertEquals(len(l), 0)

    def test_get_number_from(self):
        txt = "10 resuestas"
        self.assertEqual("10",  self.factory._get_number_from(txt))

    def test_create_with_URL_object(self):
        asunto = AsuntoFactory.createFromURLObject(URL("xx", "yy"))
        self.assertEqual(asunto.webclient.url, "xx")


class TestMsgPageFactory(unittest.TestCase):

    def setUp(self):
        self.factory = MsgPageFactory()
        self.url = 'url__'
        self.thread = {'link':self.url}

    def test_create_process(self):
        msgpage = self.factory.create(self.thread )
        self.assertEquals(msgpage.webclient.url, self.url)

    def test_create_with_id_and_url_not_ending_0(self):
        id = "id"
        msgpage = self.factory.create(self.thread, id)
        result = self.url+"."+id
        self.assertEquals(msgpage.webclient.url, result)

    def test_create_with_id_and_url_ending_0(self):
        id = "id"
        self.thread['link'] = self.url+".0"
        msgpage = self.factory.create(self.thread, id)
        result = self.url+"."+id
        self.assertEquals(msgpage.webclient.url, result)


if __name__ == '__main__':
    unittest.main()
