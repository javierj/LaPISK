__author__ = 'Javier'

import re
from datetime import datetime

meses = {"Enero": 1,
             "Febrero": 2,
            "Marzo": 3,
            "Abril": 4,
             "Mayo": 5,
             "Junio": 6,
             "Julio": 7,
             "Agosto": 8,
             "Septiembre": 9,
             "Octubre": 10,
             "Noviembre": 11,
             "Diciembre": 12
}


class ReportQueryModel(object):
    """ Nodels the set of jwyword and related infor
    for building a report.
    """
    def __init__(self, json):
        self.jsondoc = json

    def json(self):
        return self.jsondoc

    def getKeywords(self):
        return self.jsondoc['keywords']


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
        #

    def json(self):
        return self.jsondoc

    def body(self):
        return self.jsondoc['body']

    def id(self):
        if 'id' not in self.jsondoc:
            return None
        return self.jsondoc['id']

    def date(self):
        """ returns date in string format
        """
        return self.jsondoc['date']

    def year(self):
        return self.datetime().year

    def datetime(self):
        if 'date' not in self.jsondoc:
            return None
        s = re.search('([0-9][0-9]) de (.*) de ([0-9][0-9][0-9][0-9]), ([0-9][0-9]):([0-9][0-9]):([0-9][0-9]) ([ap]m)', self.date())

        #print int(s.group(6)), type(int(s.group(6)))

        if s is None:
            print "Date does nor match: ", self.json(), "<<"
            return datetime(1900,1,1, 1, 1, 1)


        return datetime(int(s.group(3)),
                        meses[s.group(2)],
                        int(s.group(1)),
                        int(s.group(4)),
                        int(s.group(5)),
                        int(s.group(6))
        )


class ThreadModel(object):
    """ Wraps a JSon containing a thread
        dont wrap msgs
    """
    def __init__(self, json):
        self.jsondoc = json
        if 'msgs' in self.jsondoc:
            self.msgs = MsgListModel(json['msgs'])
        else:
            #print "Thread without msgs: ", json
            self.msgs = None

    def json(self):
        return self.jsondoc

    def answers(self):
        """ If attribute is not in hread, the use the number of msgs minus one
            because LaNSK doses not count the first answer
        """
        if 'answers' not in self.jsondoc:
            return self.msgs.size() -1
        return int(self.jsondoc['answers'])

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

    def link(self):
        return self.jsondoc['link']

    def date(self):
        if 'date' not in self.jsondoc:
            return None
        return self.jsondoc['date']

    def set_date(self, date):
        self.jsondoc['date'] = date

    def msgList(self):
        return self.msgs

    def replace_msgs(self, msgs):
        self.jsondoc['msgs'] = msgs.json()

    def firstmsg(self):
        print "Fisrt msg: ", self.jsondoc['msgs']
        return MsgModel(self.jsondoc['msgs'][0])

    def id_last_msg(self):
        msg = self.msgs.lastmsg_object()
        return msg.id()

    def date_last_msg(self):
        return self.msgs.lastmsg_object().date()

    def replace_msgs_objs(self, msgs_objs):
        msgs = []
        for msg_obj in msgs_objs:
            msgs.append(msg_obj.json() )
        self.jsondoc['msgs'] = msgs

    def msgs_objs(self):
        objs = []
        for m in self.jsondoc['msgs']:
            objs.append(MsgModel(m))
        return objs


class MsgListModel(object):

    def __init__(self, json_code):
        self.jsondoc = json_code
        #self.list_msgs = json.loads(json_code)

    def json(self):
        return self.jsondoc
        #return json.dump(self.list_msgs)

    def replaceNewLineWith(self, newline):
        """ Didn't work
        """
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

    def lastmsg_object(self):
        return MsgModel(self.getMsg(self.size()-1))

    def append_msg(self, msg):
        self.jsondoc.append(msg)

    def size(self):
        return len(self.jsondoc)

