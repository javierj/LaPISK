__author__ = 'Javier'

import unittest

from LaBSKApi.MongoDB import MongoDB

class TestMongoDB(unittest.TestCase):

    def setUp(self):
        self.db = MongoDB()
        self.testcol = self.db.collection("labsk_test")

    def test_merge_with_empty_collection_all_docs_merged(self):
        db = self.db
        db.query("empty_new_col")
        db.insert("labsk_test")

        merge_result = db.merge_insert_wih_query('link')

        self.assertEqual(60, db.len("empty_new_col"))
        self.assertEqual(60, db.len("labsk_test"))
        db.drop("empty_new_col")

    def test_merge_returns_new_and_update_threads(self):
        db = self.db
        db.query("empty_new_col")
        db.insert("labsk_test")

        merge_result = db.merge_insert_wih_query('link')

        self.assertEqual(60, merge_result.new_threads)
        self.assertEqual(0, merge_result.updated_threads)
        db.drop("empty_new_col")

    def test_merge_drops_insert_column_and_avoid_its_use(self):
        db = self.db
        db.copy("labsk_test", "query_delete")
        db.copy("labsk_test", "insert_delete")
        db.query("query_delete")
        db.insert("insert_delete")

        merge_result = db.merge('link')

        self.assertIsNone(db.insert_col)
        self.assertEqual(0, db.len("insert_delete"))
        self.assertEqual(60, db.len("query_delete"))
        db.drop("query_delete")

    def test_find_all_by(self):
        results = self.db.find_one_by('link', 'http://labsk.net/index.php?topic=119300.0')
        self.assertEqual(results['link'], 'http://labsk.net/index.php?topic=119300.0')
        self.assertEqual(results['title'], u'Fief - Feudo Ediciones MasQueOca editar\xe1 Fief en Espa\xf1ol')

    def test_find_all_by_not_found(self):
        results = self.db.find_one_by('link', 'no no')
        self.assertIsNone(results)

    def test_by_default_query_and_insert_columns_are_the_column_in_constructor(self):
        db = MongoDB(col = "labsk_test")
        self.assertIs(db.col, db.query_col)
        self.assertIs(db.col, db.insert_col)

    def test_when_query_and_insert_columns_are_different_insertion_and_query_uses_diferent_cols(self):
        db = MongoDB()
        db.query("labsk_test")
        db.insert("to_delete")

        db.saveThread({'id':'1'})
        self.assertIsNone(db.find_one_by('id', '1'))

        db.query("to_delete")
        self.assertIsNotNone(db.find_one_by('id', '1'))

        db.drop("to_delete")

    def test_database_contains(self):
        self.db = MongoDB(col = "labsk_merge")
        result = self.db.find_one_by('link', "http://labsk.net/index.php?topic=129533.0")
        self.assertEqual("http://labsk.net/index.php?topic=129533.0", result['link'])


class TestCollection(unittest.TestCase):

    def setUp(self):
        self.db = MongoDB()
        self.col = self.db.collection("stats_borrame")

    def tearDown(self):
        self.db.drop("stats_borrame")

    def test_find_one_in_column(self):
        stat = {u'stats': [{u'date': u'2014-3-22', u'blogs': u'0', u'threads': u'0', u'msgs': u'0'}], u'name': u'HootBoardGame'}
        self.col.save(stat)
        self.assertIsNotNone(self.col.find_one('name', 'HootBoardGame'))

    def test_when_no_fin_returns_null(self):
        self.assertIsNone(self.col.find_one('name', 'NoExiste'))

    def test_update_stat(self):
        stat = {u'stats': [{u'date': u'2014-3-22', u'blogs': u'0', u'threads': u'0', u'msgs': u'0'}], u'name': u'HootBoardGame'}
        self.col.save(stat)
        stat['stats'].append({u'date': u'2014-3-22', u'blogs': u'0', u'threads': u'0', u'msgs': u'0'})
        self.col.remove('name', 'HootBoardGame')
        self.col.save(stat)
        new_stats = self.col.find_one('name', 'HootBoardGame')
        self.assertEqual(len(new_stats['stats']), 2)

    def test_find_one_when_col_is_empty(self):
        result = self.col.find_one('no', 'exist')
        self.assertIsNone(result)



if __name__ == '__main__':
    unittest.main()
