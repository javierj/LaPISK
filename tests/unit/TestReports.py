__author__ = 'Javier'

import unittest
from tests.Harness import MockMongo, Reports, MockDatetime
from LaBSKApi.reports import ReportBuilder, PreGeneratedReports, ReportService, ReportStats
from mockito import mock, verify, when
from presenter.ReportPresenter import ReportResult


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

    ##################################################################################
    # Test cases:

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
        #print result

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


class TestSortingThreads(unittest.TestCase):

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

    def test_when_stats_for_a_report_does_not_exist_then_create_it(self):
        when(self.col).find_one('name', 'report').thenReturn(None)
        self.service._save_report_stats(self.empty_report_request, self.create_report_stat())
        verify(self.col).save(self.expected_stats_report)

    def test_saving_report_stats(self):
        when(self.col).find_one('name', 'report').thenReturn({'name': 'report', 'stats': []})
        self.service._save_report_stats({'name':'report'}, self.create_report_stat())
        verify(self.col).save(self.expected_stats_report)

    def test_when_building_repot_a_report_and_stats_are_returned(self):
        result = self.service.build_report(self.empty_report_request)
        self.assertIsInstance(result, ReportResult)

    def test_when_exists_a_stat_for_same_reort_and_date_delete_old_one(self):
        pass

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


class TestReportStats(unittest.TestCase):

    def test_json(self):
        stats = ReportStats()
        result = stats.json()
        self.assertEqual(result, {'threads':'0', 'msgs':'0', 'blogs':'0'})

    def test_reports_for_hootboardgame(self):
        stats = ReportStats()
        stats.inc_msgs()
        self.assertEqual(stats.json(), {'threads': '0', 'msgs': '1', 'blogs': '0'})
        stats.inc_threads()
        stats.inc_threads()
        self.assertEqual(stats.json(), {'threads': '2', 'msgs': '1', 'blogs': '0'})


if __name__ == '__main__':
    unittest.main()
