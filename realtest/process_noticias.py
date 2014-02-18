__author__ = 'Javier'

from LaBSKApi.Process import ProcessThreads
from LaBSKApi.MongoDB import MongoDB
from LaBSKApi.HTML2Objects import MsgPageFactory, AsuntoFactory
from tests.Harness import MockMongo
from datetime import datetime

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

"""
18/02/2014
limit = 2
4 urls

Total time:  0:05:17.864000
"""

limit = 2
print "Start. Page limit ", limit
print "-----------------------------------"

db = MongoDB(col="labsk_asylum_2")
#db = MockMongo()

starttime = datetime.now()

threads = ProcessThreads(db, MsgPageFactory())
threads.setListener(StdListener())
threads.setPageLimit(limit)

urls = ("http://labsk.net/index.php?board=18.0;sort=last_post;desc", # Noticias
        "http://labsk.net/index.php?board=158.0;desc", # Juegos en los medios
        "http://labsk.net/index.php?board=11.0;desc", # Dudas de reglas
        "http://labsk.net/index.php?board=77.0;desc" # Resenyas escritas
)

for labsk_url in urls:
    # Llevar esto a una clase estatica
    print "------------------------------------"
    print "--- URL: ", labsk_url
    page = AsuntoFactory(url = labsk_url)

    threads.storeThreads(page)

delta = datetime.now() - starttime

print "Total time: ", delta

print "End."