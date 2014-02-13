__author__ = 'Javier'

from pymongo import MongoClient

class MongoDB(object):

    def __init__(self, host = "localhost", port = 27017, db="labsk"):
        self.connection = MongoClient(host, port)
        self.db = self.connection[db]
        self.col = self.db[db + "_test"]

    def saveThread(self, thread):
        self.col.insert(thread)