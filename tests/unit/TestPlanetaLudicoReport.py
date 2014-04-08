from LaBSKApi.reportstats import ReportStats

__author__ = 'Javier'

import unittest
from LaBSKApi.PlanetaLudico import PlanetaLudicoReport, BlogEntry
from mockito import mock, when
from datetime import datetime


class TestBlogEntry(unittest.TestCase):

    def test_create_BlogEntry(self):
        result = BlogEntry("xx")
        self.assertEqual(result.json(), "xx")

    def test_year(self):
        entry = BlogEntry({'date':'23 Noviembre, 2012'})
        self.assertEqual(entry.year(), 2012)

    def test_date_as_datetime(self):
        entry = BlogEntry({'date':'23 Noviembre, 2012'})
        self.assertEqual(entry.date_as_datetime(), datetime(2012, 11, 23))


class TestPlanetaLudicoReport(unittest.TestCase):

    madeira_report = {'madeira': [
                        {'last_msg_date': 'No messages',
      u'title': u'The Ambassadors nueva expansi\xf3n para Madeira', 'creation_date': 'No messages',
      u'source': u'Daniel Mayoralas',
       u'link': u'http://ludonoticias.com/2014/04/02/ambassadors-nueva-expansion-para-madeira/?utm_source=rss&utm_medium=rss&utm_campaign=ambassadors-nueva-expansion-para-madeira',
       u'date': u'2 abril, 2014'},
    {'last_msg_date': 'No messages', u'title': u'Embajadores en Madeira',
     'creation_date': 'No messages', u'source': u'CUBO Magazine', u'link': u'http://cubomagazine.com/?p=13146',
     u'date': u'2 abril, 2014'}]}

    def setUp(self):
        self.report = {}
        self.stats = ReportStats()
        self.plr = PlanetaLudicoReport()
        self.report['madeira'] = []
        self.madeira_request = {'name': 'Planeta Ludico demo',
                                'keywords': ["madeira"]}
        self.rb = mock()
        when(self.rb).build_report(self.madeira_request).thenReturn(TestPlanetaLudicoReport.madeira_report)

        self.plr._report_builder = self.rb

    def test_when_no_enties_report_and_stats_remains_unmodified(self):
        when(self.rb).build_report(self.madeira_request).thenReturn(self.report)

        self.plr.build_report(self.madeira_request, self.report, self.stats)
        self.assertEqual(self.report, {'madeira': []})
        self.assertEqual(str(self.stats), "0, 0, 0")

    def test_when_two_entries_are_found_return_entries(self):
        self.plr.build_report(self.madeira_request, self.report, self.stats)
        self.assertEqual(len(self.report['madeira']), 2)

    def test_when_two_entries_are_found_blog_stats_are_incremented(self):
        self.plr.build_report(self.madeira_request, self.report, self.stats)
        self.assertEqual(str(self.stats), "0, 0, 2")

    def test_all_objects_from_report_are_from_class_(self):
        self.plr.build_report(self.madeira_request, self.report, self.stats)
        for object in self.report['madeira']:
            self.assertIsInstance(object, BlogEntry)

if __name__ == '__main__':
    unittest.main()
