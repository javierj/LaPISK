__author__ = 'Javier'

from HTML2Objects import AsuntoFactory
from modelobjects import ThreadModel

class VoidListener(object):
    def enteringThread(self, title, link):
        pass

    def msgsFound(self, count):
        pass

    def nectPage(self, pagecount):
        pass

    def noMorePagea(self):
        pass

    def limitReached(self):
        pass

    def newMsg(self, user, body):
        pass

    def newURL(self, url):
        """ url is a web.URL object
        """
        pass

    def oldThreadFound(self, obj):
        """ A URL with the same link is already stored
        """
        pass

    def skippingUnmodifiedThread(self, obj):
        """ Old thread seems to be the same one than the new thread
        """
        pass

class ProcessThreads(object):
    def __init__(self, database, processmsgfactory):
        self.database = database
        self.processmsgfactory = processmsgfactory
        self.pagelimit = 1
        self.msgpagelimit = 1
        self.pagecount = 0
        self.listener = VoidListener()

    def setListener(self, listener):
        self.listener = listener

    def setPageLimit(self,limit):
        self.pagelimit = limit

    def setMsgPageLimit(self,limit):
        self.msgpagelimit = limit

    def scrapListOfURL(self, listOfURLS):
        """ Receives a list of web.URL objects
            for each, creates a page and calls self. storeThreads
        """
        for url in listOfURLS:
            self.listener.newURL(url)
            #page = AsuntoFactory(url = url.url)
            page = AsuntoFactory.createFromURLObject(url)
            self.storeThreads(page)

    def storeThreads(self, page):
        repeat = True
        self.pagecount = 1

        processThread = ProcessThread(database = self.database, processmsgfactory = self.processmsgfactory)
        processThread.msgpagelimit = self.msgpagelimit
        processThread.listener = self.listener

        while repeat:
            #self._saveThread(page)
            processThread._saveThread(page)
            self.pagecount += 1
            repeat = self._hasNext(page) and self._onlimit()
            if repeat:
                page = self._nextPage(page)
                self.listener.nectPage(self.pagecount)

    def _hasNext(self, page):
        res = page.nextUrl() is not ""
        if res is False:
           self.listener.noMorePagea()
        return res

    def _nextPage(self, oldpage):
        oldpage.changeUrl(oldpage.nextUrl())
        return oldpage

    def _onlimit(self):
        res = self.pagecount <= self.pagelimit
        if res is False:
           self.listener.limitReached()
        return res




class ProcessThread(object):

    def __init__(self, database = None, processmsgfactory = None):
        self.database = database
        self.processmsgfactory = processmsgfactory
        self.pagelimit = 1
        self.msgpagelimit = 1
        self.pagecount = 0
        self.listener = VoidListener()

    def _saveThread(self, page):
        threadlist = page.createListOfAsuntos()
        for thread in threadlist:
            objthread = ThreadModel(thread)
            self._evaluate_thread(objthread)

    def _evaluate_thread(self, objthread):
        old_thread = self.database.find_one_by('link', objthread.link())
        if old_thread is None:
            self._enter_in_thread(objthread)
            return

        obj_old_thread = ThreadModel(old_thread)
        self.listener.oldThreadFound(objthread)
        if not self._hilo_modificado(objthread, obj_old_thread):
            self.listener.skippingUnmodifiedThread(objthread)
            return

    def _hilo_modificado(self, obj1, obj2):
        if obj1.date() is not None and obj2.date() is not None:
            return obj1.date() == obj2.date()
        if obj1.answers() is not None and obj2.answers() is not None:
            return obj1.answers() == obj2.answers()
        return True


    def _enter_in_thread(self, objthread):
        self.listener.enteringThread(objthread.title(), objthread.link())
        msgs = self._messagesfrom(objthread.json())
        info = self._createThreadStruct(objthread.json(), msgs)
        self.listener.msgsFound(len(msgs))
        self.database.saveThread(info)

    def _messagesfrom(self, thread):
        page = self.processmsgfactory.create(thread)
        process = self._createProcessMsgs()

        # this should done by a factory
        process.setListener(self.listener)
        process.pagelimit = self.pagelimit

        return process.getMsgs(page)

    def _createProcessMsgs(self):
        """ Creates a ProcessMsgs to read the messages of a thread
        """
        process = ProcessMsgs()
        process.setListener(self.listener)
        process.pagelimit = self.msgpagelimit
        return process


    def _createThreadStruct(self, thread, msgs):
        result = dict()
        #result = ThreadModel.clone(thread)
        result['source'] = "LaBSK"
        # for testing
        if thread is None:
            return result
        result['title'] = thread['title']
        result['link'] = thread['link']
        result['msgs'] = msgs
        result['answers'] = len(msgs)
        return result


class ProcessMsgs(object):

    def __init__(self):
        self.pagelimit = 1
        self.pagecount = 0
        self.listener = VoidListener()

    def setListener(self, listener):
        self.listener = listener

    def getMsgs(self, page):
        self.pagecount = 1
        repeat = True
        msgs = list()
        while repeat:
            msgs.extend(self._readMsgs(page))
            self.pagecount += 1
            repeat = (page.nextUrl() is not "") and (self._onlimit())
            if repeat:
                page = self._nextPage(page)
                self.listener.nectPage(self.pagecount)

        return msgs

    def _nextPage(self, oldpage):
        oldpage.changeUrl(oldpage.nextUrl())
        return oldpage

    def _onlimit(self):
        return self.pagecount <= self.pagelimit

    def _readMsgs(self, page):
        msgs = list()
        content = page.createListOfMsgs()
        for msg in content:
            msgs.append(msg)
            self.listener.newMsg(msg['user'], msg['body'])
        return msgs
