__author__ = 'Javier'

import unittest
from LaBSKApi.MongoDB import MongoDB
from datetime import datetime
from LaBSKApi.Process import ProcessThread
from tests.Harness import Reports
from LaBSKApi.modelobjects import ThreadModel


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.obj_thread = ThreadModel(Reports.get_asylum_thread())
        self.obj_thread.set_answers(59)

    def test_skip_thread(self):
        db = MongoDB()
        db.query("labsk_merge")
        tmp_col = "labsk_temp_temp"
        db.insert(tmp_col)

        process = ProcessThread()
        process.database = db

        process._evaluate_thread(self.obj_thread)

        self.assertEqual(0, db.len("labsk_temp_temp"))

        db.drop(tmp_col)

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
        db = MongoDB()
        db.query("labsk_merge")
        tmp_col = "labsk_temp_temp"
        db.insert(tmp_col)

        process = ProcessThread()
        process.database = db


        result = process._search_thread(self.obj_thread)

        bol = process._is_unmodified(self.obj_thread , result)

        print self.obj_thread.answers(), ", ", result.answers()

        self.assertTrue(bol)

        db.drop(tmp_col)


if __name__ == '__main__':
    unittest.main()
