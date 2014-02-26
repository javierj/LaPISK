__author__ = 'Javier'

import unittest

from LaBSKApi.HTML2Objects import AsuntoFactory, MsgFactory
from LaBSKApi.Process import ProcessThreads, ProcessMsgs, ProcessThread
from LaBSKApi.modelobjects import ThreadModel
from tests.Harness import MockWebClient, HTMLFactory, MockMongo, Reports
from mockito import mock, verify, any, when


class MockMsgPageFactory(object):
    def create(self, thread):
        return MsgFactory( MockWebClient(HTMLFactory.msg_html()))


class TestProcessThreads(unittest.TestCase):

    def setUp(self):
        mockweb = MockWebClient(HTMLFactory.tablamensajes_html())
        self.threadfactory = AsuntoFactory(mockweb)
        self.mongo = MockMongo()
        self.processthread = ProcessThreads(self.mongo, MockMsgPageFactory())
        self.navhtml = HTMLFactory.tablamensajes_html() +  HTMLFactory.navigation_url()

    def test_getlistofthreads(self):
        self.assertEquals("", self.threadfactory.nextUrl())
        self.processthread.storeThreads(self.threadfactory)

        self.assertEquals(2, self.mongo.treadssaved)

    def test_createThreadStruct_with_msgs(self):
        self.processthread.storeThreads(self.threadfactory)

        self.assertEquals(2, len(self.mongo.listofthreads))
        thread = self.mongo.listofthreads[0]
        self.assertEqual(2, len(thread['msgs']))

    def test_default_pagelimit_is_1(self):
        mockweb = MockWebClient(self.navhtml)
        self.processthread.storeThreads(AsuntoFactory(mockweb))

        self.assertEquals(2, len(self.mongo.listofthreads))

    def test_two_loops(self):
        mockweb = MockWebClient(self.navhtml)
        self.processthread.pagelimit = 2
        self.processthread.storeThreads(AsuntoFactory(mockweb))

        self.assertEquals(4, len(self.mongo.listofthreads))

    def test_generate_new_factory(self):
        oldpage = AsuntoFactory( MockWebClient(self.navhtml))
        page = self.processthread._nextPage(oldpage)

        self.assertEquals(u"http://labsk.net/index.php?board=18.20", page.webclient.url)



class TestProcessThreads(unittest.TestCase):

    def setUp(self):
        self. processthread = ProcessThread()
        self.t01 = ThreadModel(Reports.threats_with_newline.copy())
        self.t02 = ThreadModel(Reports.threats_with_newline.copy())


    def test_set_the_limit_for_process_msg(self):
        #self.processthread.setMsgPageLimit(4)

        self. processthread.msgpagelimit = 4
        process = self. processthread._createProcessMsgs()
        self.assertEqual(process.pagelimit, 4)

    # Pocess Thread
    def test_createThreadStruct(self):
        mockweb = MockWebClient(HTMLFactory.tablamensajes_html())
        self.threadfactory = AsuntoFactory(mockweb)
        self.assertEquals("", self.threadfactory.nextUrl())
        thread = self.threadfactory.create(HTMLFactory.asunto())
        msgs = list()
        struct = ThreadModel(self. processthread._createThreadStruct(thread, msgs))

        self.assertEquals("LaBSK", struct.source())
        self.assertEquals(thread['title'], struct.title())
        self.assertEquals(struct.answers(), 0)
        self.assertIsInstance(struct.json()['msgs'], list)

    def test_when_thread_is_new_then_store_it(self):
        self.processthread.database = mock()
        self.processthread.processmsgfactory = mock()
        page = mock()
        when(page).createListOfMsgs().thenReturn(list())
        when(self.processthread.processmsgfactory).create(any()).thenReturn(page)
        thread = mock()

        self.processthread._evaluate_thread(thread)

        verify(self.processthread.database, times=1).saveThread(any())

    def test_hilo_modificado_iguales(self):
        self.assertTrue(self.processthread._hilo_modificado(self.t01, self.t02))

    def test_hilo_modificado_diferente_fecha(self):
        self.t01.set_date("Yes")
        self.t02.set_date("No")
        self.assertFalse(self.processthread._hilo_modificado(self.t01, self.t02))

    def test_hilo_modificado_misma_fecha(self):
        self.t01.set_date("Yes")
        self.t02.set_date("Yes")
        self.assertTrue(self.processthread._hilo_modificado(self.t01, self.t02))

    def test_hilo_modificado_diferentes_mensajes(self):
        self.t01.set_answers(10)
        self.t02.set_answers(20)
        self.assertFalse(self.processthread._hilo_modificado(self.t01, self.t02))

    def test_hilo_modificado_misma_mensajes(self):
        self.t01.set_answers(10)
        self.t02.set_answers(10)
        self.assertTrue(self.processthread._hilo_modificado(self.t01, self.t02))


class TestProcessMsgs(unittest.TestCase):

    def setUp(self):
      self.process = ProcessMsgs()

    def test_createMsg(self):
        mockweb = MockWebClient(HTMLFactory.msg_html())
        self.msgfactory = MsgFactory(mockweb)
        self.assertEquals(2, len(self.msgfactory.createListOfMsgs()))

        msgs = self.process.getMsgs(self.msgfactory)

        self.assertEquals(2, len(msgs))

    def test_default_pagelimit_is_1(self):
        html = HTMLFactory.msg_html() +  HTMLFactory.navigation_url()
        mockweb = MockWebClient(html)

        msgs = self.process.getMsgs(MsgFactory(mockweb))

        self.assertEquals(2, len(msgs))

    def test_lopp_2(self):
        html = HTMLFactory.msg_html() +  HTMLFactory.navigation_url()
        mockweb = MockWebClient(html)
        self.process.pagelimit = 2
        msgs = self.process.getMsgs(MsgFactory(mockweb))

        self.assertEquals(4, len(msgs))


if __name__ == '__main__':
    unittest.main()
