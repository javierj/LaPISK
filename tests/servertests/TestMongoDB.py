__author__ = 'Javier'

import unittest

from LaBSKApi.MongoDB import MongoDB

class  TestMongoDB(unittest.TestCase):

    def setUp(self):
        self.db = MongoDB()
        self.testcol = self.db.collection("labsk_test")

    def test_merge_same_collection_zero_docs_merged(self):
        db = self.db

        col2 = db.collection("labsk_test")

        self.assertEqual(60, db.len(self.testcol))
        self.assertEqual(60, db.len(col2))

        merged = db.merge(self.testcol, col2, 'link')

        self.assertEqual(0, merged)
        self.assertEqual(60, db.len(self.testcol))
        self.assertEqual(60, db.len(col2))

    def test_merge_with_empty_collection_all_docs_merged(self):
        db = self.db
        col2 = db.collection("labsk_drop_me")

        self.assertEqual(60, db.len(self.testcol))
        self.assertEqual(0, db.len(col2))

        merged = db.merge(self.testcol, col2, 'link')

        self.assertEqual(60, merged)
        self.assertEqual(60, db.len(self.testcol))
        self.assertEqual(60, db.len(col2))
        db.drop(col2)


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


if __name__ == '__main__':
    unittest.main()
