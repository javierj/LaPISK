__author__ = 'Javier'

import unittest
import urllib2

class TestPintToPoint(unittest.TestCase):
    """ This tets suite tests the server on-line
        If server it is not online, this test will fail.
    """

    def test_LoadReportAsylumGame(self):
        web = urllib2.urlopen("http://127.0.0.1:5000/reports/asylum-games")
        self.assertEqual(web.code, 200)
        print web

if __name__ == '__main__':
    unittest.main()
