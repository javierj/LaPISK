__author__ = 'Javier'


from GUIModel import Table


class ReportStatsPresenter(object):

    def __init__(self, service):
        self.service = service

    def stats_from_report(self, report_name):
        t = Table()
        rs_object = self.service.reportStatsFrorReport(report_name)
        self._create_titles(t)
        self._add_rows(t, rs_object)
        return t

    def _create_titles(self, table):
        table.append_title("Fecha", "Mensajes", "Incremento", "Asuntos", "Incremento", "Entradas de blog", "Incremento")

    def _add_rows(self, table, rs_object):
        previous = None
        for stat_obj in rs_object.stats:
            row = self._stat_as_text(stat_obj)
            # Untested blobk
            if previous is not None:
                self._calculate_increments(previous, row)
            table.append_row(row)
            previous = row

    def _stat_as_text(self, stat_obj):
        result_list = []
        result_list.append(stat_obj.date())
        result_list.append(stat_obj.msgs())
        result_list.append("0")
        result_list.append(stat_obj.threads())
        result_list.append("0")
        result_list.append(stat_obj.blogs())
        result_list.append("0")
        return result_list

    def _calculate_increments(self, yesterday, today):
        today[2] = self._dec(today[1], yesterday[1])
        today[4] = self._dec(today[3], yesterday[3])
        today[6] = self._dec(today[5], yesterday[5])

    def _dec(self, b, a):
        c = int(b) - int(a)
        return str(c)

