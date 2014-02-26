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



if __name__ == '__main__':
    unittest.main()
