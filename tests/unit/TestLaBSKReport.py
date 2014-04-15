from LaBSKApi.reportstats import ReportStats

__author__ = 'Javier'

import unittest
from mockito import mock, when
from tests.Harness import Reports
from LaBSKApi.modelobjects import ThreadModel, ReportModel, ReportEntriesModel
from LaBSKApi.LaBSK import LaBSKReportBuilder


class TestLaBSKReport(unittest.TestCase):

    def setUp(self):
        #self.report = ReportModel({'Asylum Games':[], 'Banjooli':[], 'Mutinies':[], 'Polis':[]})
        self.report = ReportEntriesModel()
        self.stats = ReportStats()

    def test_all_objects_from_report_are_from_class_(self):
        rb = mock()
        when(rb).build_report(Reports.asylum_report_request).thenReturn(Reports.asylum)
        l_report = LaBSKReportBuilder(rb)
        l_report.build_report(Reports.asylum_report_request, self.report, self.stats)
        #print report
        self.assertGreater(self.report.count_entries_in('Polis'), 0)
        for object in self.report.entries_in('Polis'):
            self.assertIsInstance(object, ThreadModel)

    def test_inc_stats_right(self):
        rb = mock()
        when(rb).build_report(Reports.asylum_report_request).thenReturn(Reports.asylum)
        l_report = LaBSKReportBuilder(rb)
        self.stats.inc_threads()
        self.stats.inc_msgs(2)
        l_report.build_report(Reports.asylum_report_request, self.report, self.stats)
        #print report.json()['Polis']

        thread = ThreadModel(Reports.asylum['Polis'][0])
        self.assertEqual(5, thread.msg_count())
        thread = ThreadModel(Reports.asylum['Asylum Games'][0])
        self.assertEqual(1, thread.msg_count())
        thread = ThreadModel(Reports.asylum['Banjooli'][0])
        self.assertEqual(1, thread.msg_count())

        self.assertEquals(10, self.stats._msgs)
        self.assertEquals(self.stats._threads, 5)