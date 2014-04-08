from LaBSKApi.reportstats import ReportStats

__author__ = 'Javier'

import unittest
from tests.Harness import MockMongo, Reports, MockDatetime
from LaBSKApi.reports import ReportBuilder, PreGeneratedReports, \
    ReportService, ReportBuilderService, SaveReportStatsService, \
    FilteringService, FilterMsgYear, FilterEntryYear, SortService
from mockito import mock, verify, when, any
from presenter.ReportPresenter import ReportResult
from LaBSKApi.modelobjects import ThreadModel, ReportQueryModel
from LaBSKApi.PlanetaLudico import BlogEntry


def create_mock_for_db():
    col = mock()
    mongo = mock()
    when(mongo).report_stats_collection().thenReturn(col)
    return (mongo, col)

def transtale_report_into_threads(report_query, report):
    new_report = {}
    for kword in report_query['keywords']:
        threads = []
        for thread in report[kword]:
            threads.append(ThreadModel(thread))
        new_report[kword] = threads
    return new_report


class TestReportBuilder(unittest.TestCase):

    def setUp(self):
        self.mock = MockMongo()
        self.builder = ReportBuilder(self.mock)
        self.report = {'name': "TestReport", 'keywords': ['key', 'word']}
        self.thread = {'title': (self.report['keywords'][0]), 'msgs': []}.copy()
        self.keyword = self.report['keywords'][0]
        self.builder.report_request = self.report

    def assertLen(self, count, elements):
        self.assertEquals(count, len(elements))

    def test_when_report_has_no_keywords_launch_exception(self):
        emptyReport = dict()
        self.assertRaises(ValueError, self.builder.build_report, emptyReport)

    def test_when_report_has_keywords_calls_hreads(self):
        self.builder.build_report(self.report)

        self.assertEquals(self.mock.threadscalled, 1)

    def test_report_has_title(self):
        self.builder._create_report()
        result = self.builder.report
        self.assertEqual(result['title'], "Result for report TestReport")

    def test_when_add_first_therad_first_create_report(self):
        self.builder._add_thead_to_report("", dict())
        result = self.builder.report
        self.assertEqual(result['title'], "Result for report TestReport")

    def test_when_add_first_therad_report_contains_the_keyword(self):
        self.builder._add_thead_to_report('key', self.thread)
        result = self.builder.report

        self.assertIn(self.keyword, result)
        self.assertLen(1, result[self.keyword])

    def test_when_add_second_therad_report_contains_both(self):
        self.builder._add_thead_to_report(self.keyword, self.thread)
        self.builder._add_thead_to_report(self.keyword, self.thread)
        result = self.builder.report

        self.assertLen(2, result[self.keyword])

    def test_when_keyword_is_foun_in_therad_titles_then_msgs_are_not_added(self):
        self.builder._find_keywords(self.thread, ['key'])
        #self.builder._add_thead_to_report('key', self.thread)
        keyline = self.builder.report[self.keyword][0]
        self.assertNotIn('msgs', keyline)

    def test_words_are_searched_in_title_ignoring_case(self):
        self.thread['title']= self.keyword.lower()

        self.builder._add_thead_to_report(self.keyword.upper(), self.thread)
        result = self.builder.report
        self.assertIn(self.keyword.upper(), result)

    def test_word_in_msgs_when_msg_coitains_keyword(self):
        self.thread['msgs'].append({'body': self.keyword})
        result = self.builder._word_in_msgs(self.keyword, self.thread)
        self.assertLen(1, result)

    def test_word_in_msgs_when_msg_not_coitains_keyword(self):
        self.thread['msgs'].append({'body': "No word"})
        result = self.builder._word_in_msgs(self.keyword, self.thread)
        self.assertLen(0, result)

    def test_word_in_msgs_when_msg_is_empty(self):
        result = self.builder._word_in_msgs(self.keyword, self.thread)
        self.assertLen(0, result)

    def test_word_in_with_zacatrus(self):
        word = PreGeneratedReports.tienda_zacatrus['keywords'][0]
        msg_title = u'Clash of Cultures a 33,75\x80 en Zacatrus (ZMAN)'
        self.assertTrue(self.builder._word_in(word, msg_title))

    def test_add_msgs_to_report(self):
        msg = {'body': "Message"}
        msglist = [msg]
        self.builder._add_msgs_to_report(self.keyword, self.thread, msglist)

        result = self.builder.report
        self.assertLen(1, result[self.keyword])
        thread = result[self.keyword][0]
        self.assertIn('msgs', thread)
        msgs = thread['msgs']
        self.assertEquals(msgs[0]['body'], msg['body'])

    def test_report_includes_creation_date_of_thread(self):
        self.thread['msgs'] = Reports.asylum_msg_list
        self.mock.saveThread(self.thread)
        self.assertLen(1, self.mock.threads())

        result = self.builder.build_report(self.report)
        # print result
        self.assertLen(1, result[self.keyword])
        first_thread = result[self.keyword][0]
        self.assertEquals(first_thread['creation_date'], Reports.asylum_msg_list[0]['date'])

    def test_add_creation_date_two_messages(self):
        self.thread['msgs'].append({'date': 'yes'})
        self.thread['msgs'].append({'date': 'no'})
        self.builder._add_creation_and_last_msg_date(self.thread)

        self.assertIn('creation_date', self.thread)
        self.assertEquals('yes', self.thread['creation_date'])

    def test_when_thread_already_has_creation_date_then_exit(self):
        self.thread['creation_date'] = "Already exists"
        self.builder._add_creation_and_last_msg_date(self.thread)

        self.assertEqual("Already exists", self.thread['creation_date'])

    def test_report_includes_date_of_last_msg(self):
        self.thread['msgs'] = Reports.asylum_msg_list
        self.mock.saveThread(self.thread)
        self.assertLen(1, self.mock.threads())

        result = self.builder.build_report(self.report)
        # print result
        self.assertLen(1, result[self.keyword])
        first_thread = result[self.keyword][0]
        self.assertEquals(first_thread['last_msg_date'], Reports.asylum_msg_list[0]['date'])

    def test_msg_has_a_link(self):
        self.thread['msgs'] = [{'id': 'xxx'}]
        self.thread['link'] = 'yyy'
        self.builder._add_link(self.thread, self.thread['msgs'])

        msg = self.thread['msgs'][0]
        self.assertIn('link', msg)
        self.assertEquals(msg['link'], 'yyy#xxx')

    def test_when_msg_has_no_id_link_is_the_same_than_the_thread(self):
        self.thread['msgs'] = [{}]
        self.thread['link'] = 'yyy'
        self.builder._add_link(self.thread, self.thread['msgs'])

        msg = self.thread['msgs'][0]
        self.assertNotIn('link', msg)

    def test_hilo_con_mas_de_una_keyword(self):
        thread = {u'title': u'Guardian cross para Android/Iphone/Ipad', u'answers': 1, 'creation_date': u' 03 de Junio de 2013, 10:55:11 am \xbb', u'source': u'LaBSK', u'link': u'http://labsk.net/index.php?topic=111335.0', u'location': u'Videojuegos'}
        #threadobj = ThreadModel(thread)

        self.builder._find_keywords(thread, ["iphone", "ios", "android", "tablet"])
        report = self.builder.report
        self.assertEquals(1, len(report["iphone"]))
        self.assertEquals(1, len(report["android"]))


class TestSortingThreads_Deprecated(unittest.TestCase):
    """ This test suite test the sorting in the report builder.
        Nor the sorting has moved to a comlete service
    """

    def setUp(self):
        self.mock = MockMongo()
        self.builder = ReportBuilder(self.mock)
        self.report = {'name': "TestReport", 'keywords': ['key', 'word']}
        self.thread = {'title': (self.report['keywords'][0]), 'msgs': []}.copy()
        self.keyword = self.report['keywords'][0]
        self.builder.report_request = self.report

    def test_sorts_threads_by_creation_date_and_hour(self):
        report = {'key': [ {'title':'b', 'msgs': [{'date': u' 21 de Noviembre de 2012, 10:18:38 am \xbb'}]},
                           {'title':'a', 'msgs': [{'date': u' 21 de Noviembre de 2012, 10:28:38 am \xbb'}]}]}
        self.builder._sorts_threads(['key'], report)
        self.assertEqual(report['key'][0]['title'], "a")
        self.assertEqual(report['key'][1]['title'], "b")

    def test_sorts_threads_by_second(self):
        report = {'key': [{'title': 'b', 'msgs': [{'date': u' 21 de Noviembre de 2012, 10:28:36 am \xbb'}]},
                           {'title': 'a', 'msgs': [{'date': u' 21 de Noviembre de 2012, 10:28:37 am \xbb'}]}]}
        self.builder._sorts_threads(['key'], report)
        self.assertEqual(report['key'][0]['title'], "a")
        self.assertEqual(report['key'][1]['title'], "b")

    def test_sorts_threads_by_creation_date_and_moth(self):
        report = {'key': [{'title': 'b', 'msgs': [{'date': u' 21 de Noviembre de 2012, 10:28:38 am \xbb'}]},
                           {'title': 'a', 'msgs': [{'date': u' 21 de Diciembre de 2012, 10:18:38 am \xbb'}]}]}
        self.builder._sorts_threads(['key'], report)
        self.assertEqual(report['key'][0]['title'], "a")
        self.assertEqual(report['key'][1]['title'], "b")

    def test_sorts_threads_by_creation_date_year(self):
        report = {'key': [{'title': 'b', 'msgs':[{'date':u' 21 de Diciembre de 2011, 10:28:38 am \xbb'}]},
                           {'title': 'a', 'msgs':[{'date':u' 21 de Noviembre de 2012, 10:18:38 am \xbb'}]}]}
        self.builder._sorts_threads(['key'], report)
        self.assertEqual(report['key'][0]['title'], "a")
        self.assertEqual(report['key'][1]['title'], "b")

    def test_sorts_threads_by_creation_date_without_date(self):
        report = {'key': [ {'title':'b', 'msgs':[{'date':u'  \xbb'}], 'link': "Test data"},
                           {'title':'a', 'msgs':[{'date':u' 21 de Noviembre de 2012, 10:18:38 am \xbb'}]}]}
        self.builder._sorts_threads(['key'], report)
        self.assertEqual(report['key'][0]['title'], "a")
        self.assertEqual(report['key'][1]['title'], "b")


class TestReportService(unittest.TestCase):

    def create_report_stat(self):
        report_stats = ReportStats()
        report_stats.inc_msgs()
        report_stats.inc_threads()
        return report_stats

    def setUp(self):
        self.col = mock()
        self.mongo = mock()
        when(self.mongo).report_stats_collection().thenReturn(self.col)
        self.service = ReportService(self.mongo)
        self.service._builder = mock()
        self.service._now = MockDatetime()
        self.empty_report_request = {'name':'report', 'keywords':[]}
        self.expected_stats_report = {'name':'report', 'stats':[
            {'date':'2014-1-1', 'threads':'1', 'msgs':'1', 'blogs':'0'}]}

    def test_when_creates_a_service_it_includes_the_report_builder(self):
        self.service = ReportService(self.mongo)
        self.assertIsInstance(self.service._builder, ReportBuilder)

    def test_when_generating_a_report_report_builder_is_called(self):
        self.service.build_report(self.empty_report_request)
        verify(self.service._builder, 1).build_report(self.empty_report_request)

    def test_when_building_repot_a_report_and_stats_are_returned(self):
        result = self.service.build_report(self.empty_report_request)
        self.assertIsInstance(result, ReportResult)

    def test_building_a_report_stats_are_saved(self):
        when(self.col).find_one('name', 'report').thenReturn(None)
        self.service.build_report(self.empty_report_request)
        verify(self.col).save(any())


class TestSaveReportStatsService(unittest.TestCase):

    def create_report_stat(self):
        report_stats = ReportStats()
        report_stats.inc_msgs()
        report_stats.inc_threads()
        return report_stats

    def setUp(self):
        (self.mongo, self.col) = create_mock_for_db()
        self.service = SaveReportStatsService(self.mongo)
        self.service._now = MockDatetime()
        self.empty_report_request = {'name':'report', 'keywords':[]}
        self.expected_stats_report = {'name':'report', 'stats':[
            {'date':'2014-1-1', 'threads':'1', 'msgs':'1', 'blogs':'0'}]}

    def test_find_stat_with_date_no_delete(self):
        stats = {u'stats': [{u'date': u'2014-3-22', u'blogs': u'0', u'threads': u'0', u'msgs': u'0'}], u'name': u'HootBoardGame'}
        stats_len = 1
        self.service._delete_with_date_now(stats)
        self.assertEqual(len(stats['stats']), stats_len)

    def test_find_stat_with_date_delete(self):
        stats = {u'stats': [{u'date': u'2014-1-1', u'blogs': u'0', u'threads': u'0', u'msgs': u'0'}],
                 u'name': u'HootBoardGame'}
        self.service._delete_with_date_now(stats)
        self.assertEqual(len(stats['stats']), 0)

    def test_when_stats_for_a_report_does_not_exist_then_create_it(self):
        when(self.col).find_one('name', 'report').thenReturn(None)
        self.service._save_report_stats(self.empty_report_request['name'], self.create_report_stat())
        verify(self.col).save(self.expected_stats_report)

    def test_saving_report_stats(self):
        when(self.col).find_one('name', 'report').thenReturn({'name': 'report', 'stats': []})
        self.service._save_report_stats('report', self.create_report_stat())
        verify(self.col).save(self.expected_stats_report)


class TestReportBuilderService(unittest.TestCase):

    def setUp(self):
        (self.db, self.col) = create_mock_for_db()
        self.service = ReportBuilderService(self.db)
        self.empty_report_request = {'name':'report', 'keywords':[]}

    def test_when_generating_a_report_service_calls_all_reports_module(self):
        report_module = mock()
        self.service.add_module(report_module)
        self.service.build_report(self.empty_report_request)
        #empty_report = {}
        #empty_ststa = ReportStats()
        verify(report_module).build_report(self.empty_report_request, any(), any())

    def test__build_empty_report_with_all_keywords(self):
        result = self.service._create_empty_report(Reports.asylum_report_request)
        for word in Reports.asylum_report_request['keywords']:
            self.assertIn(word, result)

    def test_when_building_report_save_stats(self):
        self.service.save_stats = mock()
        self.service.build_report(self.empty_report_request)
        verify(self.service.save_stats, 1)._save_report_stats(self.empty_report_request['name'], any())


class TestReportFilteringService(unittest.TestCase):

    def setUp(self):
        self.filtering = FilteringService()
        self.asylum_report = transtale_report_into_threads(Reports.asylum_report_request, Reports.get_asylum_report())
        self.asylum_report_query = ReportQueryModel(Reports.asylum_report_request)

    def test_when_filtering_without_filter_result_is_teh_same(self):
        self.filtering.filter_report(self.asylum_report_query, self.asylum_report)
        expected = transtale_report_into_threads(Reports.asylum_report_request, Reports.get_asylum_report())
        self.assertEqual(len(self.asylum_report['Polis']), len(expected['Polis']))

    def test_when_deleting_2012_two_msg_from_polis_is_deleted(self):
        filterMsgYear = FilterMsgYear('2012')
        self.filtering.add_filter(filterMsgYear)
        polis = self.asylum_report['Polis'][0].msg_count()

        self.filtering.filter_report(self.asylum_report_query, self.asylum_report)
        self.assertEqual(self.asylum_report['Polis'][0].msg_count(), (polis-2))

    def test_when_deleting_2013_all_therads_from_polis_are_deleted(self):
        self.filtering.add_filter(FilterEntryYear('2013'))

        self.filtering.filter_report(self.asylum_report_query, self.asylum_report)
        self.assertEqual(len(self.asylum_report['Polis']), 0)

    def test_deleing_threads_and_blog_entries(self):
        blog_entry = BlogEntry({"date": "21 marzo, 2013"})
        self.asylum_report['Polis'].append(blog_entry)
        self.filtering.add_filter(FilterEntryYear('2013'))

        self.filtering.filter_report(self.asylum_report_query, self.asylum_report)
        self.assertEqual(len(self.asylum_report['Polis']), 0)

    def test_deleing_threads_and_blog_entries_no_deletes(self):
        blog_entry = BlogEntry({"date": "21 marzo, 2013"})
        self.asylum_report['Polis'].append(blog_entry)
        self.filtering.add_filter(FilterEntryYear('2012'))

        self.filtering.filter_report(self.asylum_report_query, self.asylum_report)
        self.assertEqual(len(self.asylum_report['Polis']), 2)


class TestFilterMsgYear(unittest.TestCase):

    def setUp(self):
        self.thread_obj = ThreadModel(Reports.get_asylum_polis_thread())
        self.msg_count = self.thread_obj.msg_count()
        self.filter2012 = FilterMsgYear('2012')

    def test_when_entry_has_not_msgs_then_it_remains_unchanged(self):
        entry_mock = mock()
        when(entry_mock).has_msgs().thenReturn(False)
        result = self.filter2012.filter(entry_mock)
        verify(entry_mock, 1).has_msgs()
        verify(entry_mock, 0).msgs_objs()
        self.assertTrue(result)

    def test_when_entry_has_not_msgs_with_or_under_indicated_date_it_remains_unchanged(self):
        filter2011 = FilterMsgYear('2011')
        filter2011.filter(self.thread_obj)
        self.assertEqual(self.thread_obj.msg_count(), self.msg_count)

    def test_when_entry_has_msgs_with_the_indicated_date_remove_them(self):
        self.filter2012.filter(self.thread_obj)
        self.assertEqual((self.msg_count - 2), self.thread_obj.msg_count())

    def test_when_entry_has_msgs_with_the_indicated_and_under_date_remove_them(self):
        filter2013 = FilterMsgYear('2013')
        filter2013.filter(self.thread_obj)
        self.assertEqual(0, self.thread_obj.msg_count())


class TestFilterEntryYear(unittest.TestCase):

    def setUp(self):
        self.thread_obj = ThreadModel(Reports.get_asylum_polis_thread())

    def test_when_entry_date_is_over_filtering_return_true(self):
        filter2011 = FilterEntryYear('2011')
        include = filter2011.filter(self.thread_obj)
        self.assertTrue(include)

        filter2012 = FilterEntryYear('2012')
        include = filter2012.filter(self.thread_obj)
        self.assertTrue(include)

    def test_when_entry_date_is_equal_or_under_over_filtering_return_true(self):
        filter2013 = FilterEntryYear('2013')
        include = filter2013.filter(self.thread_obj)
        self.assertFalse(include)


class TestSortingService(unittest.TestCase):
    """ This test suite test the sorting in the report builder.
        Nor the sorting has moved to a comlete service
    """

    def setUp(self):
        self.service = SortService()
        self.report = {'name': "TestReport", 'keywords': ['key', 'word']}
        self.thread = {'title': (self.report['keywords'][0]), 'msgs': []}.copy()
        self.keyword = self.report['keywords'][0]

    def test_sorts_threads_by_creation_date_and_hour(self):
        report = {'key': [ {'title':'b', 'msgs': [{'date': u' 21 de Noviembre de 2012, 10:18:38 am \xbb'}]},
                           {'title':'a', 'msgs': [{'date': u' 21 de Noviembre de 2012, 10:28:38 am \xbb'}]}]}
        report_obj = transtale_report_into_threads({'keywords':['key']}, report)
        self.service.sort_report(['key'], report_obj)
        self.assertEqual(report_obj['key'][0].title(), "a")
        self.assertEqual(report_obj['key'][1].title(), "b")

    def test_sorts_threads_by_second(self):
        report = {'key': [{'title': 'b', 'msgs': [{'date': u' 21 de Noviembre de 2012, 10:28:36 am \xbb'}]},
                           {'title': 'a', 'msgs': [{'date': u' 21 de Noviembre de 2012, 10:28:37 am \xbb'}]}]}
        report_obj = transtale_report_into_threads({'keywords':['key']}, report)
        self.service.sort_report(['key'], report_obj)
        self.assertGoesFirst(report_obj, "a")
        self.assertEqual(report_obj['key'][1].title(), "b")

    def test_sorts_threads_by_creation_date_and_moth(self):
        report = {'key': [{'title': 'b', 'msgs': [{'date': u' 21 de Noviembre de 2012, 10:28:38 am \xbb'}]},
                           {'title': 'a', 'msgs': [{'date': u' 21 de Diciembre de 2012, 10:18:38 am \xbb'}]}]}
        report_obj = transtale_report_into_threads({'keywords':['key']}, report)
        self.service.sort_report(['key'], report_obj)
        self.assertGoesFirst(report_obj, "a")
        self.assertEqual(report_obj['key'][1].title(), "b")

    def test_sorts_threads_by_creation_date_year(self):
        report = {'key': [{'title': 'b', 'msgs':[{'date':u' 21 de Diciembre de 2011, 10:28:38 am \xbb'}]},
                           {'title': 'a', 'msgs':[{'date':u' 21 de Noviembre de 2012, 10:18:38 am \xbb'}]}]}
        report_obj = transtale_report_into_threads({'keywords':['key']}, report)
        self.service.sort_report(['key'], report_obj)
        self.assertGoesFirst(report_obj, "a")
        self.assertEqual(report_obj['key'][1].title(), "b")

    def test_sorts_threads_by_creation_date_without_date(self):
        report = {'key': [ {'title':'b', 'msgs':[{'date':u' 21 de Diciembre de 2011, 10:28:38 am \xbb'}],
                            'link': "Test data"},
                           {'title':'a', 'msgs':[{'date':u' 21 de Noviembre de 2012, 10:18:38 am \xbb'}]}]}
        report_obj = transtale_report_into_threads({'keywords':['key']}, report)
        self.service.sort_report(['key'], report_obj)
        self.assertGoesFirst(report_obj, "a")
        self.assertEqual(report_obj['key'][1].title(), "b")

    # Test con entradas de blog

    def test_sorts_threads_and_blog_entry_goes_first(self):
        report = {'key': [ {'title':'b', 'msgs':[{'date':u' 21 de Diciembre de 2011, 10:28:38 am \xbb'}],
                            'link': "Test data"},
                           {'title':'a', 'msgs':[{'date':u' 21 de Noviembre de 2012, 10:18:38 am \xbb'}]}]}
        report_obj = transtale_report_into_threads({'keywords':['key']}, report)
        entry = BlogEntry({'date':'23 Noviembre, 2012'})
        report_obj['key'].append(entry)
        self.service.sort_report(['key'], report_obj)
        self.assertEqual(report_obj['key'][1].title(), "a")
        self.assertEqual(report_obj['key'][2].title(), "b")

    def test_sorts_threads_and_blog_entry_goes_last(self):
        report = {'key': [ {'title':'b', 'msgs':[{'date':u' 21 de Diciembre de 2011, 10:28:38 am \xbb'}],
                            'link': "Test data"},
                           {'title':'a', 'msgs':[{'date':u' 21 de Noviembre de 2012, 10:18:38 am \xbb'}]}]}
        report_obj = transtale_report_into_threads({'keywords':['key']}, report)
        entry = BlogEntry({'date':'23 Noviembre, 2010'})
        report_obj['key'].append(entry)
        self.service.sort_report(['key'], report_obj)
        self.assertGoesFirst(report_obj, "a")
        self.assertEqual(report_obj['key'][1].title(), "b")

    def test_sorts_threads_and_blog_entry_goes_in_the_middle(self):
        report = {'key': [ {'title': 'b', 'msgs': [{'date': u' 21 de Diciembre de 2011, 10:28:38 am \xbb'}],
                            'link': "Test data"},
                           {'title':'a', 'msgs':[{'date':u' 21 de Noviembre de 2012, 10:18:38 am \xbb'}]}]}
        report_obj = transtale_report_into_threads({'keywords':['key']}, report)
        entry = BlogEntry({'date':'23 Enero, 2012'})
        report_obj['key'].append(entry)
        self.service.sort_report(['key'], report_obj)
        self.assertGoesFirst(report_obj, "a")
        self.assertEqual(report_obj['key'][2].title(), "b")


    def assertGoesFirst(self, report, title):
        self.assertEqual(report['key'][0].title(), title)

if __name__ == '__main__':
    unittest.main()
