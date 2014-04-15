from LaBSKApi.reportstats import ReportStats

__author__ = 'Javier'

from datetime import datetime
from LaBSKApi.modelobjects import ThreadModel, ReportModel, ReportQueryModel, ReportEntriesModel
from presenter.ReportPresenter import ReportResult
# Too much dependencies
from LaBSKApi.MongoDB import MongoDB
from PlanetaLudico import PlanetaLudicoReport
from LaBSKApi.LaBSK import LaBSKReportBuilder


class PreGeneratedReports(object):

    report_hootboardgame = {'name': 'HootBoardGame',
                      'keywords': ["HootBoardGame", "HBG"]}

    report_moviles = {'name': 'Juegos en dispositivos moviles',
                      'keywords': ["iphone", "ios", "android", "tablet"]}

    # Editoriales 4

    report_asylum_games = {'name': 'Informe de Asylum Games',
                           'keywords': ["Asylum Games", "Polis", "Mutinies", "Banjooli"]}
    """
    #report_devir = {'name': 'Informe de Devir',
    #                'keywords': ["Devir"]}
    #report_ludonova = {'name': 'Editorial Ludonova',
    #                'keywords': ["Ludonova"]}
    #report_lost_games = {'name': 'Editorial Ludonova',
    #                'keywords': ["Lost Games"]}
    #report_edge_entertainment = {'name': 'Editorial EDGE Entertainment',
    #                'keywords': ["Edge"]}
    #report_looping_games = {'name': 'Editorial Looping Games',
    #                'keywords': ["Looping Games", "1911 AMUNDSEN vs SCOTT"]}
    #report_nestor_games = {'name': 'Editorial Nestor Games',
    #                'keywords': ["Nestor"]}
    """
    report_asmodee = {'name': 'Editorial Asmodee',
                    'keywords': ["Asmodee"]}
    #report_dizemo_entertainment = {'name': 'Editorial Dizemo Entertainment',
    #                'keywords': ["dizemo"]}
    report_morapiaf = {'name': 'Editorial Morapiaf',
                    'keywords': ["Morapiaf"]}

    """
    # Tiendas: 7

    #tienda_planeton = {'name': 'Tienda Planeton Games',
    #                  'keywords': ["planeton"]}
    #tienda_100_doblones = {'name': 'Tienda 100 Doblones',
    #                  'keywords': ["100 doblones"]}
    #tienda_dungeon_marvels = {'name': 'Tienda Dungeon Marvels',
    #                  'keywords': ["dungeon marvels"]}
    """
    tienda_zacatrus = {'name': 'Tienda Zacatrus',
                      'keywords': ["zacatrus", "coup"]}
    tienda_finplay = {'name': 'Tienda Finplay',
                      'keywords': ["finplay"]}
    tienda_tablerum = {'name': 'Tienda Tablerum',
                      'keywords': ["tablerum"]}
    tienda_evolution_goya = {'name': 'Tienda Evolution Goya',
                      'keywords': ["evolution goya", "Evolution Store"]}
    tienda_mas_que_oca = {'name': 'Tienda Mas Que Oca',
                      'keywords': ["que oca", "masqueoca", "mqo"]}
    tienda_click_and_rol = {'name': 'Tienda Clickandrol',
                      'keywords': ["click and rol", "clickandrol"]}
    tienda_demartina = {'name': 'Tienda DeMartina',
                      'keywords': ["demartina"]}

    # tienda: Juegos en la Mesa

class ReportBuilder(object):
    """ Builds a report using the information in mongodb from labsk
    """
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
            #print thread
            #print "thread"
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
        #print keywords
        for word in keywords:
            #print word in  thread['title']
            if self._word_in(word, thread['title']):
                #print word in  thread['title']
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
        """ Returns true if word.lower() in line.lower()
        """
        normal = word.lower()
        #normalword = " "+normal.strip() + " "
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


class ReportService(object):
    """ This class creates and generated a report and stores the stats in
        a MomgoDB column
    """

    def __init__(self, db):
        self.db = db
        self._builder = ReportBuilder(db)
        #self._collection = db.report_stats_collection()
        #self._now = datetime

    def build_report(self, report_request):
        result = self._build_report_from_modules(report_request)
        stats = self._generateStats(report_request, result)
        self._save_report_stats(report_request, stats)
        return ReportResult(result, stats)

    def _build_report_from_modules(self, report_request):
        result = self._builder.build_report(report_request)
        return result

    def _generateStats(self, report_request, report_json):
        result = ReportStats()
        report_obj = ReportModel(report_json)
        for key in report_request['keywords']:
            for thread_obj in report_obj.threads_in(key):
                result.inc_threads()
                result.inc_msgs( thread_obj.msg_count() )

        return result

    def _save_report_stats(self, report_request, stats):
        service = SaveReportStatsService(self.db)
        service._save_report_stats(report_request['name'], stats)


class SaveReportStatsService(object):

    def __init__(self, db):
        self._collection = db.report_stats_collection()
        self._now = datetime

    def _save_report_stats(self, report_name, report_stats):
        """ I need two abtsractions here. first one a mediator between this class and
            the collection that knows the structure of the json.
            The second abstraction is an object fro report_request.
        """

        json_report = self._collection.find_one('name', report_name)
        if json_report is None:
            #self._collection.save({'stats': [], 'name': report_request['name']})
            json_report = {'stats': [], 'name': report_name}
        else:
            self._collection.remove('name', report_name)
            self._delete_with_date_now(json_report)

        json_stats = report_stats.json()
        now = self._now.now()
        json_stats['date'] = str(now.year) + "-" + str(now.month) + "-" + str(now.day)
        json_report['stats'].append(json_stats)

        #print json_report
        self._collection.save(json_report)

    def _delete_with_date_now(self, json_report):
        now = self._now.now()
        now_date = str(now.year) + "-" + str(now.month) + "-" + str(now.day)
        new_stats = []
        for stat in json_report['stats']:
            if stat['date'] != now_date:
                new_stats.append(stat)
        json_report['stats'] = new_stats


#################################################################
# Filtering services


class FilterMsgYear(object):
    """ Report_entry must has a method called has_msgs()
    """

    def __init__(self, year):
        self._year = int(year)

    def filter(self, report_entry):
        """ A filter retusn true if the entry should be not filtered.
        """
        if not report_entry.has_msgs():
            return True
        msgs = []
        for msgobj in report_entry.msgs_objs():
            if msgobj.year() > self._year:
                #print "Add"
                msgs.append(msgobj)
        report_entry.replace_msgs_objs(msgs)
        return True

    def __str__(self):
        return "Se omiten mensajes desde el "+str(self._year)+" o posteriores"


class FilterEntryYear(object):
    """ Report entry  must ahs a method called year()
    """

    def __init__(self, year):
        self._year = int(year)

    def filter(self, report_entry):
        return report_entry.year() > self._year

    def __str__(self):
        return "Se omiten asuntos sin mensajes desde el "+str(self._year)+" o posteriores"


class FilteringService(object):
    """ Filters a report using the filters added.
        Report must be a dict of objects.
        Methods of the objects depnds on the type of filters.
    """

    def __init__(self):
        self.filters = []

    def add_filter(self, filter):
        self.filters.append(filter)

    def filter_report(self, report_query, report_objects):
        for kword in report_query.keywords():
            entries = self._select_entries(report_objects[kword])
            report_objects[kword] = entries

    def _select_entries(self, report_objects):
        entries = []
        for entry in report_objects:
               include = True
               for filter_obj in self.filters:
                   include = filter_obj.filter(entry)
                   if not include:
                       break
               if include:
                   entries.append(entry)
        return entries

    def descriptions_from_filters(self):
        result = [str(filter) for filter in self.filters]
        if result is None:
            return []
        return result


class FilteringServiceFactory():
    """ Several methods to facilitate the creation of
        filtering_service objects
    """

    @staticmethod
    def create_2_filters_same_year(year):
        service = FilteringService()
        service.add_filter(FilterEntryYear(year))
        service.add_filter(FilterMsgYear(year))
        return service


class SortService(object):
    """ Objects in report must have a date() method.
    """
    def sort_report(self, keywords, report_object):
        for kword in keywords:
            entries = report_object[kword]
            report_object[kword] = sorted(entries, key=lambda t: t.date_as_datetime(), reverse=True)


class ReportBuilderService(object):
    """ This class creates and generated a report and stores the stats in
        a MomgoDB column.
        Seeral report modules may be used for diferent data sources.
        This service expects a filtering service propertly configures.
        In other case, there is no filtering
    """

    def __init__(self, filter_service = FilteringService()):
        self.report_modules = []
        #self.db = db
        self.save_stats = None
        self.sorting_service = SortService()
        self.filter_service = filter_service

    def add_module(self, module):
        self.report_modules.append(module)

    def set_filter_service(self, fs):
        self.filter_service = fs

    def set_save_stats_service(self, service):
        self.save_stats = service

    def build_report(self, report_request):
        """ This mehtod should return a json ???"""
        report_obj = self._create_empty_report(report_request)
        #report_obj = ReportModel(report_json)
        report_query = ReportQueryModel(report_request)
        stats = ReportStats()
        for module in self.report_modules:
            module.build_report(report_request, report_obj, stats)
        self._save_stats(report_query.name(), stats)
        self._filter_report(report_query, report_obj)
        self.sorting_service.sort_report(report_query.keywords(), report_obj)
        return ReportResult(report_obj, stats)

    def _create_empty_report(self, report_request):
        """
        report = dict()
        if 'name' in report_request:
            report['title'] = "Result for report " + report_request['name']
        else:
            report['title'] = "Result for report."
        # Untested feature
        now = datetime.now()
        report['report_date'] = str(datetime.date(now)) +", " + str(now.hour) + ":" + str(now.minute)

        for keyword in report_request['keywords']:
            report[keyword] = []
        """

        report = ReportEntriesModel()
        if 'name' in report_request:
            report.set_title("Result for report " + report_request['name'])
        else:
            report.set_title("Result for report.")

        now = datetime.now()
        report.set_report_date( str(datetime.date(now)) +", " + str(now.hour) + ":" + str(now.minute) )

        return report

    def _save_stats(self, report_name, stats):
        self.save_stats._save_report_stats(report_name, stats)

    def _filter_report(self, report_query, report):
        self.filter_service.filter_report(report_query, report)

    def descriptions_from_filters(self):
        return self.filter_service.descriptions_from_filters()


class ReportBuilderServiceFactory(object):

    @staticmethod
    def create_service_with_all_modules():
        service = ReportBuilderService()
        service.add_module(LaBSKReportBuilder(ReportBuilder(MongoDB(col=MongoDB.COL_LABSK))))
        service.add_module(PlanetaLudicoReport(ReportBuilder(MongoDB(col=MongoDB.COL_BLOGS))))
        service.set_save_stats_service(SaveReportStatsService(MongoDB(col=MongoDB.COL_REPORT_STATS)))
        return service