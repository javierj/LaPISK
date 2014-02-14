__author__ = 'Javier'


class ReportBuilder(object):

    def __init__(self, db):
        self.db = db

    def build_report(self, report):
        raise ValueError("No keywords in report: " + str(report))
        #pass