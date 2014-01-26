__author__ = 'Javier'

from features.steps.LaBSKMessagesPage import LaBSKMessagesPage
from features.steps.LaBSKThreadListPage import LaBSKThreadListPage
from LaBSKPages.web import WebClient
from bs4 import UnicodeDammit, BeautifulSoup

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

class TestLaBSKThreadListPage(unittest.TestCase):

    def test_getURLForThread(self):
        source = BeautifulSoup(u'<td class="subject windowbg2"><div><span id="msg_1169262"><a href="http://labsk.net/index.php?topic=119300.0">Fief - Feudo Ediciones MasQueOca editara Fief en Espanyol</a></span><p>Iniciado por <a href="http://labsk.net/index.php?action=profile;u=19849" title="Ver perfil de flOrO">flOrO</a><small id="pages1169262">x <a class="navPages" href="http://labsk.net/index.php?topic=119300.0">1</a> <a class="navPages" href="http://labsk.net/index.php?topic=119300.15">2</a> <a class="navPages" href="http://labsk.net/index.php?topic=119300.30">3</a> <span onclick="expandPages(this, "http://labsk.net/index.php?topic=119300.%1$d", 45, 210, 15);" onmouseover="this.style.cursor="pointer";" style="font-weight: bold;"> ... </span><a class="navPages" href="http://labsk.net/index.php?topic=119300.210">15</a>  x</small></p></div></td>')
        page = LaBSKThreadListPage(MockWebClient())
        self.assertEqual(page.getURLForThread(source), u'http://labsk.net/index.php?topic=119300.0')

if __name__ == '__main__':
    unittest.main()
