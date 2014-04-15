__author__ = 'Javier'

import re
from datetime import datetime


class DateManager(object):
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

    def __init__(self, now = datetime.now):
        self.now = now

    def hoy(self):
        date = self.now()
        return str(date.day) + " de " + self.month_name(date.month) + " de " + str(date.year)

    def month_name(self, index):
        return DateManager.meses.keys()[DateManager.meses.values().index(index)]


class ReportQueryModel(object):
    """ Nodels the set of jwyword and related infor
    for building a report.
    """
    def __init__(self, json):
        self.jsondoc = json

    def json(self):
        return self.jsondoc

    def keywords(self):
        return self.jsondoc['keywords']

    def name(self):
        return self.jsondoc['name']


class ReportModel(object):
    """ Deprecated. Try to use ReportEntriesModel
    """

    def __init__(self, json):
        self.jsondoc = json

    def json(self):
        return self.jsondoc

    def getKeywords(self):
        words = list()
        for key in self.jsondoc.keys():
            if key.lower() != 'title' and key.lower() != "report_date":
                words.append(key)
        return words

    def firstthread(self, key):
        return ThreadModel(self.jsondoc[key][0])

    def threads_in(self, key):
        threads = [ThreadModel(t) for t in self.jsondoc[key]]
        return threads

    # Untested
    def count_entries_in(self, key):
        return len(self.jsondoc[key])

    def set_threads_to(self, keyw, threads):
        self.jsondoc[keyw] = threads

    # Untested
    def add_thread(self, key, thread):
        self.jsondoc[key].append(thread)


class ReportEntriesModel(object):
    """ This class sores entries (thredas and blogs) modeled as objects
        This class replaces the ReportModel class

        # Untested class
    """

    def __init__(self):
        self.report= dict()
        self._title = ""
        self._report_date = ""

    def json(self):
        return "No implemented yet"

    def set_title(self, title):
        self._title = title

    def set_report_date(self, report_date):
        self._report_date = report_date

    def entries_in(self, key):
        return self.report[key]

    def count_entries_in(self, key):
        return len(self.report[key])

    def set_entries_to(self, keyw, threads):
        self.report[keyw] = threads

    def add_entry(self, key, thread):
        if key not in self.report:
            self.report[key] = []
        self.report[key].append(thread)

    # Tesing only
    def size(self):
        return len(self.report)


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

        return MsgModel.build_datetime(self.date())

    @staticmethod
    def build_datetime(date):
        s = re.search('([0-9][0-9]) de (.*) de ([0-9][0-9][0-9][0-9]), ([0-9][0-9]):([0-9][0-9]):([0-9][0-9]) ([ap]m)', date)
        s = re.search('([0-9][0-9]) de (.*) de ([0-9][0-9][0-9][0-9]), ([0-9][0-9]):([0-9][0-9]):([0-9][0-9]) ([ap]m)', date)

        if s is None:
            s = re.search('([0-9][0-9]) de (.*) de ([0-9][0-9][0-9][0-9]), a las ([0-9][0-9]):([0-9][0-9]):([0-9][0-9]) ([ap]m)', date)

        if s is None:
            return datetime(1900,1,1, 1, 1, 1)

        return datetime(int(s.group(3)),
                        DateManager.meses[s.group(2)],
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
            self.msgs =  MsgListModel([])

    def json(self):
        return self.jsondoc

    def answers(self):
        """ If attribute is not in hread, the use the number of msgs minus one
            because LaNSK doses not count the first answer
        """
        if 'answers' not in self.jsondoc:
            return self.msgs.size() - 1
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
        """ Text plain date
        """
        if 'date' not in self.jsondoc:
            return None
        return self.jsondoc['date']

    def set_date(self, date):
        self.jsondoc['date'] = date

    def msgList(self):
        return self.msgs

    def msg_count(self):
        return self.msgList().size()

    def firstmsg(self):
        #print "Fisrt msg: ", self.jsondoc['msgs']
        #return MsgModel(self.jsondoc['msgs'][0])
        return self.msgs.firstmsg_object()

    def id_last_msg(self):
        msg = self.msgs.lastmsg_object()
        return msg.id()

    def date_last_msg(self):
        """ Date in plain text
        """
        return self.msgs.lastmsg_object().date()

    def date_first_msg(self):
        """ Date in plain text
        """
        return self.msgs.firstmsg_object().date()

    def replace_msgs_objs(self, msgs_objs):
        msgs = []
        for msg_obj in msgs_objs:
            msgs.append(msg_obj.json())
        self.jsondoc['msgs'] = msgs
        self.msgs = MsgListModel(self.jsondoc['msgs'])

    def msgs_objs(self):
        objs = []
        if 'msgs' in self.jsondoc:
            for m in self.jsondoc['msgs']:
                objs.append(MsgModel(m))
        return objs

    def year_last_msg(self):
        #print "year_last_msg:", self.link(), ", ", self.msgList().size()
        if 'last_msg_date' in self.jsondoc:
            return self.last_msg_date_as_datetime().year
        if self.msgList().size() == 0:
            return None
        return self.msgList().lastmsg_object().year()

    def year(self):
        return self.year_last_msg()

    def add_creation_and_last_update_dates(self):
        """ Use this mathod only generating reports
        """
        if self.msg_count() == 0:
            self.jsondoc['creation_date'] = "No messages"
            self.jsondoc['last_msg_date'] = "No messages"
            return
        self.jsondoc['creation_date'] = self.date_first_msg()
        self.jsondoc['last_msg_date'] = self.date_last_msg()

    def last_msg_date_as_datetime(self):
        if 'last_msg_date' not in self.jsondoc:
            self.jsondoc['last_msg_date'] = self.date_last_msg()
        return MsgModel.build_datetime(self.jsondoc['last_msg_date'])

    def has_msgs(self):
        """ This method is used by the report's filtering to distingsh
        a thread entry from a blog entry.
        """
        return True

    def date_as_datetime(self):
        """ This method is sued by the sorted service to sort report entries
        """
        return self.last_msg_date_as_datetime()


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
            result_msg = msg.copy()
            new_msg = msg['body'].replace("\n", newline)
            result_msg['body'] = new_msg
            result.append(result_msg)
        self.jsondoc = result

    def getMsg(self, index):
        return self.jsondoc[index]

    def lastmsg_object(self):
        if self.size() == 0:
            return None
        return MsgModel(self.getMsg(self.size()-1))

    def firstmsg_object(self):
        return MsgModel(self.getMsg(0))

    def append_msg(self, msg):
        self.jsondoc.append(msg)

    def size(self):
        return len(self.jsondoc)
