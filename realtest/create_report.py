__author__ = 'Javier'


# Creates an static report

from jinja2 import FileSystemLoader, Environment
from bs4 import UnicodeDammit
from LaBSKApi.web import get_all_descs
from LaBSKApi.MongoDB import MongoDB
from LaBSKApi.reports import ReportBuilder, PreGeneratedReports
from presenter.GUIModel import Text
from datetime import datetime


def write(filename, html_text):
    with open(filename, 'w') as template_file:
        template_file.write(html_text.encode('utf8'))


db = MongoDB(col="labsk_merge")

starttime = datetime.now()
builder = ReportBuilder(db)
text = Text()

env = Environment(loader=FileSystemLoader('../webgui/templates'))
template = env.get_template("_static_report.html")



def generate_report(name, report_schema):
    report = builder.build_report(report_schema)
    text.change_newline_in_report(report_schema['keywords'], report)
    xhtml = template.render(keywords=report_schema['keywords'],
                            report=report,
                            links=get_all_descs()
                            )

    html = UnicodeDammit(xhtml).unicode_markup

    write('../webgui/templates/static_'+name+'.html', html)


generate_report("asylum", PreGeneratedReports.report_asylum_games)
generate_report("devir", PreGeneratedReports.report_devir)
generate_report("moviles", PreGeneratedReports.report_moviles)
