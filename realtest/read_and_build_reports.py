__author__ = 'Javier'

from LaBSKApi.Process import ProcessThreads
from LaBSKApi.HTML2Objects import MsgPageFactory, AsuntoFactory
from LaBSKApi.web import labsk_urls, get_all_descs
from jinja2 import FileSystemLoader, Environment
from tests.Harness import Reports
from bs4 import UnicodeDammit
from LaBSKApi.MongoDB import MongoDB
from LaBSKApi.reports import ReportBuilder, PreGeneratedReports
from presenter.GUIModel import Text
from datetime import datetime

class StdListener(object):
    def __init__(self):
        self.msgs = 0
        self.urls = 0
        self.thread = 0
        self.skiped = 0

    def enteringThread(self, obj_thread):
        print "Thread ", obj_thread.title(), ", ", obj_thread.answers(), " | ", obj_thread.link()
        self.thread += 1

    def msgsFound(self, count):
        pass

    def nectPage(self, pagecount):
        pass

    def noMorePagea(self):
        pass

    def limitReached(self):
        #print "Limit of pages"
        pass

    def newMsg(self, user, body):
        #print "   ", user, ": ", body
        self.msgs += 1

    def newURL(self, url):
        """ url is a web.URL object        """
        print "----------------------------------------------"
        print "---  ", url.desc, " ", url.url
        self.urls += 1

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
threads.setPageLimit(3)
threads.setMsgPageLimit(120) # Nunca bajes este valor o perderas mensajes, al menos mantenlo igual


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


generate_report("asylum_games", PreGeneratedReports.report_asylum_games)
generate_report("devir", PreGeneratedReports.report_devir)
generate_report("moviles", PreGeneratedReports.report_moviles)