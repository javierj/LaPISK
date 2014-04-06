__author__ = 'Javier'


class ReportStatsModel(object):

    def __init__(self, json):
        self._json = json
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
    """ Objects returned from de data repository
    """

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


class ReportStats(object):

    def __init__(self):
        self._threads = 0
        self._msgs = 0
        self._blogs = 0

    def inc_threads(self):
        self._threads += 1

    def inc_msgs(self, inc = 1):
        self._msgs += inc

    def inc_blogs(self, inc = 1):
        self._blogs += inc

    def merge(self, stats):
        self._blogs += stats._blogs
        self._msgs += self._msgs
        self._threads += self._threads

    def json(self):
        return {'threads':str(self._threads), 'msgs':str(self._msgs), 'blogs':str(self._blogs)}

    def __str__(self):
        """ for testing only
        """
        return "%s, %s, %s" % (self._threads, self._msgs, self._blogs)