__author__ = 'Javier'

import unittest
from presenter.ReportPresenter import ReportPresenter
from tests.Harness import Reports, MockMongo
from LaBSKApi.reports import PreGeneratedReports
from LaBSKApi.modelobjects import MsgModel
from mockito import mock, when

class TestReportPresenter(unittest.TestCase):

    pre = post = None
    #post = None
    def setUp(self):
        global pre, post
        self.presenter = ReportPresenter()
        self.asylum = Reports.asylum
        pre = post = self
        #post = self

    def test_when_transform_a_report_to_gui_first_text_is_report_name(self):
        result = self.presenter._toGUIMode(self.asylum, Reports.asylum_keywords)
        post.assertEqual(result.text[0], self.asylum['title'])

    def test_when_transform_a_report_to_gui_has_as_many_nexttext_as_keywords(self):
        result = self.presenter._toGUIMode(self.asylum, Reports.asylum_keywords)
        print result.nexttext
        post.assertEqual(len(result.nexttext), 4)

    def test_set_database(self):
        mock = MockMongo()
        self.presenter.database = mock
        self.assertEquals(self.presenter.database, mock)

    def test_when_report_has_no_msgs_with_year_return_same_report(self):
        polis = len(self.asylum['Polis'][0]['msgs'])
        banjooli = len(self.asylum['Banjooli'][0]['msgs'])
        asylum = len(self.asylum['Asylum Games'][0]['msgs'])
        self.presenter._filter_report_using_year(PreGeneratedReports.report_asylum_games, self.asylum, '2011')
        post.assertEqual(len(self.asylum['Polis'][0]['msgs']), polis)
        post.assertEqual(len(self.asylum['Banjooli'][0]['msgs']), banjooli)
        post.assertEqual(len(self.asylum['Asylum Games'][0]['msgs']), asylum)

    def test_when_deleting_2012_two_msg_from_polis_is_deleted(self):
        polis = len(self.asylum['Polis'][0]['msgs'])
        self.presenter._filter_report_using_year(PreGeneratedReports.report_asylum_games, self.asylum, '2012')
        post.assertEqual(len(self.asylum['Polis'][0]['msgs']), (polis-2))

    def test_when_deleting_2013_all_msg_from_polis_are_deleted(self):
        polis = len(self.asylum['Polis'][0]['msgs'])
        self.presenter._filter_report_using_year(PreGeneratedReports.report_asylum_games, self.asylum, '2013')
        post.assertEqual(len(self.asylum['Polis'][0]['msgs']), 0)

    def test_filer_msgs_in(self):
        msgs = [MsgModel({u'date': u' 24 de Octubre de 2013, 08:22:36 am \xbb'}),
               MsgModel({u'date': u' 24 de Octubre de 2012, 08:22:36 am \xbb'})]
        pre.assertEquals(2013, msgs[0].year())
        pre.assertEquals(2012, msgs[1].year())
        thread_mock = mock()
        when(thread_mock).msgs_objs().thenReturn(msgs)
        newlist = self.presenter._filer_msgs_in(thread_mock, '2012')
        post.assertEqual(len(newlist), 1)

    def test_filer_msgs_delete_all_msgs(self):
        msgs = [MsgModel({u'date': u' 24 de Octubre de 2013, 08:22:36 am \xbb'}),
               MsgModel({u'date': u' 24 de Octubre de 2012, 08:22:36 am \xbb'})]
        pre.assertEquals(2013, msgs[0].year())
        pre.assertEquals(2012, msgs[1].year())
        thread_mock = mock()
        when(thread_mock).msgs_objs().thenReturn(msgs)
        newlist = self.presenter._filer_msgs_in(thread_mock, '2013')
        post.assertEqual(len(newlist), 0)

    def test_filer_msgs_in_none(self):
        msgs = [MsgModel({u'date': u' 24 de Octubre de 2013, 08:22:36 am \xbb'}),
               MsgModel({u'date': u' 24 de Octubre de 2012, 08:22:36 am \xbb'})]
        pre.assertEquals(2013, msgs[0].year())
        pre.assertEquals(2012, msgs[1].year())
        thread_mock = mock()
        when(thread_mock).msgs_objs().thenReturn(msgs)
        newlist = self.presenter._filer_msgs_in(thread_mock, '2011')
        post.assertEqual(len(newlist), (2))

if __name__ == '__main__':
    unittest.main()
