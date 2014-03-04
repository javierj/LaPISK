"""
Test local server and opemShift
Run this test cas eonce before deployment in EopneShift and once after deployment.
"""
__author__ = 'Javier'

import unittest
import urllib2


class TestLocalFlaskWeb(unittest.TestCase):
    """ This tets suite tests the server running in localhost
        If server it is not online, this test will fail.

        Run this test before uploading the app to Openshift
    """

    def setUp(self):
        self.url = "http://127.0.0.1:5000"

    def test_LoadReportAsylumGame(self):
        web = urllib2.urlopen(self.url + "/reports/asylum-games")
        self.assertEqual(web.code, 200)
        #print web

    def test_Load_main_page(self):
        web = urllib2.urlopen(self.url)
        self.assertEqual(web.code, 200)
        #print web

    def test_Load_stats_page(self):
        web = urllib2.urlopen(self.url + "/stats")
        self.assertEqual(web.code, 200)
        #print web


class TestOpenShiftFlaskWeb(TestLocalFlaskWeb):
    """ Test the openshift deployment
    """
    def setUp(self):
        self.url = "http://phorumledge-hootboardgame.rhcloud.com"


if __name__ == '__main__':
    #TestLocalFlaskWeb.url = "http://127.0.0.1:5000" -- no.
    unittest.main()
