__author__ = 'Javier'

import unittest
from LaBSKApi.HTML2Objects import AsuntoFactory, MsgFactory
from LaBSKApi.Process import ProcessThreads, ProcessMsgs
from Harness import MockWebClient, HTMLFactory, MockMongo


class MockMsgPageFactory(object):
    def create(self, thread):
        return MsgFactory( MockWebClient(HTMLFactory.msg_html()))


class TestProcessThreads(unittest.TestCase):

    def setUp(self):
        mockweb = MockWebClient(HTMLFactory.tablamensajes_html())
        self.threadfactory = AsuntoFactory(mockweb)
        self.mongo = MockMongo()
        self.processthread = ProcessThreads(self.mongo, MockMsgPageFactory())

    def test_getlistofthreads(self):
        self.processthread.storeThreads(self.threadfactory)

        self.assertEquals(2, self.mongo.treadssaved)

    def test_createThreadStruct(self):
        thread = self.threadfactory.create(HTMLFactory.asunto())
        msgs = list()
        struct = self.processthread._createThreadStruct(thread, msgs)

        self.assertEquals("LaBSK", struct['source'])
        self.assertEquals(thread['title'], struct['title'])
        self.assertIsInstance(struct['msgs'], list)

    def test_createThreadStruct_with_msgs(self):
        self.processthread.storeThreads(self.threadfactory)

        self.assertEquals(2, len(self.mongo.listofthreads))
        thread = self.mongo.listofthreads[0]
        self.assertEqual(2, len(thread['msgs']))


class TestProcessMsgs(unittest.TestCase):

    def test_createMsg(self):
        mockweb = MockWebClient(HTMLFactory.msg_html())
        self.msgfactory = MsgFactory(mockweb)
        self.assertEquals(2, len(self.msgfactory.createListOfMsgs()))
        self.process = ProcessMsgs()
        msgs = self.process.getMsgs(self.msgfactory)

        self.assertEquals(2, len(msgs))

if __name__ == '__main__':
    unittest.main()
