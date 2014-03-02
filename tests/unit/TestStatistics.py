__author__ = 'Javier'

import unittest
from LaBSKApi.statistics import Statistics
from tests.Harness import create_datetime

class TestStatistics(unittest.TestCase):
    def test_store_and_rtrive_visit(self):
        stats = Statistics(None)
        fecha_acceso = create_datetime("01/01/2014", "12:00")
        stats.register_access('/', fecha_acceso)

        visits = stats.all_visits()
        self.assertEqual(len(visits), 1)
        self.assertEquals(fecha_acceso, visits[0].access_datetime())
        self.assertEqual('/', visits[0].url())


if __name__ == '__main__':
    unittest.main()
