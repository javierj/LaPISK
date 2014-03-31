__author__ = 'Javier'


class ReportStatsModel(object):

    def __init__(self, json):
        self._json = json
#        print json
#        print json['stats']
#        print "Hellooo"
        self._stats = self._create_list(json['stats'])

    def json(self):
        return self._json

    def _create_list(self, stats_json):
        stats = []
        for stat in stats_json:
            stats.append(ReportStatModel(stat))
        return stats

    @property
    def stats(self):
        return self._stats


class ReportStatsService(object):
    """ Recoverst the stats for a report.
    Saving stats is in other class, it should be moved here
    """

    def __init__(self, mongo):
        self.col = mongo.report_stats_collection()

    def reportStatsFrorReport(self, service_name):
        stats = self.col.find_one('name', service_name)
        stats_obj = self._buidl_object(stats)
        return stats_obj

    def _buidl_object(self, stats):
        if stats is None:
            return ReportStatsModel({u'stats': [{'date': "No stats found",
                                                'msgs': '0',
                                                'threads': '0',
                                                'blogs': '0'}]})
        return ReportStatsModel(stats)


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
