__author__ = 'Javier'

from LaBSKApi.reports import ReportBuilder
from LaBSKApi.modelobjects import ReportQueryModel, ThreadModel, ReportModel
from GUIModel import Text


class ReportPresenter(object):
    def __init__(self):
        self.db = None
        self.builder = None

    def set_builder(self, builder):
        self.builder = builder

    def _get_builder(self):
        if self.builder == None:
            self.builder = ReportBuilder(self.db)
        return self.builder

    def report_and_stats(self, reportDescription, data_filter=None):
        """ Retrurns an object with the result of the query incuding
        the generated report and starts woth the reuslts
        """
        rr = ReportResult()
        rr.report = self.generateReport(reportDescription, data_filter)
        rr.report_stats = self.generateStats(reportDescription, rr.report)
        return rr

    def generateReport(self, reportDescription, data_filter = None):
        #assert self.db is not None
        informeBuilder = self._get_builder()
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

    def generateStats(self, reportDescription, report_json):
        threads = 0
        msgs = 0
        report_obj = ReportModel(report_json)
        for key in reportDescription['keywords']:
            for thread_obj in report_obj.threads_in(key):
                threads += 1
                print thread_obj.msg_count()
                msgs += thread_obj.msg_count()

        result = Text(u"Asuntos encontrados: " + str(threads))
        result.addText(u"Mensajes encontrados: " + str(msgs))
        return result

    @property
    def database(self):
        return self.db

    @database.setter
    def database(self, value):
        self.db = value


class ReportResult(object):

    def __init__(self):
        self.thereport = None
        self.stat = None

    @property
    def report(self):
        return self.thereport

    @report.setter
    def report(self, value):
        self.thereport = value

    @property
    def report_stats(self):
        return self.stat

    @report_stats.setter
    def report_stats(self, value):
        self.stat = value
