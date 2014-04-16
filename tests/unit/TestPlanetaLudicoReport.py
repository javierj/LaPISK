from LaBSKApi.reportstats import ReportStats

__author__ = 'Javier'

import unittest
from LaBSKApi.PlanetaLudico import PlanetaLudicoReport, BlogEntry
from LaBSKApi.modelobjects import ReportEntriesModel
from tests.Harness import MockKimonoPlanetaLudicoAPI
from mockito import mock, when
from datetime import datetime


class TestBlogEntry(unittest.TestCase):

    def test_create_BlogEntry(self):
        result = BlogEntry("xx")
        self.assertEqual(result.json(), "xx")

    def test_year(self):
        entry = BlogEntry({'date':'23 Noviembre, 2012'})
        self.assertEqual(entry.year(), 2012)
        entry = BlogEntry({'date':'3 Noviembre, 2012'})
        self.assertEqual(entry.year(), 2012)

    def test_date_as_datetime(self):
        entry = BlogEntry({'date':'23 Noviembre, 2012'})
        self.assertEqual(entry.date_as_datetime(), datetime(2012, 11, 23))
        entry = BlogEntry({'date':'2 Noviembre, 2012'})
        self.assertEqual(entry.date_as_datetime(), datetime(2012, 11, 2))


class TestPlanetaLudicoReport(unittest.TestCase):

    madeira_report = MockKimonoPlanetaLudicoAPI.report_json

    def setUp(self):
        self.report = ReportEntriesModel()
        self.stats = ReportStats()
        self.plr = PlanetaLudicoReport()
        self.madeira_request = {'name': 'Planeta Ludico demo',
                                'keywords': ["madeira"]}
        self.rb = mock()
        when(self.rb).build_report(self.madeira_request).thenReturn(TestPlanetaLudicoReport.madeira_report)

        self.plr._report_builder = self.rb

    def test_when_no_entries_report_and_stats_remains_unmodified(self):
        when(self.rb).build_report(self.madeira_request).thenReturn({'madeira': []})

        self.plr.build_report(self.madeira_request, self.report, self.stats)
        self.assertEqual(self.report.size(), 0)
        self.assertEqual(str(self.stats), "0, 0, 0")

    def test_when_two_entries_are_found_return_entries(self):
        self.plr.build_report(self.madeira_request, self.report, self.stats)
        self.assertEqual(self.report.count_entries_in('madeira'), 2)

    def test_when_two_entries_are_found_blog_stats_are_incremented(self):
        self.plr.build_report(self.madeira_request, self.report, self.stats)
        self.assertEqual(str(self.stats), "0, 0, 2")

    def test_all_objects_from_report_are_from_class_(self):
        self.plr.build_report(self.madeira_request, self.report, self.stats)
        for object in self.report.entries_in('madeira'):
            self.assertIsInstance(object, BlogEntry)

    def test_creation_date(self):
        self.plr.build_report(self.madeira_request, self.report, self.stats)
        json = self.report.entries_in('madeira')[0].json()
        date = json['creation_date']
        print json
        self.assertEqual(date, "21 marzo, 2014")

if __name__ == '__main__':
    unittest.main()
