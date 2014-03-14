__author__ = 'Javier'

import unittest
from presenter.ReportPresenter import ReportPresenter
from tests.Harness import Reports, MockMongo
from LaBSKApi.reports import PreGeneratedReports
from LaBSKApi.modelobjects import MsgModel
from mockito import mock, when, any


class TestReportPresenter(unittest.TestCase):

    pre = post = None

    def setUp(self):
        global pre, post
        self.presenter = ReportPresenter()
        self.asylum = Reports.asylum
        pre = post = self
        self.builder = mock()
        when(self.builder).build_report(any()).thenReturn("Valid")
        self.presenter.set_builder(self.builder)


    def test_when_transform_a_report_to_gui_first_text_is_report_name(self):
        result = self.presenter._toGUIMode(self.asylum, Reports.asylum_keywords)
        post.assertEqual(result.text[0], self.asylum['title'])

    def test_when_transform_a_report_to_gui_has_as_many_nexttext_as_keywords(self):
        result = self.presenter._toGUIMode(self.asylum, Reports.asylum_keywords)
        print result.nexttext
        post.assertEqual(len(result.nexttext), 4)

    def test_set_database(self):
        mongo_mock = MockMongo()
        self.presenter.database = mongo_mock
        self.assertEquals(self.presenter.database, mongo_mock)

    def test_report_and_stats_returns_a_report_and_stats(self):
        result = self.presenter.report_and_stats({'keywords':[]})
        post.assertIsNotNone(result)
        post.assertIsNotNone(result.report)
        post.assertIsNotNone(result.report_stats)

    def test_report_and_stats_returns_a_valid_report(self):
        result = self.presenter.report_and_stats({'keywords':[]})
        post.assertEquals(result.report, "Valid")

    def test_report_and_stats_returns_a_valid_stats(self):
        text_stats = self.presenter.generateStats(PreGeneratedReports.report_asylum_games, Reports.asylum)
        post.assertEquals(text_stats.text[0], "Asuntos encontrados: 4")
        post.assertEquals(text_stats.text[1], "Mensajes encontrados: 8")


class TestReportPresenter_FilteringMsgs(unittest.TestCase):

    pre = post = None

    def setUp(self):
        global pre, post
        self.presenter = ReportPresenter()
        self.asylum = Reports.asylum
        pre = post = self
        self.polis_msgs = self.asylum['Polis'][0]['msgs']
        self.msgs = [MsgModel({u'date': u' 24 de Octubre de 2013, 08:22:36 am \xbb'}),
                     MsgModel({u'date': u' 24 de Octubre de 2012, 08:22:36 am \xbb'})]
        self.thread_mock = mock()
        when(self.thread_mock).msgs_objs().thenReturn(self.msgs)

    def test_when_report_has_no_msgs_with_year_return_same_report(self):
        polis = len(self.polis_msgs)
        banjooli = len(self.asylum['Banjooli'][0]['msgs'])
        asylum = len(self.asylum['Asylum Games'][0]['msgs'])
        self.presenter._filter_report_using_year(PreGeneratedReports.report_asylum_games, self.asylum, '2011')
        post.assertEqual(len(self.polis_msgs), polis)
        post.assertEqual(len(self.asylum['Banjooli'][0]['msgs']), banjooli)
        post.assertEqual(len(self.asylum['Asylum Games'][0]['msgs']), asylum)

    def test_when_deleting_2012_two_msg_from_polis_is_deleted(self):
        polis = len(self.polis_msgs)
        self.presenter._filter_report_using_year(PreGeneratedReports.report_asylum_games, self.asylum, '2012')
        post.assertEqual(len(self.asylum['Polis'][0]['msgs']), (polis-2))

    def test_when_deleting_2013_all_msg_from_polis_are_deleted(self):
        self.presenter._filter_report_using_year(PreGeneratedReports.report_asylum_games, self.asylum, '2013')
        post.assertEqual(len(self.asylum['Polis'][0]['msgs']), 0)

    def test_filer_msgs_in_delete_2012_msg(self):
        pre.assertEquals(2013, self.msgs[0].year())
        pre.assertEquals(2012, self.msgs[1].year())
        newlist = self.presenter._filer_msgs_in(self.thread_mock, '2012')
        post.assertEqual(len(newlist), 1)

    def test_filer_msgs_delete_all_msgs(self):
        newlist = self.presenter._filer_msgs_in(self.thread_mock, '2013')
        post.assertEqual(len(newlist), 0)

    def test_filer_msgs_in_delete_0_msgs(self):
        newlist = self.presenter._filer_msgs_in(self.thread_mock, '2011')
        post.assertEqual(len(newlist), 2)

if __name__ == '__main__':
    unittest.main()
