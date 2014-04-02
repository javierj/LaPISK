__author__ = 'Javier'

import unittest
from tests.Harness import Reports
from LaBSKApi.PlanetaLudico import PlanetaLudicoReport
from LaBSKApi.reports import ReportStats


class TestPlanetaLudicoReport(unittest.TestCase):

    def test_when_no_enties_report_and_stats_remains_unmodified(self):
        report = {}
        stats = ReportStats()
        plr = PlanetaLudicoReport()
        plr.build_report(Reports.asylum_report_request, report, stats)
        self.assertEqual(report, {})
        self.assertEqual(str(stats), "0, 0, 0")



if __name__ == '__main__':
    unittest.main()
