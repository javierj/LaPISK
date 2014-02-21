__author__ = 'Javier'

import unittest
from flask import Flask
from webgui import flaskweb
from mockito import *
from presenter.ReportPresenter import ReportPresenter, ReportModel
from presenter.GUIModel import Text
from webgui.helppers import GenerateHTMLFromText
from Harness import Reports
import urllib2

class TestFlaskWeb(unittest.TestCase):

    def setUp(self):
        #self.db_fd, flaskr.app.config['DATABASE'] = tempfile.mkstemp()
        flaskweb.app.config['TESTING'] = True
        self.app = flaskweb.app.test_client()
        self.baseURL = ""
        self.title = "HootBoardGame"

    def test_report_presenter_by_default(self):
        self.app = flaskweb.app.test_client()
        self.assertIsInstance(flaskweb.reportPresenter, ReportPresenter)

    def test_main_page_title(self):
        mockReportPresenter = mock()
        flaskweb.reportPresenter = mockReportPresenter
        rv = self.app.get('/')
        self.assertTitleIn(self.title, rv)

    def test_main_page_link_to_reports(self):
        mockReportPresenter = mock()
        flaskweb.reportPresenter = mockReportPresenter
        rv = self.app.get('/')
        self.assertLinkIn("reports", rv)

    def test_reports_page_title(self):
        rv = self.app.get('/reports')
        self.assertTitleIn(self.title, rv)

    def test_when_requesting_asylum_then_report_presenter_is_called(self):
        mockReportPresenter = mock()
        jsonMock = mock()
        when(jsonMock).json().thenReturn(dict())
        when(mockReportPresenter).getReportFor_AsylumGames().thenReturn(jsonMock)
        flaskweb.reportPresenter = mockReportPresenter
        rv = self.app.get('/reports/asylum-games')
        verify(mockReportPresenter).getReportFor_AsylumGames()

    def testGenerateAsylumGamesReport_contains_keyword(self):
        rv = self.app.get('/reports/asylum-games')
        #report = ReportModel(Reports.asylum)
        for word in Reports.asylum_keywords:
            self.assertIn(word, rv.data)


    #
    # New asserts
    #
    def assertTitleIn(self,title, rv):
       self.assertIn("<title>"+title+"</title>", rv.data)

    def assertLinkIn(self, link, rv):
        self.assertIn("<a href='" + self.baseURL + "/"+link+"'", rv.data)


class TestGenerateHTMLFromText(unittest.TestCase):
    """ Class GenerateHTMLFromText is actually not in use
    """
    def testGenerateParagraphFromFirstLine(self):
        text = Text("Hola");
        create = GenerateHTMLFromText()
        result = create.html_from(text)
        self.assertEquals(result, "<p>Hola</p>")

    def testGenerateParagraphFromFirstTwoLines(self):
        text = Text("Hola");
        text.addText("Adios")
        create = GenerateHTMLFromText()
        result = create.html_from(text, 2)
        self.assertEquals(result, "<p>Hola / Adios</p>")




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
