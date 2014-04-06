from LaBSKApi.reportstats import ReportStats

__author__ = 'Javier'

import unittest
from mockito import mock, when
from tests.Harness import Reports
from LaBSKApi.modelobjects import ThreadModel
from LaBSKApi.reports import LaBSKReportBuilder


class TestLaBSKReport(unittest.TestCase):

    def test_all_objects_from_report_are_from_class_(self):
        rb = mock()
        when(rb).build_report(Reports.asylum_report_request).thenReturn(Reports.asylum)
        l_report = LaBSKReportBuilder(rb)
        report = {'Asylum Games':[], 'Banjooli':[], 'Mutinies':[], 'Polis':[]}
        stats = ReportStats()
        l_report.build_report(Reports.asylum_report_request, report, stats)
        print report
        self.assertGreater(len(report['Polis']), 0)
        for object in report['Polis']:
            self.assertIsInstance(object, ThreadModel)
