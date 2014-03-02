__author__ = 'Javier'

from datetime import datetime


class Statistics(object):
    def __init__(self, db):
        self.db = db

    def all_visits(self):
        return [Visit()]

    def register_access(self, url, access_datetime):
        pass


class Visit(object):
    def access_datetime(self):
        return datetime(2014, 1, 1, 12, 0)

    def url(self):
        return "/"