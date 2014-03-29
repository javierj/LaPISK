__author__ = 'Javier'

from presenter.GUIModel import Text, Table
from tests.Harness import Reports
import unittest


class TestGUIModel(unittest.TestCase):

    def setUp(self):
        self.t = Text()

    def test_insert_br_no_newline(self):
        self.assertEqual("a", self.t.insert_br("a"))

    def test_insert_br_one_newline(self):
        self.assertEqual("a<br/>", self.t.insert_br("a\n"))

    def test_insert_br_several_newline(self):
        self.assertEqual("a<br/>a<br/><br/>a", self.t.insert_br("a\na\n\na"))

    def test_insert_br_real_newline(self):
        msg = u"Programaci\xf3n de la emisi\xf3n para hoy jueves 24.\nEn el aire"
        expected_msg = u"Programaci\xf3n de la emisi\xf3n para hoy jueves 24.<br/>En el aire"
        result = self.t.insert_br(msg)
        print result
        self.assertEqual(expected_msg, result)

    def test_change_newline_in_report(self):
        threat = Reports.asylum
        self.t.change_newline_in_report(Reports.asylum_keywords, threat)
        t = threat['Banjooli']
        #print t
        m = t[0]
        print m
        firm = m['msgs']
        msg = firm[0]['body']
        self.assertIn("<br/>", msg)
        self.assertNotIn("\n", msg)


class TestGUITable(unittest.TestCase):

    def setUp(self):
        self.table = Table()

    def test_add_one_title(self):
        self.table.append_title("X")
        self.assertEqual(self.table.titles, ["X"])

    def test_add_one_row(self):
        self.table.append_row("A", "B", "C")
        self.assertEqual(self.table.row(0), ("A", "B", "C"))

    def test_all_rows(self):
        self.table.append_row("A", "B", "C")
        self.assertEqual(self.table.rows, [("A", "B", "C")])


if __name__ == '__main__':
    unittest.main()