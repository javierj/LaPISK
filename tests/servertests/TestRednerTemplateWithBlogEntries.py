__author__ = 'Javier'

import unittest
from tests.Harness import MockKimonoPlanetaLudicoAPI, Reports
from jinja2 import FileSystemLoader, Environment

class TestRednerTemplateWithBlogEntries(unittest.TestCase):

    def setUp(self):
        self.env = Environment(loader=FileSystemLoader('../../webgui/templates'))
        self.template = self.env.get_template("_static_report.html")

    def test_render_remplate_with_blog_entries_only(self):
        xhtml = self.template.render(keywords= MockKimonoPlanetaLudicoAPI.keywords_reort_json,
                            report=MockKimonoPlanetaLudicoAPI.report_json,
                            links=['Planeta Ludico'],
                            stats=["2 entries"]
                            )
        print xhtml
        self.assertEqual(True, False)

    def test_render_template_with_blog_and_forum_entries(self):
        report = MockKimonoPlanetaLudicoAPI.report_json
        report['madeira'].append(Reports.threats_with_newline)
        xhtml = self.template.render(keywords= MockKimonoPlanetaLudicoAPI.keywords_reort_json,
                            report=report,
                            links=['Planeta Ludico', 'LaBSK'],
                            stats=["2 entries"]
                            )
        print "--------------------------------------------"
        print xhtml
        self.assertEqual(True, False)

if __name__ == '__main__':
    unittest.main()
