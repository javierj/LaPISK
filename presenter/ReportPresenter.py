__author__ = 'Javier'

from LaBSKApi.reports import ReportBuilder, PreGeneratedReports
from LaBSKApi.modelobjects import ReportModel
from GUIModel import Text

class ReportPresenter(object):
    def __init__(self):
        self.db = None

    def generateReport(self, reportDescription, data_filter = None):
        assert self.db is not None
        informeBuilder = ReportBuilder(self.db)
        report = informeBuilder.build_report(reportDescription)
        if data_filter is not None:
            self._filter_report_using_year(report, data_filter)
        return report

    def _filter_report_using_year(self, report, year):
        pass

    """
    # Untested method
    def generatePreReport_AsylumGames(self):
        report = self.generateReport(PreGeneratedReports.report_asylum_games)
        return self._toGUIMode(report, PreGeneratedReports.report_asylum_games)

    def getReportFor_AsylumGames(self):
        json = self.generateReport(PreGeneratedReports.report_asylum_games)
        return ReportModel(json)
    """

    def _toGUIMode(self, report, keywords):
        """ Translates a report from model domain to GUI domain
        """
        result = Text(report['title'])
        for keyword in keywords:
            result.addNextText(Text(keyword))
        return result

    @property
    def database(self):
        return self.db

    @database.setter
    def database(self, value):
        self.db = value