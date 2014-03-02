__author__ = 'Javier'

from datetime import datetime


class Statistics(object):
    def __init__(self, db):
        self.db = db
        self._mock_visits = list()
        self._datetime = datetime

    def all_visits(self):
        return self._mock_visits

    def register_access_now(self, url):
        self._mock_visits.append(Visit(url, self._datetime.now()))


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


