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
        self.thread = 0
        self.skiped = 0

    def enteringThread(self, obj_thread):
        print "Thread ", obj_thread.title(), ", ", obj_thread.answers(), " | ", obj_thread.link()
        self.thread += 1

    def msgsFound(self, count):
        pass

    def nectPage(self, pagecount):
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
        """ url is a web.URL object        """
        print "----------------------------------------------"
        print "---  ", url.desc, " ", url.url
        self.urls += 1

    def skippingUnmodifiedThread(self, old, new):
        """ Old thread seems to be the same one than the new thread        """
        self.skiped += 1
        print old.answers(), "==", new.answers(), ". Skipping ", old.title(), " / ", old.link()

    def __str__(self):
        return "Urls: " + str(self.urls) + ". Threads: " + str(self.thread) + ". Messages readed: " + str(listener.msgs) + ". Threads skipped: " + str(self.skiped)


db = MongoDB()
db.query("labsk_merge")
db.insert("labsk_" + str(datetime.now()))

starttime = datetime.now()

listener = StdListener()
threads = ProcessThreads(db, MsgPageFactory())
threads.setListener(listener)
threads.setPageLimit(1)
threads.setMsgPageLimit(80) # Nunca bajes este valor o perderas mensajes, al menos mantenlo igual


threads.scrapListOfURL(labsk_urls)
delta = datetime.now() - starttime

print "----------------------------------------------"
print "Total time: ", delta
print "Page limit ", threads.pagelimit, " Msg page limit ", threads.msgpagelimit
print str(listener)

mr = db.merge('link')
print str(mr)
