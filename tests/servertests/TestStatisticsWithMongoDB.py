__author__ = 'Javier'

import unittest
from LaBSKApi.MongoDB import MongoDB
from LaBSKApi.statistics import Statistics
from tests.Harness import MockDatetime

class TestStatsWithMondoDB(unittest.TestCase):

    def setUp(self):
        self.db = MongoDB(col = 'stats_test')
        self.stats = Statistics(self.db)
        mock = MockDatetime()
        self.expected_date = mock.now()
        self.stats._datetime = mock

    def test_save_stat(self):
        json_doc = {'url':"url", 'datetime': "2014-01-01 14:10:00" }
        self.stats.register_access_now("url")

        result = self.db.find_one_by('url', "url")
        self.assertEqual(result['url'], "url")
        self.assertEqual(result['datetime'], str(self.expected_date))

        self.db.drop('stats_test')

    def test_all_visits(self):
        self.stats.register_access_now("url")

        visits = self.stats.all_visits()

        self.assertEqual(len(visits), 1)

if __name__ == '__main__':
    unittest.main()
