__author__ = 'Javier'

import unittest
from flask import Flask
from webgui import flaskweb
from mockito import *
from presenter.ReportPresenter import ReportPresenter
from presenter.GUIModel import Text
from webgui.helppers import GenerateHTMLFromText

class TestFlaskWeb(unittest.TestCase):

    def setUp(self):
        #self.db_fd, flaskr.app.config['DATABASE'] = tempfile.mkstemp()
        flaskweb.app.config['TESTING'] = True
        self.app = flaskweb.app.test_client()
        self.baseURL = ""

    def test_report_presenter_by_default(self):
        self.assertIsInstance(flaskweb.reportPresenter, ReportPresenter)

    def test_main_page_title(self):
        rv = self.app.get('/')
        self.assertTitleIn("HootBoard", rv)

    def test_main_page_link_to_reports(self):
        rv = self.app.get('/')
        self.assertLinkIn("reports", rv)

    def test_reports_page_title(self):
        rv = self.app.get('/reports')
        self.assertTitleIn("HootBoard", rv)

    def test_when_requesting_asylum_then_report_presenter_is_called(self):
        mockReportPresenter = mock()
        flaskweb.reportPresenter = mockReportPresenter
        rv = self.app.get('/reports/asylum-games')
        verify(mockReportPresenter).generatePreReport_AsylumGames()


    #
    # New asserts
    #
    def assertTitleIn(self,title, rv):
       self.assertIn("<title>"+title+"</title>", rv.data)

    def assertLinkIn(self, link, rv):
        self.assertIn("<a href='" + self.baseURL + "/"+link+"'", rv.data)



class TestGenerateHTMLFromText(unittest.TestCase):

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


if __name__ == '__main__':
    unittest.main()
