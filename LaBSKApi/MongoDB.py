__author__ = 'Javier'

from pymongo import MongoClient

class MongoDB(object):

    def __init__(self, host = "localhost", port = 27017, db="labsk", col = None):
        self.connection = MongoClient(host, port)
        self.db = self.connection[db]
        if col is None:
            self.col = self.db[db + "_test"]
        else:
            self.col = self.db[col]

    def saveThread(self, thread):
        self.col.insert(thread)

    def threads(self):
        return self.col.find()