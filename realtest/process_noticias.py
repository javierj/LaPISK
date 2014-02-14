__author__ = 'Javier'

from LaBSKApi.Process import ProcessThreads
from LaBSKApi.MongoDB import MongoDB
from LaBSKApi.HTML2Objects import MsgPageFactory, AsuntoFactory
from tests.Harness import MockMongo

class StdListener(object):
    def enteringThread(self, title, link):
        print "Thread ", title, " | ", link

    def msgsFound(self, count):
        print "Msgs found: ", count

    def nectPage(self, pagecount):
        print "Nect page: ", pagecount

    def noMorePagea(self):
        pass

    def limitReached(self):
        print "Limit of pages"

    def newMsg(self, user, body):
        print "   ", user, ": ", body


limit = 3
print "Start. Page limit ", limit
print "-----------------------------------"

#db = MongoDB()
db = MockMongo()
threads = ProcessThreads(db, MsgPageFactory())
threads.setListener(StdListener())
threads.setPageLimit(limit)

# Llevar esto a una clase estatica
page = AsuntoFactory(url = "http://labsk.net/index.php?board=18.0;sort=last_post;desc")

threads.storeThreads(page)



print "End."