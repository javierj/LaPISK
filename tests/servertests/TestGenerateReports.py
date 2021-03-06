__author__ = 'Javier'

import unittest
from LaBSKApi.reports import ReportService, PreGeneratedReports
from LaBSKApi.MongoDB import MongoDB
from presenter.ReportPresenter import ReportPresenter


class TestGenerateReports(unittest.TestCase):

    def setUp(self):
        self.report = ReportService(MongoDB(col="labsk_merge"))
        self.presenter = ReportPresenter()
        self.presenter.set_builder(self.report)

    def test_find_zacatrus_thread_in_report(self):
        result = self.report.build_report(PreGeneratedReports. tienda_zacatrus)
        found = False
        #print "X"
        for thread in result.report["zacatrus"]:
            if thread['link'] == "http://labsk.net/index.php?topic=129533.0":
                found = True
                break
        self.assertTrue(found)

    def test_find_zacatrus_with_presenter(self):
        result = self.presenter.report_and_stats(PreGeneratedReports.tienda_zacatrus)
        found = False
        #print "X"
        for thread in result.report["zacatrus"]:
            if thread['link'] == "http://labsk.net/index.php?topic=129533.0":
                found = True
                break
        self.assertTrue(found)

    def test_find_finplay_thread_in_report(self):
        result = self.report.build_report(PreGeneratedReports.tienda_finplay)
        found = False
        #print "X"
        for thread in result.report["finplay"]:
            if thread['link'] == "http://labsk.net/index.php?topic=121033.0":
                found = True
                break
        self.assertTrue(found)

    def test_find_finplay_with_presenter(self):
        result = self.presenter.report_and_stats(PreGeneratedReports.tienda_finplay)
        found = False
        #print "X"
        for thread in result.report["finplay"]:
            if thread['link'] == "http://labsk.net/index.php?topic=121033.0":
                found = True
                break
        self.assertTrue(found)

    def test_find_finplay_with_presenter_filtering_2013(self):
        result = self.presenter.report_and_stats(PreGeneratedReports.tienda_finplay, filter_year='2013')
        found = False
        #print "X"
        for thread in result.report["finplay"]:
            if thread['link'] == "http://labsk.net/index.php?topic=121033.0":
                found = True
                break
        self.assertTrue(found)

    """
    def test_reports_for_hootboardgame(self):
        result = self.presenter.report_and_stats(PreGeneratedReports.report_hootboardgame)
        stats = result.report_stats
        print result.report_stats
        self.assertEqual(1, stats._threads)
        self.assertEquals(stats.json()['threads'], "1")
    """

if __name__ == '__main__':
    unittest.main()
