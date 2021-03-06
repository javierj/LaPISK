__author__ = 'Javier'

from LaBSKApi.modelobjects import ReportQueryModel, ThreadModel, ReportModel
from GUIModel import Text


class ReportPresenter(object):
    def __init__(self, builder=None):
        self.builder = builder

    def set_builder(self, builder):
        self.builder = builder

    def _get_builder(self):
        return self.builder

    def report_and_stats(self, reportDescription, data_filter=None, filter_year=None):
        """ Retrurns an object with the result of the query incuding
            the generated report and starts woth the reuslts
        """
        rr = self.generateReport(reportDescription, data_filter, filter_year)
        #rr.report = self.generateReport(reportDescription, data_filter, filter_year)
        result = ReportResult()
        result.report_stats = self.generateStats(reportDescription, rr.report)
        if data_filter is not None:
            prev_year = int(data_filter) +1
            result.report_stats.addText("Se omiten mensajes desde el "+str(prev_year)+" o posteriores")
        if filter_year is not None:
            prev_year = int(filter_year) +1
            result.report_stats.addText("Se omiten asuntos sin mensajes desde el "+str(prev_year)+" o posteriores")
        result.report = rr.report
        return result

    def generateReport(self, reportDescription, data_filter = None, filter_year = None):
        informeBuilder = self._get_builder()
        report_result = informeBuilder.build_report(reportDescription)
        if data_filter is not None:
            self._filter_report_using_year(reportDescription, report_result.report, data_filter)
        if filter_year is not None:
            self._filter_threads_using_year(reportDescription, report_result.report, filter_year)
        return report_result

    # Duplicate code. For filtering use the classes in report module
    def _filter_report_using_year(self, reportDescription, report, year):
        query = ReportQueryModel(reportDescription)
        for kword in query.keywords():
            for thread in report[kword]:
                threadobj = ThreadModel(thread)
                new_msgs = self._filer_msgs_in(threadobj, year)
                threadobj.replace_msgs_objs(new_msgs)

    def _filer_msgs_in(self, threadobj, year):
        msgs = []
        year_int = int(year)
        for msgobj in threadobj.msgs_objs():
            if msgobj.year() > year_int:
                #print "Bigger"
                msgs.append(msgobj)
        return msgs

    def _filter_threads_using_year(self, reportDescription, report, year):
        """ Previous method filter messages of a thread.
            this method filters therads in a report.
            Don't word modifyng directy the report so I retorn the JSon again
        """
        year_int = int(year)
        query = ReportQueryModel(reportDescription)
        report_obj = ReportModel(report)
        for kword in query.keywords():
            threats = list()
            for threadobj in report_obj.threads_in(kword):
                #print kword, ":", threadobj.year_last_msg(), ", ", year_int, threadobj.link()
                if threadobj.year_last_msg() > year_int:
                    threats.append(threadobj.json())
            report_obj.set_threads_to(kword, threats)
        return report_obj.json()

    def _toGUIMode(self, report, keywords):
        """ Unused by now.
        Translates a report from model domain to GUI domain
        """
        result = Text(report['title'])
        for keyword in keywords:
            result.addNextText(Text(keyword))
        return result

    # Duplicate code. Report services return stats.
    def generateStats(self, reportDescription, report_json):
        threads = 0
        msgs = 0
        report_obj = ReportModel(report_json)
        for key in reportDescription['keywords']:
            for thread_obj in report_obj.threads_in(key):
                threads += 1
                msgs += thread_obj.msg_count()

        result = Text(u"Asuntos encontrados: " + str(threads))
        result.addText(u"Mensajes encontrados: " + str(msgs))
        return result


class ReportResult(object):

    def __init__(self, report=None, stats=None):
        self.thereport = report
        self.stat = stats

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


class ReportBuilderPresenter(object):

    def __init__(self, builder=None):
        """ Builder should have the filters setted """
        self.builder = builder

    def set_builder(self, builder):
        self.builder = builder

    def _get_builder(self):
        return self.builder

    def report_and_stats(self, reportDescription):
        """ Retrurns an object with the result of the query incuding
            the generated report and starts woth the reuslts
        """
        rr = self.generateReport(reportDescription)
        #rr.report = self.generateReport(reportDescription, data_filter, filter_year)
        result = ReportResult()
        result.report_stats = self.generateStats(reportDescription, rr.report)
        result.report_stats.addText(self.builder.descriptions_from_filters())
        result.report = rr.report
        return result

    def generateReport(self, reportDescription):
        informeBuilder = self._get_builder()
        report_result = informeBuilder.build_report(reportDescription)
        return report_result

    def _toGUIMode(self, report, keywords):
        """ Unused by now.
        Translates a report from model domain to GUI domain
        """
        result = Text(report['title'])
        for keyword in keywords:
            result.addNextText(Text(keyword))
        return result

    # Untested
    def generateStats(self, reportDescription, report_json):
        count = 0
        report_obj = ReportModel(report_json)
        for key in reportDescription['keywords']:
            count += report_obj.count_entries_in(key)

        result = Text(u"Resultados encontrados: " + str(count))
        #result.addText(u"Mensajes encontrados: " + str(msgs))
        return result
