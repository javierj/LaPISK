__author__ = 'Javier'

import unittest
from LaBSKApi.statistics import Statistics, Visit
from tests.Harness import MockDatetime, MockMongo
import datetime

class TestStatistics(unittest.TestCase):

    def setUp(self):
        self.mock_date = MockDatetime()
        self.mock_date.set_datetime("01/01/2014", "12:00")
        self.stats = Statistics(MockMongo())
        self.stats._datetime = self.mock_date

    def test_by_default_statistics_uses_a_datetime(self):
        stats = Statistics(None)
        self.assertIs(stats._datetime, datetime.datetime)

    def test_store_and_retrive_visit(self):
        self.stats.register_access_now('/')

        visits = self.stats.all_visits()
        self.assertEqual(len(visits), 1)
        self.assertEquals(str(self.mock_date.dt), visits[0].access_datetime)
        self.assertEqual('/', visits[0].url)


class TestVisit(unittest.TestCase):

    def test_to_json(self):
        json_doc = {'url':"/", 'datetime': "2014/02/02 14:53" }
        visit = Visit("/", "2014/02/02 14:53")

        self.assertEqual(visit.json(), json_doc)


if __name__ == '__main__':
    unittest.main()
