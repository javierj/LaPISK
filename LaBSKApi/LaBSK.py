__author__ = 'Javier'

from LaBSKApi.modelobjects import ReportModel, ThreadModel
from LaBSKApi.reportstats import ReportStats

class LaBSKReportBuilder(object):
    """Cass under construction do nor use it"""

    def __init__(self, builder = None):
        self._report_builder = builder

    def build_report(self, report_request, report_obj, stats):
        """ Should return a set of thread objects.
            Este codigo tiene pinta de estar muy, muy mal.
        """

        #report_obj = ReportModel(report)

        report_result = self._report_builder.build_report(report_request)
        new_stats = ReportStats()
        for keyword in report_request['keywords']:
            for entry_json in report_result[keyword]:
                report_obj.add_entry(keyword, ThreadModel(entry_json))

        result = ReportStats()
        for key in report_request['keywords']:
            for thread_obj in report_obj.entries_in(key):
                result.inc_threads()
                result.inc_msgs( thread_obj.msg_count() )

        stats.merge(result)
