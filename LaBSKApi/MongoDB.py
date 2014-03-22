__author__ = 'Javier'

from pymongo import MongoClient


class MongoDB(object):

    COL_REPORT_STATS = "report_stats"
    COL_BLOGS = "blogs"

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

    def report_stats_collection(self):
        return Collection(MongoDB.COL_REPORT_STATS, self.db[MongoDB.COL_REPORT_STATS])

    def blogs_collection(self):
        return Collection(MongoDB.COL_BLOGS, self.db[MongoDB.COL_BLOGS])

    def authenticate(self, name, passwd):
        self.db.authenticate(name, passwd)

    def query(self, name):
        self.query_col = self.db[name]

    def insert(self, name):
        self.insert_col = self.db[name]

    def saveThread(self, thread):
        self.insert_col.insert(thread)

    # duplicated in collection
    def saveDocIn(self, colllection, doc):
        colllection.insert(doc)

    def threads(self):
        return self.col.find()

    def collection(self, name):
        return Collection(name, self.db[name])

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
            count += 1
        return count

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
        mr.total_threads(self.find_all().count())
        return mr

    # Duplicate
    def find_one_by(self, field, value):
        return self.query_col.find_one({field: value})

    def find_all(self):
        return self.query_col.find()


class Collection(object):
    """ Duplicated methods are untested.
    """

    def __init__(self, name, col):
        self.name = name
        self.col = col

    def __str__(self):
        return self.name

    # duplicated in MongoDB
    def save(self, doc):
        self.col.insert(doc)

    def remove(self, field, value):
        self.col.remove({field: value})

    # Duplicate
    def find_one(self, field, value):
        #print self.name, 'name', value+ "<<<"
        return self.col.find_one({field: value})


class MergeResult(object):

    def __init__(self):
        self.new_threads = 0
        self.updated_threads = 0
        self.threads = 0

    def new_thread(self):
        self.new_threads += 1

    def updated_thread(self):
        self.updated_threads += 1

    def total_threads(self, thread_num):
        self.threads = thread_num

    def __str__(self):
        return "New threads: " + str(self.new_threads) \
               + ". Updated threads: " + str(self.updated_threads) \
               + ". Threads in collection: " + str(self.threads)