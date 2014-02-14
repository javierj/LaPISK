__author__ = 'Javier'

import unittest
from Harness import MockMongo
from LaBSKApi.reports import ReportBuilder

class TestReportBuilder(unittest.TestCase):

    def setUp(self):
        self.builder = ReportBuilder(MockMongo())

    def test_when_report_has_no_keywords_launch_exception(self):
        emptyReport = dict()
        try:
            self.builder.build_report(emptyReport)
        except ValueError:
            return
        self.fail("No exception ValueError")



if __name__ == '__main__':
    unittest.main()
