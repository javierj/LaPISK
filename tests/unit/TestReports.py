__author__ = 'Javier'

import unittest
from tests.Harness import MockMongo, Reports
from LaBSKApi.reports import ReportBuilder, _word_in

class TestReportBuilder(unittest.TestCase):

    def setUp(self):
        self.mock = MockMongo()
        self.builder = ReportBuilder(self.mock)
        self.report = {'name': "TestReport" ,'keywords':['key', 'word']}
        self.thread = {'title': (self.report['keywords'][0]), 'msgs': []}
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
    """
    def test_thread_contains_keywords_return_false_when_no_keywords(self):
        thread = {'title': "no"}
        result = self.builder._thread_contains_keywords(thread, self.report['keywords'])
        self.assertFalse(result)

    def test_thread_contains_keywords_return_true_when_keywords(self):
        result = self.builder._thread_contains_keywords(self.thread, self.report['keywords'])
        self.assertTrue(result)
    """

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

        self.assertIn(self.keyword , result)
        self.assertLen(1, result[self.keyword ])

    def test_when_add_second_therad_report_contains_both(self):
        self.builder._add_thead_to_report(self.keyword , self.thread)
        self.builder._add_thead_to_report(self.keyword , self.thread)
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
        self.thread['msgs'].append({'date':'yes'})
        self.thread['msgs'].append({'date':'no'})
        self.builder._add_creation_date(self.thread)

        self.assertIn('creation_date', self.thread)
        self.assertEquals('yes', self.thread['creation_date'])


class TestWordIn(unittest.TestCase):
    def test_word_with_itsfel(self):
        self.assertTrue(_word_in("a", " a "))
    def test_word_ignore_case(self):
        self.assertTrue(_word_in("a", " A "))
    def test_word_dont_find_fragments(self):
        self.assertFalse(_word_in("a", "aa"))
    def test_word_dont_find_fragments_one_letter(self):
        self.assertFalse(_word_in("a", "a"))

if __name__ == '__main__':
    unittest.main()
