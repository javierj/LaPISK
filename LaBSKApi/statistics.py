__author__ = 'Javier'

from datetime import datetime

class Statistics(object):
    def __init__(self, db):
        self.db = db
        self._datetime = datetime
        self.ignore = dict()

    def all_visits(self):
        result = list()
        for vist_json in self.db.find_all():
            result.append(Visit.from_json(vist_json))
        return result

    def register_access_now(self, url, ip=None):
        if ip in self.ignore:
            return
        visit = Visit(url, self._datetime.now(), ip)
        self.db.saveThread(visit.json())

    def add_ignore_ip(self, ip_to_ignore):
        """ Adds a nw ip to ignore. If a visit cointais that IP is not stores
        """
        self.ignore[ip_to_ignore] = ip_to_ignore

class Visit(object):
    """ Stores one visit to a concrete page
    """
    def __init__(self, u, access_datetime, ip):
        self._url = u
        self._access_datetime = access_datetime
        self._ip = ip

    @property
    def access_datetime(self):
        return self._access_datetime

    @property
    def url(self):
        return self._url

    @property
    def ip(self):
        return self._ip

    def json(self):
        #return json.dumps(self)
        return {'url': self._url, 'datetime':str(self._access_datetime), 'ip': self._ip}

    @staticmethod
    def from_json(json_doc):
        ip = "No IP"
        if 'ip' in json_doc:
            ip = json_doc['ip']
        return Visit(json_doc['url'], json_doc['datetime'], ip)
