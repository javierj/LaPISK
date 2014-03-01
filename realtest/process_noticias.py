__author__ = 'Javier'

from LaBSKApi.Process import ProcessThreads
from LaBSKApi.MongoDB import MongoDB
from LaBSKApi.HTML2Objects import MsgPageFactory, AsuntoFactory
from LaBSKApi.web import labsk_urls
from tests.Harness import MockMongo
from datetime import datetime

class StdListener(object):
    def __init__(self):
        self.msgs = 0
        self.urls = 0

    def enteringThread(self, obj_thread):
        print "Thread ", obj_thread.title(), ", ", obj_thread.answers(), " | ", obj_thread.link()

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

    def newURL(self, url):
        """ url is a web.URL object
        """
        print "----------------------------------------------"
        print "---  ", url.desc, " ", url.url
        self.urls += 1

    def oldThreadFound(self, obj):
        """ A URL with the same link is already stored
        """
        print "Old thread found ", obj.title()

    def skippingUnmodifiedThread(self, obj):
        """ Old thread seems to be the same one than the new thread
        """
        print "No modification. Skipping ", obj.title()

    def __str__(self):
        return "Urls: " + str(self.urls) + " Messages readed: " + str(listener.msgs)

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

24/02(2014
limit = 4, 6 urls, 466 hilos, 7927 msgs
Total time:  0:22:58.348000 aprox.  seg;  seg por hilo
New: 15  Updated: 17 -- Casi toda la informacion es duplicada
518 hilos en el merge

25/02/2014
threads limit = 2, mspg pages limit = 2, 232 hilos 6urls, 3152 msgs
Total time:  0:07:06.326000
New: 89  Updated: 10
607 hilos en el merge / 9850 mensajes

26/02/2014
threads limit = 1, mspg pages limit = 4, 169 hilos 10 urls, 1430 msgs
Total time:  0:02:27.784000
New: 67  Updated: 102
674 hilos en el merge / 11275 mensajes por 613459 de LaBSK

26/02/2014
threads limit = 2, mspg pages limit = 6, 349 hilos 10 urls, 4201 msgs
Total time:  0:08:18.704000, 498,704 segundos || 1'43 seg por hilo || 0'119 seg por msgs
New: 68  Updated: 174
742 hilos en el merge / 14037 mensajes por 613459 de LaBSK


27/02/2014
threads limit = 2, mspg pages limit = 7, xx hilos 13 urls, xx msgs
La tuve que parar por fata de tiempo.
Empieoz a ver que va muy lento.
New: 73  Updated: 65
Msgs in Labsk_merge: 17184


28/02/2014
threads limit = 2, mspg pages limit = 5, 446 hilos, 13 urls, 8274 msgs
Total time:  0:24:03.480000, 1443,48 segundos || 3'237 seg por hilo || 0'175 seg por msgs
New: 44  Updated: 50
862 hilos en el merge / 19192 mensajes por 614302 de LaBSK


01/02/2014
threads limit = 1, mspg pages limit = 10, xx hilos, 15 urls, 8274 msgs
Total time:  0:33:07.646000, XX segundos || 3'237 seg por hilo || 0'175 seg por msgs
New: 44  Updated: 50
862 hilos en el merge / 19192 mensajes por 614302 de LaBSK


"""



#db = MongoDB(col="labsk_" + str(datetime.now()))
db = MongoDB()
db.query("labsk_merge")
db.insert("labsk_" + str(datetime.now()))

starttime = datetime.now()

listener = StdListener()
threads = ProcessThreads(db, MsgPageFactory())
threads.setListener(listener)
threads.setPageLimit(1)
threads.setMsgPageLimit(10)
print "Page limit ", threads.pagelimit, " Msg page limit ", threads.msgpagelimit

""" - Use this to play with threads
for labsk_url in labsk_urls:
    # Llevar esto a una clase estatica
    print "----------------------------------------------"
    print "---  ", labsk_url.desc, " ", labsk_url.url
    page = AsuntoFactory(url = labsk_url.url)

    threads.storeThreads(page)
"""

threads.scrapListOfURL(labsk_urls)
delta = datetime.now() - starttime

print "----------------------------------------------"
print "Total time: ", delta
print str(listener)

print "End."