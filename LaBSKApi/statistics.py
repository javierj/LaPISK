__author__ = 'Javier'

from datetime import datetime
import json

class Statistics(object):
    def __init__(self, db):
        self.db = db
        self._datetime = datetime

    def all_visits(self):
        result = list()
        for vist_json in self.db.find_all():
            result.append(Visit.from_json(vist_json))
        return result


    def register_access_now(self, url):
        visit = Visit(url, self._datetime.now())
        self.db.saveThread(visit.json())


class Visit(object):

    def __init__(self, u, access_datetime):
        self._url = u
        self._access_datetime = access_datetime

    @property
    def access_datetime(self):
        return self._access_datetime

    @property
    def url(self):
        return self._url

    def json(self):
        #return json.dumps(self)
        return {'url': self._url, 'datetime':str(self._access_datetime)}

    @staticmethod
    def from_json(json_doc):
        return Visit(json_doc['url'], json_doc['datetime'])
