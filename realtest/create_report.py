__author__ = 'Javier'

"""
Creates an static report
"""

from jinja2 import FileSystemLoader, TemplateNotFound, Environment
from tests.Harness import Reports
from bs4 import UnicodeDammit
from LaBSKApi.web import get_all_descs
from LaBSKApi.MongoDB import MongoDB
from LaBSKApi.reports import ReportBuilder, PreGeneratedReports
from presenter.GUIModel import Text
from datetime import datetime

def write(filename, html):
    with open(filename, 'w') as file:
        file.write(html.encode('utf8'))


db = MongoDB(col="labsk_merge")
#db = MockMongo()

starttime = datetime.now()

builder = ReportBuilder(db)
text = Text()

env = Environment(loader=FileSystemLoader('../webgui/templates'))
template = env.get_template("_static_report.html")


report = builder.build_report(PreGeneratedReports.report_asylum_games)
# No funciona
#text.change_newline_in_report(PreGeneratedReports.report_asylum_games['keywords'], report)
#post_report = report
xhtml = template.render(keywords = Reports.asylum_keywords,
                        report = report,
                        links = get_all_descs(),
                        last_update = "24/02/2014 16:30")

html = UnicodeDammit(xhtml).unicode_markup
write('../webgui/templates/static_asylum_games.html', html)



report = builder.build_report(PreGeneratedReports.report_devir)
# No funciona
text.change_newline_in_report(PreGeneratedReports.report_devir['keywords'], report)
xhtml = template.render(keywords = ['Devir'],
                        report = report,
                        links = get_all_descs(),
                        last_update = "24/02/2014 16:30")

html = UnicodeDammit(xhtml).unicode_markup

write('../webgui/templates/static_devir.html', html)



