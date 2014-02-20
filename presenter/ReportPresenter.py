__author__ = 'Javier'

from LaBSKApi.reports import ReportBuilder, PreGeneratedReports
from GUIModel import Text

class ReportPresenter(object):
    def __init__(self):
        self.db = None

    def generateReport(self, reportDescription):
        assert self.db is not None
        informeBuilder = ReportBuilder(self.db)
        report = informeBuilder.build_report(reportDescription)
        return report

    # Untested method
    def generatePreReport_AsylumGames(self):
        """ Generates the predefined report for the editorial aSylm Games
        Predefines report is declared in repowts module"
        return a text object
        """
        assert self.db is not None
        informeBuilder = ReportBuilder(self.db)
        report = informeBuilder.build_report(PreGeneratedReports.report_asylum_games)
        return self._toGUIMode(report, PreGeneratedReports.report_asylum_games)


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