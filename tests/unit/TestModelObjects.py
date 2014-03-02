__author__ = 'Javier'

import unittest
from LaBSKApi.modelobjects import ReportModel, ThreadModel, MsgListModel
from tests.Harness import Reports


class TestReportModel(unittest.TestCase):

    def test_json_is_the_same_that_creation(self):
        rm = ReportModel(Reports.asylum)
        self.assertEqual(Reports.asylum, rm.json())

    def test_get_keyword(self):
        expected = ['Asylum Games', 'Banjooli', 'Mutinies', 'Polis']
        rm = ReportModel(Reports.asylum)
        keywords = rm.getKeywords()
        print keywords
        self.assertEqual(len(expected), len(keywords))
        self.assertEqual(expected, keywords)

    """ Use Text class instead
    def test_replace_newline(self):
        rm = ReportModel(Reports.asylum)
        rm.replaceNewLineWith("<br/>")
        thread = rm.firstthread("Banjooli")
        msg = thread.firstmsg()

        self.assertIn("<br/>", msg.body())
        self.assertNotIn("\n", msg.body())
    """


class TestMsgListModel(unittest.TestCase):

    def setUp(self):
        self.pre = self.assertTrue
        self.threat = Reports.get_asylum_thread()
        self.msglist = MsgListModel(self.threat['msgs'])

    def test_json(self):
        self.assertEqual(self.threat['msgs'], self.msglist.json())

    """ - Use Text class instead
    def test_replace_newline(self):
        #self.pre("\n" in Reports.asylum_threat['msgs'])
        #self.pre("<br/>" not in Reports.asylum_threat['msgs'])
        self.msglist.replaceNewLineWith("<br/>")
        msg = self.msglist.getMsg(0)['body']
        self.assertIn("<br/>", msg)
        self.assertNotIn("\n", msg)
    """

    def test_append_one_msg(self):
        self.pre(self.msglist.size() == 1)
        self.msglist.append_msg(dict())
        self.assertTrue(self.msglist.size() == 2)


class TestThreadModel(unittest.TestCase):

    def setUp(self):
        self.empty_thread = ThreadModel({"msgs": [{}]})
        self.thread = ThreadModel(Reports.threats_with_newline.copy())

    def test_date(self):
        self.assertIsNone(self.empty_thread.date())
        self.empty_thread.set_date("X")
        self.assertEqual("X",  self.empty_thread.date())

    def test_get_id_last_msg(self):
        _id = self.thread.id_last_msg()
        self.assertEqual(_id, "msg_1169262")

    def test_get_id_last_msg_return_null_if_not_id(self):
        result_id = self.empty_thread.id_last_msg()
        self.assertIsNone(result_id)

    """ - Metodo incompleto
    def test_update_msg(self):
        thread = ThreadModel(Reports.threats_with_newline)
        newmsg = [{"body": "xxx"}]
        thread.update_msgs(newmsg)
        self.assertEqual(2, thread.msgList().size())
    """

    def test_date_last_msg(self):
        self.assertEqual(u' 24 de Octubre de 2013, 08:22:36 am \xbb', self.thread.date_last_msg())

    def test_when_thread_has_no_answers_return_num_of_msg(self):
        thread = ThreadModel({'msgs': [{}, {}]})
        self.assertEqual(2, thread.answers())

if __name__ == '__main__':
    unittest.main()