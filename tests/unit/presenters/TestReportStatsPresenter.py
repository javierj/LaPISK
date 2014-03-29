__author__ = 'Javier'

import unittest

from presenter.ReportStatsPresenter import ReportStatsPresenter
from LaBSKApi.reportstats import ReportStatsModel, ReportStatModel
from presenter.GUIModel import Table
from tests.Harness import Reports
from mockito import mock, when, verify


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.service = mock()
        self.presenter = ReportStatsPresenter(self.service)
        self.reportstats_object = ReportStatsModel(Reports.report_stat_json)
        when(self.service).reportStatsFrorReport("X").thenReturn(self.reportstats_object)

    def test_when_requesting_stats_return_a_table(self):
        result = self.presenter.stats_from_report("X")
        self.assertIsInstance(result, Table)

    def test_creaying_titles(self):
        result = self.presenter.stats_from_report("X")
        self.assertEqual(result.titles, ["Fecha", "Mensajes", "Incremento", "Asuntos", "Incremento", "Entradas de blog", "Incremento"])

    def test_creaying_one_row_for_each_day(self):
        result = self.presenter.stats_from_report("X")
        self.assertEqual(5, len(result.rows))

    def test_stat_as_text(self):
        stat_obj = ReportStatModel(Reports.report_stat_json['stats'][0])
        result = self.presenter._stat_as_text(stat_obj)
        self.assertEqual(result, ["2014-3-22","0","0","0","0","0","0"])

    def test_calculate_increment(self):
        yesterday = ["2014-3-22","0","0","0","0","0","0"]
        today = ["2014-3-22","1","0","2","0","3","0"]
        self.presenter._calculate_increments(yesterday, today)
        self.assertEqual(today, ["2014-3-22","1","1","2","2","3","3"])



if __name__ == '__main__':
    unittest.main()
