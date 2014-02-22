__author__ = 'Javier'

import unittest

from LaBSKApi.MongoDB import MongoDB

class  TestMongoDB(unittest.TestCase):

    def test_merge_same_collection_zero_docs_merged(self):
        db = MongoDB()
        col1 = db.collection("labsk_test")
        col2 = db.collection("labsk_test")

        self.assertEqual(60, db.len(col1))
        self.assertEqual(60, db.len(col2))

        merged = db.merge(col1, col2, 'link')

        self.assertEqual(0, merged)
        self.assertEqual(60, db.len(col1))
        self.assertEqual(60, db.len(col2))

    def test_merge_with_empty_collection_all_docs_merged(self):
        db = MongoDB()
        col1 = db.collection("labsk_test")
        col2 = db.collection("labsk_drop_me")

        self.assertEqual(60, db.len(col1))
        self.assertEqual(0, db.len(col2))

        merged = db.merge(col1, col2, 'link')

        self.assertEqual(60, merged)
        self.assertEqual(60, db.len(col1))
        self.assertEqual(60, db.len(col2))
        db.drop(col2)


if __name__ == '__main__':
    unittest.main()
