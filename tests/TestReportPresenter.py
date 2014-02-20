__author__ = 'Javier'

import unittest
from presenter.ReportPresenter import ReportPresenter
from Harness import Reports, MockMongo

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

if __name__ == '__main__':
    unittest.main()
