__author__ = 'Javier'

from features.steps.LaBSKMessagesPage import LaBSKMessagesPage
from LaBSKApi.WebClient import WebClient

import unittest

class MockWebClient:
    def sourceCode(self):
        return ""

class TestLaBSKMessagesPage(unittest.TestCase):

    def test_build_msg_builds_several_lines(self):
        page = LaBSKMessagesPage(MockWebClient())
        lines = ["A", "B", "C"]
        self.assertEqual(page.build_msg(lines), u'ABC')

    def test_search_new_page(self):
        webclient = WebClient("file:///C:/code/workspaces/Python/LaBSK-API/labsk_fief.html")
        page = LaBSKMessagesPage(webclient)
        self.assertIsNotNone(page.search_next_page())

    def test_search_no_new_page(self):
        webclient = WebClient("file:///C:/code/workspaces/Python/LaBSK-API/labsk_fief_last_page.html")
        page = LaBSKMessagesPage(webclient)
        self.assertIsNone(page.search_next_page())

if __name__ == '__main__':
    unittest.main()
