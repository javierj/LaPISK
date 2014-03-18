__author__ = 'Javier'

from datetime import datetime
from LaBSKApi.modelobjects import ThreadModel


# Not in use
def _word_in(word, line):
    normal = word.lower().strip()
    normalword = " "+normal + " "
    print "'"+normalword, "' / '", line.lower()+"' "
    return normalword in line.lower()


class PreGeneratedReports(object):

    report_hootboardgame = {'name': 'HootBoardGame',
                      'keywords': ["HootBoardGame", "HBG"]}

    report_moviles = {'name': 'Juegos en dispositivos moviles',
                      'keywords': ["iphone", "ios", "android", "tablet"]}

    # Editoriales 6

    report_asylum_games = {'name': 'Informe de Asylum Games',
                           'keywords': ["Asylum Games", "Polis", "Mutinies", "Banjooli"]}
    report_devir = {'name': 'Informe de Devir',
                    'keywords': ["Devir"]}
    report_ludonova = {'name': 'Editorial Ludonova',
                    'keywords': ["Ludonova"]}
    report_asmodee = {'name': 'Editorial Asmodee',
                    'keywords': ["Asmodee"]}
    report_lost_games = {'name': 'Editorial Ludonova',
                    'keywords': ["Lost Games"]}
    report_edge_entertainment = {'name': 'Editorial EDGE Entertainment',
                    'keywords': ["Edge"]}
    report_dizemo_entertainment = {'name': 'Editorial Dizemo Entertainment',
                    'keywords': ["dizemo"]}
    report_looping_games = {'name': 'Editorial Looping Games',
                    'keywords': ["Looping Games", "1911 AMUNDSEN vs SCOTT"]}
    report_nestor_games = {'name': 'Editorial Nestor Games',
                    'keywords': ["Nestor"]}
    report_morapiaf = {'name': 'Editorial Morapiaf',
                    'keywords': ["Morapiaf"]}


    # Tiendas: 9

    tienda_planeton = {'name': 'Tienda Planeton Games',
                      'keywords': ["planeton"]}
    tienda_100_doblones = {'name': 'Tienda 100 Doblones',
                      'keywords': ["100 doblones"]}
    tienda_zacatrus = {'name': 'Tienda Zacatrus',
                      'keywords': ["zacatrus", "coup"]}
    tienda_finplay = {'name': 'Tienda Finplay',
                      'keywords': ["finplay"]}
    tienda_tablerum = {'name': 'Tienda Tablerum',
                      'keywords': ["tablerum"]}
    tienda_evolution_goya = {'name': 'Tienda Evolution Goya',
                      'keywords': ["evolution goya", "Evolution Store"]}
    tienda_dungeon_marvels = {'name': 'Tienda Dungeon Marvels',
                      'keywords': ["dungeon marvels"]}
    tienda_mas_que_oca = {'name': 'Tienda Mas Que Oca',
                      'keywords': ["que oca", "masqueoca", "mqo"]}
    tienda_click_and_rol = {'name': 'Tienda Clickandrol',
                      'keywords': ["click and rol", "clickandrol"]}


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
        for word in keywords:
            if self._word_in(word, thread['title']):
                self._add_creation_and_last_msg_date(thread)
                self._drop_msgs_from_thread(thread)
                self._add_thead_to_report(word, thread)
            else:
                messagesWithKeyword = self._word_in_msgs(word, thread)
                if len(messagesWithKeyword) > 0:
                    # Add to report
                    self._add_creation_and_last_msg_date(thread)
                    self._add_link(thread, messagesWithKeyword)
                    self._add_msgs_to_report(word, thread, messagesWithKeyword)

    def _add_creation_and_last_msg_date(self, thread):
        if 'creation_date' in thread:
            return
        thread_obj = ThreadModel(thread)
        thread_obj.add_creation_and_last_update_dates()

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
        now = datetime.now()
        self.report['report_date'] = str(datetime.date(now)) +", " + str(now.hour) + ":" + str(now.minute)

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

    def _add_link(self, thread, messagesWithKeyword):
        # msg should be an object
        for msg in messagesWithKeyword:
            if 'id' in msg:
                msg['link'] = thread['link'] + "#" + msg['id']

    def _add_msgs_to_report(self, keyword, thread, msgs):
        """ Adds a list of messages to a report's keyword that does not contain the hread
            (thread not contains keuwords in its tittle but some messages contain keywords)
        """
        thread['msgs'] = msgs
        self._add_thead_to_report(keyword, thread)

    def _sorts_threads(self, keywords, report):
        for kword in keywords:
            threads = report[kword]
            report[kword] = sorted(threads, key=lambda t: self._get_date_for_thread(t), reverse=True)

    def _get_date_for_thread(self, thread):
        thread_obj = ThreadModel(thread)
        return thread_obj.last_msg_date_as_datetime()