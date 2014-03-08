__author__ = 'Javier'

import unittest
from LaBSKApi.MongoDB import MongoDB
from LaBSKApi.Process import ProcessThread
from tests.Harness import Reports
from LaBSKApi.modelobjects import ThreadModel
from mockito import mock, verify


class TestPorcessWithMongo(unittest.TestCase):
    """ this test suites verify tje coordination between two collections and the
        detection of an unmodified thead.
    """

    def setUp(self):
        self.obj_thread = ThreadModel(Reports.get_asylum_thread())
        self.obj_thread.set_answers(59)
        self.mock_listener = mock()
        self.db = MongoDB()
        self.db.query("labsk_merge")

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

    def _create_process(self):
        process = ProcessThread()
        process.database = self.db
        process.listener =  self.mock_listener
        return process

    def test_skip_existing_thread_with_one_msg_and_0_answers(self):
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
