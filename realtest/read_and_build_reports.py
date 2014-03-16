__author__ = 'Javier'

from LaBSKApi.Process import ProcessThreads, VoidListener
from LaBSKApi.HTML2Objects import MsgPageFactory
from LaBSKApi.web import labsk_urls, get_all_descs
from jinja2 import FileSystemLoader, Environment
from bs4 import UnicodeDammit
from LaBSKApi.MongoDB import MongoDB
from LaBSKApi.reports import ReportBuilder, PreGeneratedReports
from presenter.GUIModel import Text
from presenter.ReportPresenter import ReportPresenter
from datetime import datetime


class StdListener(VoidListener):
    def __init__(self):
        self.msgs = 0
        self.urls = 0
        self.thread = 0
        self.skiped = 0

    # Override
    def enteringThread(self, obj_thread):
        print "Thread ", obj_thread.title(), ", ", obj_thread.answers(), " | ", obj_thread.link()
        self.thread += 1

    # Override
    def newMsg(self, user, body):
        #print "   ", user, ": ", body
        self.msgs += 1

    # Override
    def newURL(self, url):
        """ url is a web.URL object        """
        print "----------------------------------------------"
        print "---  ", url.desc, " ", url.url
        self.urls += 1

    # Override
    def skippingUnmodifiedThread(self, old, new):
        """ Old thread seems to be the same one than the new thread        """
        self.skiped += 1
        print old.answers(), "==", new.answers(), ". Skipping ", old.title(), " / ", old.link()

    def __str__(self):
        return "Urls: " + str(self.urls) + ". Threads: " + str(self.thread) + ". Messages readed: " + str(listener.msgs) + ". Threads skipped: " + str(self.skiped)


db = MongoDB()
db.query("labsk_merge")
db.insert("labsk_" + str(datetime.now()))

starttime = datetime.now()

listener = StdListener()
threads = ProcessThreads(db, MsgPageFactory())
threads.setListener(listener)
threads.setPageLimit(2)
threads.setMsgPageLimit(200)  # Nunca bajes este valor o perderas mensajes, al menos mantenlo igual

threads.scrapListOfURL(labsk_urls)
delta = datetime.now() - starttime

print "----------------------------------------------"
print "Total time: ", delta
print "Page limit ", threads.pagelimit, " Msg page limit ", threads.msgpagelimit
print str(listener)

mr = db.merge('link')
print str(mr)

#------------------------------------------------
# Build reports


def write(filename, html_text):
    with open(filename, 'w') as template_file:
        template_file.write(html_text.encode('utf8'))


starttime = datetime.now()
builder = ReportPresenter()
builder.set_builder(ReportBuilder(MongoDB(col="labsk_merge")))
text = Text()

env = Environment(loader=FileSystemLoader('../webgui/templates'))
template = env.get_template("_static_report.html")


def generate_report(name, report_schema, filter=None):
    result = builder.report_and_stats(report_schema, filter_year=filter)
    text.change_newline_in_report(report_schema['keywords'], result.report)
    xhtml = template.render(keywords=report_schema['keywords'],
                            report=result.report,
                            links=get_all_descs(),
                            stats=result.report_stats.get_text()
                            )

    #html = UnicodeDammit(xhtml).unicode_markup

    write('../webgui/templates/static_'+name+'.html', xhtml)


generate_report("asylum_games", PreGeneratedReports.report_asylum_games)
generate_report("devir", PreGeneratedReports.report_devir, '2013')
generate_report("tienda_planeton", PreGeneratedReports.tienda_planeton, '2013')
generate_report("tienda_100_doblones", PreGeneratedReports.tienda_100_doblones, '2013')
generate_report("tienda_zacatrus", PreGeneratedReports.tienda_zacatrus, '2013')
generate_report("tienda_finplay", PreGeneratedReports.tienda_finplay, '2013')
generate_report("tienda_tablerum", PreGeneratedReports.tienda_tablerum)
generate_report("tienda_evolution_goya", PreGeneratedReports.tienda_evolution_goya, '2013')
generate_report("tienda_dungeon_marvels", PreGeneratedReports.tienda_dungeon_marvels)
generate_report("tienda_mas_que_oca", PreGeneratedReports.tienda_mas_que_oca, '2013')
generate_report("tienda_click_and_rol", PreGeneratedReports.tienda_click_and_rol)
#generate_report("moviles", PreGeneratedReports.report_moviles)
