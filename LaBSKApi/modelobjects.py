__author__ = 'Javier'


class ReportModel(object):
    def __init__(self, json):
        self.jsondoc = json

    def json(self):
        return self.jsondoc

    def getKeywords(self):
        words = list()
        for key in self.jsondoc.keys():
            if key.lower() != 'title' and key != "report_date":
                words.append(key)
        return  words

    def replaceNewLineWith(self, newline):
        for keyword in self.getKeywords():
            threadlist = self.jsondoc[keyword]
            threads = list()
            for json_thread in threadlist:
                thread = ThreadModel(json_thread)
                msgs = thread.msgList()
                msgs.replaceNewLineWith(newline)
                thread.replace_msgs(msgs)
                threads.append(thread)
            self.jsondoc[keyword] = threads


    def firstthread(self, key):
        return ThreadModel(self.jsondoc[key][0])


class MsgModel(object):
    """ Wraps a JSon containing a msg
    """
    def __init__(self, json):
        self.jsondoc = json

    def json(self):
        return self.jsondoc

    def body(self):
        return self.jsondoc['body']


class ThreadModel(object):
    """ Wraps a JSon containing a thread
        dont wrap msgs
    """
    def __init__(self, json):
        self.jsondoc = json

    def json(self):
        return self.jsondoc

    def answers(self):
        if 'answers' not in self.jsondoc:
            return None
        return self.jsondoc['answers']

    def set_answers(self, a):
        self.jsondoc['answers'] = a

    def views(self):
        return self.jsondoc['views']

    def source(self):
        return self.jsondoc['source']

    def title(self):
        return self.jsondoc['title']

    def location(self):
        return self.jsondoc['location']

    def date(self):
        if 'date' not in self.jsondoc:
            return None
        return self.jsondoc['date']

    def set_date(self, date):
        self.jsondoc['date'] = date

    def msgList(self):
        return MsgListModel(self.jsondoc['msgs'])

    def replace_msgs(self, msgs):
        self.jsondoc['msgs'] = msgs.json()

    def firstmsg(self):
        print "Fisrt msg: ", self.jsondoc['msgs']
        return MsgModel(self.jsondoc['msgs'][0])


class MsgListModel(object):
    def __init__(self, json):
        self.jsondoc = json

    def json(self):
        return self.jsondoc

    def replaceNewLineWith(self, newline):
        result = list()
        for msg in self.jsondoc:
            #print "Before: ", msg['body']
            result_msg = msg.copy()
            new_msg = msg['body'].replace("\n", newline)
            #print "After: ", new_msg
            result_msg['body'] = new_msg
            result.append(result_msg)
        self.jsondoc = result

    def getMsg(self, index):
        return self.jsondoc[index]