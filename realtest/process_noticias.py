__author__ = 'Javier'

from LaBSKApi.Process import ProcessThreads
from LaBSKApi.MongoDB import MongoDB
from LaBSKApi.HTML2Objects import MsgPageFactory, AsuntoFactory
from tests.Harness import MockMongo
from datetime import datetime

class StdListener(object):
    def __init__(self):
        self.msgs = 0

    def enteringThread(self, title, link):
        print "Thread ", title, " | ", link

    def msgsFound(self, count):
        #print "Msgs found: ", count
        pass

    def nectPage(self, pagecount):
        #print "Next page: ", pagecount
        pass

    def noMorePagea(self):
        pass

    def limitReached(self):
        #print "Limit of pages"
        pass

    def newMsg(self, user, body):
        #print "   ", user, ": ", body
        self.msgs += 1

"""
18/02/2014
limit = 2, 4 urls, 156 hilos
Total time:  0:05:17.864000 aprox 318 seg; 2'04 seg por hilo

22/02(2014
limit = 2, 6 urls, 230 hilos
Total time:  0:06:53.872000 aprox. 414 seg; 1'8 seg por hilo
Solo 110 hilos eran nuevos.

22/02(2014
limit = 4, 6 urls, 466 hilos, 7960 msgs
Total time:  0:19:38.590000 aprox. 1178,6 seg; 2'53 seg por hilo
Sin hacer Merge
"""

limit = 4
print "Start. Page limit ", limit

db = MongoDB(col="labsk_" + str(datetime.now()))
#db = MockMongo()

starttime = datetime.now()

listener = StdListener()
threads = ProcessThreads(db, MsgPageFactory())
threads.setListener(listener)
threads.setPageLimit(limit)

urls = ("http://labsk.net/index.php?board=18.0;sort=last_post;desc", # Noticias
        "http://labsk.net/index.php?board=158.0;desc", # Juegos en los medios
        "http://labsk.net/index.php?board=11.0;desc", # Dudas de reglas
        "http://labsk.net/index.php?board=133.0;desc", # DCompponentes y erratas
        "http://labsk.net/index.php?board=77.0;desc", # Resenyas escritas
        "http://labsk.net/index.php?board=20.0;desc" # enlaces
)

for labsk_url in urls:
    # Llevar esto a una clase estatica
    print "----------------------------------------------"
    print "--- URL: ", labsk_url
    page = AsuntoFactory(url = labsk_url)

    threads.storeThreads(page)

delta = datetime.now() - starttime

print "----------------------------------------------"
print "Total time: ", delta
print "Messages readed: ", listener.msgs

print "End."