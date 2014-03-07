__author__ = 'Javier'

import unittest
from LaBSKApi.statistics import Statistics, Visit
from tests.Harness import MockDatetime, MockMongo
import datetime
from mockito import mock, when

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
        self.stats.register_access_now('/', "0.0.0.0")

        visits = self.stats.all_visits()
        self.assertEqual(len(visits), 1)
        self.assertEquals(str(self.mock_date.dt), visits[0].access_datetime)
        self.assertEqual('/', visits[0].url)

    def test_all_visits_with_statis_without_ip(self):
        db = mock()
        when(db).find_all().thenReturn([{'url':"/", 'datetime': "2014/02/02 14:53"}])
        stats = Statistics(db)

        visits = stats.all_visits()
        self.assertEqual(len(visits), 1)
        self.assertEquals("2014/02/02 14:53", visits[0].access_datetime)
        self.assertEqual('/', visits[0].url)

    def test_when_a_visit_comes_from_a_ignore_ip_dont_store_it(self):
        self.stats.add_ignore_ip('ignore')
        self.stats.register_access_now("url", "ignore")

        visits = self.stats.all_visits()
        self.assertEqual(len(visits), 0)


    def test_when_a_visit_comes_from_one_of_ignore_ips_dont_store_it(self):
        self.stats.add_ignore_ip('ignore01')
        self.stats.add_ignore_ip('ignore02')
        self.stats.register_access_now("ignore01", "ignore01")
        self.stats.register_access_now("ignore02", "ignore02")
        self.stats.register_access_now("no_ignore", "no_ignore")

        visits = self.stats.all_visits()
        self.assertEqual(len(visits), 1)
        self.assertEqual(visits[0].url, "no_ignore")


class TestVisit(unittest.TestCase):

    def test_to_json(self):
        json_doc = {'url':"/", 'datetime': "2014/02/02 14:53", 'ip': "0.0.0.0" }
        visit = Visit("/", "2014/02/02 14:53", "0.0.0.0")

        self.assertEqual(visit.json(), json_doc)


if __name__ == '__main__':
    unittest.main()
