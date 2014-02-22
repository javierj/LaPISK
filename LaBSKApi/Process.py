__author__ = 'Javier'


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


class ProcessThreads(object):
    def __init__(self, database, processmsgfactory):
        self.database = database
        self.processmsgfactory = processmsgfactory
        self.pagelimit = 1
        self.pagecount = 0
        self.listener = VoidListener()

    def setListener(self, listener):
        self.listener = listener

    def setPageLimit(self,limit):
        self.pagelimit = limit

    def storeThreads(self, page):
        repeat = True
        self.pagecount = 1
        while repeat:
            self._saveThread(page)
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

    def _saveThread(self, page):
        threadlist = page.createListOfAsuntos()
        for thread in threadlist:
            self.listener.enteringThread(thread['title'], thread['link'])
            msgs = self._messagesfrom(thread)
            info = self._createThreadStruct(thread, msgs)
            self.listener.msgsFound(len(msgs))
            self.database.saveThread(info)

    def _messagesfrom(self, thread):
        page = self.processmsgfactory.create(thread)
        process = ProcessMsgs()

        # this should done by a factory
        process.setListener(self.listener)
        process.pagelimit = self.pagelimit

        return process.getMsgs(page)

    def _createThreadStruct(self, thread, msgs):
        result = dict()
        #result = ThreadModel.clone(thread)
        result['source'] = "LaBSK"
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
