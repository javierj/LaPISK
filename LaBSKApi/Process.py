__author__ = 'Javier'

from HTML2Objects import AsuntoFactory
from modelobjects import ThreadModel


class VoidListener(object):
    def enteringThread(self, objthread):
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

    def skippingUnmodifiedThread(self, old, new):
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

    def setPageLimit(self, limit):
        self.pagelimit = limit

    def setMsgPageLimit(self, limit):
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

        processThread = ProcessThread(database=self.database, processmsgfactory=self.processmsgfactory)
        processThread.msgpagelimit = self.msgpagelimit
        processThread.listener = self.listener

        while repeat:
            #self._saveThread(page)
            processThread.processThread(page)
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

    def processThread(self, page):
        """ Main entri pint
            reads all threads in page and decides if read messages
            and store the thread or not
        """
        threadlist = page.createListOfAsuntos()
        for thread in threadlist:
            objthread = ThreadModel(thread)
            self._evaluate_thread(objthread)

    def _evaluate_thread(self, new_objthread):
        """ This method evaluates if the thread is fully readed,
            discarted or is readed from a concrete message
        """
        old_thread = self._search_thread(new_objthread)

        #print "old_thread: ", old_thread
        if old_thread is not None and self._is_unmodified(new_objthread, old_thread):
            self.listener.skippingUnmodifiedThread(old_thread, new_objthread)
            return

        self._enter_in_thread(new_objthread)

    def _search_thread(self, objthread):
        """ Serach if the new thread read from  the web is already stored
        """
        json_obj = self.database.find_one_by('link', objthread.link())
        if json_obj is None:
            return None
        return ThreadModel(json_obj)

    def _is_unmodified(self, new_thread, old_thread):
        """ Return true if thread is not modified
            It checks the answers of the new msg and the num of messages of the old one
            Answers in LaBSK do not count the first msg
        """
        same_msgs = new_thread.answers() == (old_thread.msgList().size() - 1 )
        #print "url: ",new_thread.link(),": ", new_thread.answers(), " == ", (old_thread.msgList().size() - 1 ), " is ", same_msgs
        return same_msgs

    def _enter_in_thread(self, objthread):
        self.listener.enteringThread(objthread)
        msgs = self._messagesfrom(objthread.json())
        info = self._createThreadStruct(objthread.json(), msgs)
        self.listener.msgsFound(len(msgs))
        self.database.saveThread(info)

    def _messagesfrom(self, thread):
        page = self.processmsgfactory.create(thread)
        process = self._createProcessMsgs()

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
        result['location'] = thread['location']
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
