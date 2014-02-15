__author__ = 'Javier'


class ReportBuilder(object):

    def __init__(self, db):
        self.db = db
        self.report = None
        self.report_request = None

    def build_report(self, report_request):
        if 'keywords' not in report_request or len(report_request['keywords']) is 0:
            raise ValueError("No keywords in report: " + str(report_request))
            return

        self.report_request = report_request
        self._create_report()
        for thread in self.db.threads():
            self._find_keywords(thread, report_request['keywords'])

        self._add_empty_keywords(report_request['keywords'])
        return self.report

    # not tested
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
                self._drop_msgs_from_thread(thread)
                self._add_thead_to_report(word, thread)
            else:
                messagesWithKeyword = self._word_in_msgs(word, thread)
                if (len(messagesWithKeyword) > 0):
                    # Add to report
                    self._add_msgs_to_report(word, thread, messagesWithKeyword)

    def _drop_msgs_from_thread(self, thread):
        if 'msgs' in thread:
            thread.pop('msgs')

    def _add_thead_to_report(self, keyword, thread):
        """ Adds the therad but frist opo out the messages of the thread
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

    # Deprecated. delete it
    def _thread_contains_keywords(self, thread, keywords):
        """ True if any of the keywords is in thread's title.
            Case sensitive (fix this).
            Use the [ x for..] notation
        """
        for word in keywords:
            if word in thread['title']:
                return True
        return False

    def _word_in(self, word, line):
        return word.lower() in line.lower()

    def _word_in_msgs(self, keyword, thread):
        """ Retur a list with the msgs in the therad tan conatians the kwyord
            or an empry list if no message contains keyword.
        """
        result = list()
        if 'msgs' not in thread:
            return result
        for msg in thread['msgs']:
            if self._word_in(keyword, msg['body']):
                result.append(msg)
        return result

    def _add_msgs_to_report(self, keyword, thread, msgs):
        """ Adds a list of messages to a report's keyword that does not contain the hread
            (thread not contains keuwords in its tittle but some messages contain keywords)
        """
        thread['msgs'] = msgs
        self._add_thead_to_report(keyword, thread)

