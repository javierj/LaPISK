__author__ = 'Javier'





class ProcessThreads(object):
    def __init__(self, database, processmsgfactory):
        self.database = database
        self.processmsgfactory = processmsgfactory


    def storeThreads(self, page):
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

    def getMsgs(self, page):
        msgs = list()
        content = page.createListOfMsgs()
        for msg in content:
            msgs.append(msg)
        return msgs

