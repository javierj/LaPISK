__author__ = 'Javier'


class ProcessThreads(object):
    def __init__(self, database, processmsgfactory):
        self.database = database
        self.processmsgfactory = processmsgfactory
        self.pagelimit = 1
        self.pagecount = 0

    def storeThreads(self, page):
        repeat = True
        self.pagecount = 1
        while(repeat):
            self._saveThread(page)
            self.pagecount += 1
            repeat = (page.nextUrl() is not "") and self._onlimit()
            if repeat:
                page = self._nextPage(page)

    def _nextPage(self, oldpage):
        oldpage.changeUrl(oldpage.nextUrl())
        return oldpage

    def _onlimit(self):
        return self.pagecount <= self.pagelimit

    def _saveThread(self, page):
        threadlist = page.createListOfAsuntos()
        for thread in threadlist:
            msgs = self._messagesfrom(thread)
            info = self._createThreadStruct(thread, msgs)
            self.database.saveThread(info)

    def _messagesfrom(self, thread):
        page = self.processmsgfactory.create(thread)
        process = ProcessMsgs()
        return process.getMsgs(page)

    def _createThreadStruct(self, thread, msgs):
        result = dict()
        result['source'] = "LaBSK"
        result['title'] = thread['title']
        result['msgs'] = msgs
        return result


class ProcessMsgs(object):

    def __init__(self):
        self.pagelimit = 1
        self.pagecount = 0

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
        return msgs
