__author__ = 'Javier'

import unittest
from LaBSKApi.MongoDB import MongoDB
from datetime import datetime
from LaBSKApi.Process import ProcessThread
from tests.Harness import Reports
from LaBSKApi.modelobjects import ThreadModel
from mockito import mock, verify


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.obj_thread = ThreadModel(Reports.get_asylum_thread())
        self.obj_thread.set_answers(59)
        self.mock_listener = mock()
        self.db = MongoDB()
        self.db.query("labsk_merge")


    def test_skip_thread(self):
        self.db.query("labsk_merge")
        tmp_col = "labsk_temp_temp"
        self.db.insert(tmp_col)

        process = self._create_process()

        process._evaluate_thread(self.obj_thread)

        self.assertEqual(0, self.db.len("labsk_temp_temp"))

        self.db.drop(tmp_col)

    def test_search_thread(self):
        db = MongoDB()
        db.query("labsk_merge")
        tmp_col = "labsk_temp_temp"
        db.insert(tmp_col)

        process = ProcessThread()
        process.database = db

        result = process._search_thread(self.obj_thread)

        self.assertIsNotNone(result)

        db.drop(tmp_col)


    def test__is_unmodified(self):

        self.db.query("labsk_merge")
        tmp_col = "labsk_temp_temp"
        self.db.insert(tmp_col)

        process = self._create_process()
        result = process._search_thread(self.obj_thread)

        bol = process._is_unmodified(self.obj_thread , result)

        print self.obj_thread.answers(), ", ", result.answers()

        self.assertTrue(bol)

        db.drop(tmp_col)

    def test_thread_is_unmodified_and_dont_read_msgs(self):
        """ Esta prueba pas ay no se por que porque el sistema falla.
        Falso positivo
        """
        link = 'http://labsk.net/index.php?topic=128630.0'
        newT = ThreadModel({'link':link, 'msgs': [{}]})

        print "Answers: ", newT.answers()
        db.query("labsk_merge")
        tmp_col = "labsk_temp_temp"
        #db.insert(tmp_col)

        process = self._create_process()
        self.assertIsNotNone(process._search_thread(newT))


        process._evaluate_thread(newT)
        verify(self.mock_listener).skippingUnmodifiedThread(newT)

    def _create_process(self):
        process = ProcessThread()
        process.database = self.db
        process.listener =  self.mock_listener
        return process

    def test_skpi_existing_thread_with_one_msg_and_0_answers(self):
        link = 'http://labsk.net/index.php?topic=127734.0'
        newT = ThreadModel({'link':link, 'msgs': [{}], 'answers':'0'})

        #print "Answers: ", newT.answers()
        tmp_col = "labsk_temp_temp"
        #db.insert(tmp_col)

        process = self._create_process()
        self.assertIsNotNone(process._search_thread(newT))
        process._evaluate_thread(newT)
        verify(self.mock_listener).skippingUnmodifiedThread(newT)

if __name__ == '__main__':
    unittest.main()
