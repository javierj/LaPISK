__author__ = 'Javier'

from pymongo import MongoClient


class MongoDB(object):

    def __init__(self, host="localhost", port=27017, db="labsk", col=None):

        #self.connection = MongoClient(host, port)

        MONGODB_URI = host+":"+str(port)
        Connection_URL = "mongodb://" + MONGODB_URI + "/"
        self.connection = MongoClient(Connection_URL)
        self.db = self.connection[db]
        if col is None:
            self.col = self.db[db + "_test"]
        else:
            self.col = self.db[col]
        self.query_col = self.insert_col = self.col

    def authenticate(self, name, passwd):
        self.db.authenticate(name, passwd)

    def query(self, name):
        self.query_col = self.db[name]

    def insert(self, name):
        self.insert_col = self.db[name]

    def saveThread(self, thread):
        self.insert_col.insert(thread)

    def saveDocIn(self, colllection, doc):
        colllection.insert(doc)

    def threads(self):
        return self.col.find()

    def collection(self, name):
        return Collection(name)

    def drop(self, collection_name):
        self.db[str(collection_name)].drop()

    def len(self, col_name):
        """ For testing only
        """
        return self.db[str(col_name)].find().count()


    def copy(self, source_col, target_col):
        """ for testing only
        """
        count = 0
        source = self.db[str(source_col)]
        target = self.db[str(target_col)]
        #criterion = {field:doc[field]}
        for doc in source.find():
            self.saveDocIn(target, doc)

    """
        def merge(self, source_col, target_col, field):
        count = 0
        source = self.db[str(source_col)]
        target = self.db[str(target_col)]
        #criterion = {field:doc[field]}
        for doc in source.find():
            found = target.find_one({field: doc[field]})
            if found is None:
                #print "A"
                count += 1
                #print count
                self.saveDocIn(target, doc)
        return count
    """

    def merge(self, field):
        mr = self.merge_insert_wih_query(field)
        self.insert_col.drop()
        self.insert_col = None
        return mr

    def merge_insert_wih_query(self, id_field):
        mr = MergeResult()
        source = self.insert_col
        target = self.query_col
        for doc in source.find():
            found = target.find_one({id_field: doc[id_field]})
            if found is None:
                mr.new_thread()
                target.insert(doc)
            else:
                target.remove({id_field: doc[id_field]})
                target.save(doc)
                mr.updated_thread()
        #print "New:", inserted, ". Replaced:", replaced
        return mr

    def find_one_by(self, field, value):
        return self.query_col.find_one({field: value})

    def find_all(self):
        return self.query_col.find()


class Collection(object):

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class MergeResult(object):

    def __init__(self):
        self.new_threads=0
        self.updated_threads = 0

    def new_thread(self):
        self.new_threads += 1

    def updated_thread(self):
        self.updated_threads += 1

    def __str__(self):
        return "New threads: " + str(self.new_threads) + ". Updated threads: " + str(self.updated_threads)