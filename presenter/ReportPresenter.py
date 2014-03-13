__author__ = 'Javier'

from LaBSKApi.reports import ReportBuilder, PreGeneratedReports
from LaBSKApi.modelobjects import ReportQueryModel, ThreadModel
from GUIModel import Text

class ReportPresenter(object):
    def __init__(self):
        self.db = None

    def generateReport(self, reportDescription, data_filter = None):
        assert self.db is not None
        informeBuilder = ReportBuilder(self.db)
        report = informeBuilder.build_report(reportDescription)
        if data_filter is not None:
            self._filter_report_using_year(reportDescription, report, data_filter)
        return report

    def _filter_report_using_year(self, reportDescription, report, year):
        query = ReportQueryModel(reportDescription)
        for kword in query.getKeywords():
            for thread in report[kword]:
                threadobj = ThreadModel(thread)
                new_msgs = self._filer_msgs_in(threadobj, year)
                #if new_msgs is not None:
                threadobj.replace_msgs_objs(new_msgs)
                    #pass

    def _filer_msgs_in(self, threadobj, year):
        msgs = []
        #modified = False
        year_int = int(year)
        for msgobj in threadobj.msgs_objs():
            if msgobj.year() > year_int:
                #print "Bigger"
                msgs.append(msgobj)
                #modifed = true
        #if len(msgs) == 0:
        #    return None
        return msgs


    """
    # Untested method
    def generatePreReport_AsylumGames(self):
        report = self.generateReport(PreGeneratedReports.report_asylum_games)
        return self._toGUIMode(report, PreGeneratedReports.report_asylum_games)

    def getReportFor_AsylumGames(self):
        json = self.generateReport(PreGeneratedReports.report_asylum_games)
        return ReportModel(json)
    """

    # Unused by now.
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