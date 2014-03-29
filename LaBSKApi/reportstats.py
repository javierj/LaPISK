__author__ = 'Javier'

class ReportStatsService(object):
    """ Recoverst the stats for a report.
    Saving stats is in other class, it should be moved here
    """

    def __init__(self, mongo):
        self.col = mongo.report_stats_collection()

    def reportStatsFrorReport(self, service_name):
        stats = self.col.find_one('name', service_name)
        return ReportStatsModel(stats)


class ReportStatsModel(object):

    def __init__(self, json):
        self._json = json
        self.stats = self._create_list(json['stats'])

    def json(self):
        return self._json

    def _create_list(self, stats_json):
        stats = []
        for stat in stats_json:
            stats.append(ReportStatModel(stat))
        return stats

    def stats(self):
        return self.stats



class ReportStatModel(object):

    def __init__(self, json):
        self._json = json

    def json(self):
        return self._json

    def date(self):
        return self._json['date']

    def msgs(self):
        return self._json['msgs']

    def threads(self):
        return self._json['threads']

    def blogs(self):
        return self._json['blogs']
