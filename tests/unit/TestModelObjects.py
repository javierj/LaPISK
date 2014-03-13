__author__ = 'Javier'

import unittest
from LaBSKApi.modelobjects import ReportModel, ThreadModel, MsgListModel, MsgModel
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

    def test_append_one_msg(self):
        self.pre(self.msglist.size() == 1)
        self.msglist.append_msg(dict())
        self.assertTrue(self.msglist.size() == 2)


class TestThreadModel(unittest.TestCase):

    def setUp(self):
        self.empty_thread = ThreadModel({"msgs": [{}], 'answers': '0'})
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

    def test_date_last_msg(self):
        self.assertEqual(u' 24 de Octubre de 2013, 08:22:36 am \xbb', self.thread.date_last_msg())

    def test_when_thread_has_no_answers_return_num_of_msg_minus_one(self):
        """ LaBSK doe snot count the first msg
        """
        thread = ThreadModel({'msgs': [{}, {}]})
        self.assertEqual(1, thread.answers())

        thread = ThreadModel({'msgs': []})
        self.assertEqual(-1, thread.answers())

        thread = ThreadModel({'msgs': [{u'date': u' 18 de Septiembre de 2013, 05:19:46 pm \xbb', u'body': u'Dejo por aqu\xed varios enlaces a nuestros \xfaltimos programas.\xa0 Hemos dejado de ser programa de radio de momento (espero que despu\xe9s de las fiestas del Pilar volvamos a serlo) as\xed que el sonido no es muy bueno, pero creo que las entrevistas son muy interesantes porque los invitados lo son\xa0 Proyecto de revista de juegos de mesa en papel y otros temas:Pedro Soto y otros temas:', u'user': u'verarua'}]})
        self.assertEqual(0, thread.answers())

    def test_answers_is_numer(self):
        #print type(self.thread.answers())
        self.assertIsInstance(self.thread.answers(), int)


class TestMsgModel(unittest.TestCase):

    def setUp(self):
        self.empty_thread = ThreadModel({"msgs": [{}], 'answers': '0'})
        self.thread = ThreadModel(Reports.threats_with_newline.copy())

    def test_when_msg_has_no_datetime_return_none(self):
        msg = {}
        msg_obj = MsgModel(msg)
        self.assertIsNone(msg_obj.datetime())

    def test_year(self):
        msg = {u'date': u' 24 de Octubre de 2013, 08:22:36 am \xbb'}
        msg_obj = MsgModel(msg)
        self.assertEquals(msg_obj.year(), 2013)


if __name__ == '__main__':
    unittest.main()
