__author__ = 'Javier'

from tests.Harness import Reports
from LaBSKApi.reportstats import ReportStatsModel, ReportStatsService
from mockito import mock, when, verify
import unittest


class MongoDBMockFactory(object):

    def __init__(self):
        self.col = None

    # Overriding a real method
    def report_stats_collection(self):
        self.col = mock()
        return self.col


class TestReportStatsModel(unittest.TestCase):

    def setUp(self):
        self.repoststats_object = ReportStatsModel(Reports.report_stat_json)

    def test_json_is_the_same(self):
        self.assertEqual(Reports.report_stat_json, self.repoststats_object.json())

    def test_rows_macthes(self):
        first_stat = self.repoststats_object.stats[0].json()
        self.assertEqual(len(first_stat), 4)


class TestReportStatsService(unittest.TestCase):

    def setUp(self):
        mongo_mock = MongoDBMockFactory()
        self.service = ReportStatsService(mongo_mock)
        self.col_mock = mongo_mock.col
        when(self.col_mock).find_one('name', 'Report name').thenReturn({'stats':[]})

    def test_srice_returns_a_model_object(self):
        result = self.service.reportStatsFrorReport('Report name')
        self.assertIsInstance(result, ReportStatsModel)

    def test_when_requesting_stats_search_in_col_for_report_name(self):
        self.service.reportStatsFrorReport('Report name')
        verify(self.col_mock).find_one('name', "Report name")

    def test_when_requesting_stats_return_all_stats(self):
        when(self.col_mock).find_one('name', "Report name").thenReturn(Reports.report_stat_json)
        result = self.service.reportStatsFrorReport('Report name')
        self.assertEqual(result.json(), Reports.report_stat_json)

    def test_when_reportname_does_not_exists_return_a_stat_with_one_line_and_0_values(self):
        when(self.col_mock).find_one('name', "No exists").thenReturn(None)
        result = self.service.reportStatsFrorReport('No exists')
        self.assertEqual(len(result.stats), 1)
        self.assertEqual(result.stats[0].msgs(), '0')
        self.assertEqual(result.stats[0].threads(), '0')
        self.assertEqual(result.stats[0].blogs(), '0')
