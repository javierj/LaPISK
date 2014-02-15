__author__ = 'Javier'

from LaBSKApi.reports import ReportBuilder

class ReportPresenter(object):
    def __init__(self):
        self.db = None

    def generateReport(self, reportDescription):
        assert self.db is not None
        informeBuilder = ReportBuilder(self.db)
        report = informeBuilder.build_report(reportDescription)
        return report

    @property
    def database(self):
        return self.db

    @database.setter
    def database(self, value):
        self.db = value