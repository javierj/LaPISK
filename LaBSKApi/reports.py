__author__ = 'Javier'

from datetime import datetime

# Not in use
def _word_in(word, line):
    normal = word.lower().strip()
    normalword = " "+normal + " "
    print "'"+normalword, "' / '", line.lower()+"' "
    return normalword in line.lower()



class PreGeneratedReports(object):

    report_asylum_games = {'name': 'Informe de Asylum Games',
                            'keywords': ["Asylum Games", "Polis", "Mutinies", "Banjooli"]}
    report_devir = {'name': 'Informe de Devir',
                            'keywords': ["Devir"]}
    report_moviles = {'name': 'Juegos en dispositivos moviles',
                            'keywords': ["iphone", "ios", "android", "tablet"]}


class ReportBuilder(object):

    def __init__(self, db):
        self.db = db
        self.report = None
        self.report_request = None

    def _check_request(self, report_request):
        if 'keywords' not in report_request or len(report_request['keywords']) is 0:
            raise ValueError("No keywords in report: " + str(report_request))
        return

    def build_report(self, report_request):
        self._check_request(report_request)

        self.report_request = report_request
        self._create_report()
        for thread in self.db.threads():
            self._find_keywords(thread, report_request['keywords'])

        self._add_empty_keywords(report_request['keywords'])
        self._sorts_threads(report_request['keywords'], self.report)
        return self.report

    def _add_empty_keywords(self, keywords):
        for word in keywords:
            if word not in self.report:
                self.report[word] = list()

    def _find_keywords(self, thread, keywords):
        """
        """
        messagesWithKeyword = None
        for word in keywords:
            if self._word_in(word, thread['title']):
                self._add_creation_date(thread)
                self._drop_msgs_from_thread(thread)
                self._add_thead_to_report(word, thread)
            else:
                messagesWithKeyword = self._word_in_msgs(word, thread)
                if len(messagesWithKeyword) > 0:
                    # Add to report
                    self._add_creation_date(thread)
                    self._add_msgs_to_report(word, thread, messagesWithKeyword)

    def _add_creation_date(self, thread):
        if 'creation_date' in thread:
            return
        msgs = thread['msgs']
        if len(msgs) == 0:
            thread['creation_date'] = "No messages"
            return
        first = msgs[0]
        date = first['date']
        thread['creation_date'] = date

    def _drop_msgs_from_thread(self, thread):
        if 'msgs' in thread:
            thread.pop('msgs')

    def _add_thead_to_report(self, keyword, thread):
        """ Adds the therad to the list associated to the kwyword
            but frist opo out the messages of the thread
        """
        if self.report is None:
            self._create_report()
        if keyword not in self.report:
            self.report[keyword] = list()
        self.report[keyword].append(thread)

    def _create_report(self):
        """ Creates a new report using the name of the report request as title.
        """
        self.report = dict()
        if 'name' in self.report_request:
            self.report['title'] = "Result for report " + self.report_request['name']
        else:
            self.report['title'] = "Result for report."
        # Untested feature
        self.report['report_date'] = datetime.date(datetime.now())


    def _word_in_msgs(self, keyword, thread):
        """ Retur a list with the msgs in the therad tan contains the kwyord
            or an empry list if no message contains keyword.
        """
        result = list()
        if 'msgs' not in thread:
            return result
        for msg in thread['msgs']:
            if self._word_in(keyword, msg['body']):
                result.append(msg)
        return result

    def _word_in(self, word, line):
        """
        Returns true if word.lower() in line.lower()
        """
        normal = word.lower()
        #normalword = " "+normal.strip() + " "
        #print "'"+normalword, "' / '", line.lower()+"' "
        return normal in line.lower()

    def _add_msgs_to_report(self, keyword, thread, msgs):
        """ Adds a list of messages to a report's keyword that does not contain the hread
            (thread not contains keuwords in its tittle but some messages contain keywords)
        """
        thread['msgs'] = msgs
        self._add_thead_to_report(keyword, thread)

    def _sorts_threads(self, keywords, report):
        for kword in keywords:
            threads = report[kword]
            report[kword] = sorted(threads, key=lambda t:self._get_date_for_thread(t))

    def _get_date_for_thread(self, thread):
        """ A better way would be to use the therad object instead
        """
        if 'msgs' not in thread:
            return "ZZZ"
        return thread['msgs'][0]['date']