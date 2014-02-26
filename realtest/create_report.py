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
from datetime import datetime


db = MongoDB(col="labsk_asylum_2")
#db = MockMongo()

starttime = datetime.now()

builder = ReportBuilder(db)

env = Environment(loader=FileSystemLoader('../webgui/templates'))
template = env.get_template("_static_report.html")


report = builder.build_report(PreGeneratedReports.report_asylum_games)

xhtml = template.render(keywords = Reports.asylum_keywords,
                        report = report,
                        links = get_all_descs(),
                        last_update = "24/02/2014 16:30")

html = UnicodeDammit(xhtml).unicode_markup
print html

with open('../webgui/templates/static_asylum_games.html', 'w') as file:
    file.write(html.encode('utf8'))


report = builder.build_report(PreGeneratedReports.report_devir)

xhtml = template.render(keywords = ['Devir'],
                        report = report,
                        links = get_all_descs(),
                        last_update = "24/02/2014 16:30")

html = UnicodeDammit(xhtml).unicode_markup
print html

with open('../webgui/templates/static_devir.html', 'w') as file:
    file.write(html.encode('utf8'))



