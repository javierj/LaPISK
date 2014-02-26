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

    def saveDocIn(self, colllection, doc):
        colllection.insert(doc)

    def threads(self):
        return self.col.find()

    def collection(self, name):
        return Collection(name)

    def drop(self, collection):
        self.db[str(collection)].drop()

    def len(self, col):
        """ For testing only
        """
        return self.db[str(col)].find().count()

    def merge(self, source_col, target_col, field):
        count = 0
        source = self.db[str(source_col)]
        target = self.db[str(target_col)]
        #criterion = {field:doc[field]}
        for doc in source.find():
            found = target.find_one({field:doc[field]})
            if found is None:
                #print "A"
                count += 1
                #print count
                self.saveDocIn(target,doc)
        return count

    def find_one_by(self, field, value):
        return self.col.find_one({field:value})

class Collection(object):

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name