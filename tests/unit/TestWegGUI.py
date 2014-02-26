__author__ = 'Javier'

import unittest
from webgui import flaskweb
from mockito import *
from presenter.ReportPresenter import ReportPresenter
from LaBSKApi.modelobjects import ReportModel
from presenter.GUIModel import Text
from webgui.helppers import GenerateHTMLFromText
from tests.Harness import Reports


class TestFlaskWeb(unittest.TestCase):

    def setUp(self):
        #self.db_fd, flaskr.app.config['DATABASE'] = tempfile.mkstemp()
        flaskweb.app.config['TESTING'] = True
        self.app = flaskweb.app.test_client()
        self.baseURL = ""
        self.title = "HootBoardGame"
    """
    def test_report_presenter_by_default(self):
        self.app = flaskweb.app.test_client()
        self.assertIsInstance(flaskweb.reportPresenter, ReportPresenter)
    """
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
        rv = self.app.get('/reports/dynamic-asylum-games')
        verify(mockReportPresenter).getReportFor_AsylumGames()

    def testGenerateAsylumGamesReport_contains_keyword(self):
        mockReportPresenter = mock()
        jsonMock = mock()
        when(jsonMock).json().thenReturn(dict())
        when(mockReportPresenter).getReportFor_AsylumGames().thenReturn(jsonMock)
        flaskweb.reportPresenter = mockReportPresenter
        rv = self.app.get('/reports/dynamic-asylum-games')
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


class TestWebNavigation(unittest.TestCase):
    def setUp(self):
        #self.db_fd, flaskr.app.config['DATABASE'] = tempfile.mkstemp()
        flaskweb.app.config['TESTING'] = True
        self.app = flaskweb.app.test_client()
        self.baseURL = ""
        self.title = "HootBoardGame"

    def test_report_page_links_to_static_asylum_report(self):
        rv = self.app.get('/reports')
        self.assertLinkIn("reports/asylum-games", rv)

    def test_report_page_links_to_static_devir_report(self):
        rv = self.app.get('/reports')
        self.assertLinkIn("reports/devir", rv)

    def assertLinkIn(self, link, rv):
        self.assertIn("<a href='" + self.baseURL + "/"+link+"'", rv.data)



class TestStaticReports(unittest.TestCase):
    def setUp(self):
        #self.db_fd, flaskr.app.config['DATABASE'] = tempfile.mkstemp()
        flaskweb.app.config['TESTING'] = True
        self.app = flaskweb.app.test_client()
        self.baseURL = ""
        self.title = "HootBoardGame"

    def test_asylum_report_contains_keywords(self):
        rv = self.app.get('/reports/asylum-games')
        for word in Reports.asylum_keywords:
            self.assertIn(word, rv.data)


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






if __name__ == '__main__':
    unittest.main()
