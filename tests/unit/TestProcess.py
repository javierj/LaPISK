__author__ = 'Javier'

import unittest

from LaBSKApi.HTML2Objects import AsuntoFactory, MsgFactory
from LaBSKApi.Process import ProcessThreads, ProcessMsgs
from LaBSKApi.reports import ThreadModel
from tests.Harness import MockWebClient, HTMLFactory, MockMongo


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

    def test_createThreadStruct(self):
        self.assertEquals("", self.threadfactory.nextUrl())
        thread = self.threadfactory.create(HTMLFactory.asunto())
        msgs = list()
        struct = ThreadModel(self.processthread._createThreadStruct(thread, msgs))

        self.assertEquals("LaBSK", struct.source())
        self.assertEquals(thread['title'], struct.title())
        self.assertEquals(struct.answers(), 0)
        self.assertIsInstance(struct.json()['msgs'], list)

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

    def test_set_the_limit_for_process_msg(self):
        self.processthread.setMsgPageLimit(4)
        process = self.processthread._createProcessMsgs()
        self.assertEqual(process.pagelimit, 4)



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
