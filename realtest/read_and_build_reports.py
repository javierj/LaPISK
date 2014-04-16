__author__ = 'Javier'

from LaBSKApi.Process import ProcessThreads, VoidListener
from LaBSKApi.HTML2Objects import MsgPageFactory
from LaBSKApi.web import get_all_descs, planetaludico_urls, labsk_urls
from jinja2 import FileSystemLoader, Environment
from LaBSKApi.MongoDB import MongoDB
from LaBSKApi.reports import PreGeneratedReports, ReportService, FilteringServiceFactory, ReportBuilderServiceFactory
from presenter.GUIModel import Text
from presenter.ReportPresenter import ReportPresenter, ReportBuilderPresenter
from datetime import datetime
from LaBSKApi.PlanetaLudico import PlanetaLudicoScrap
import shutil
import threading


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
        return "Urls: " + str(self.urls) + ". Threads: " + str(self.thread) + ". Messages readed: " + str(self.msgs) + ". Threads skipped: " + str(self.skiped)


# combinar con la anterior
class BlogListener(VoidListener):
    def __init__(self):
        self.thread = 0

    # Override
    def enteringThread(self, obj_thread):
        print "Thread ", obj_thread.title, ", ", obj_thread.date, " | ", obj_thread.link
        self.thread += 1

    # Override
    def skippingUnmodifiedThread(self, old, new):
        """ Old thread seems to be the same one than the new thread        """
        self.thread -= 1
        print "Skipping ", new.title, ", ", new.date, " | ", new.link

    def __str__(self):
        return ". Threads: " + str(self.thread) \


db = MongoDB()
db.query("labsk_merge")
db.insert("labsk_" + str(datetime.now()))

starttime = datetime.now()

listener = StdListener()
threads = ProcessThreads(db, MsgPageFactory())
threads.setListener(listener)
threads.setPageLimit(1)
threads.setMsgPageLimit(250)  # Nunca bajes este valor o perderas mensajes, al menos mantenlo igual

threads.scrapListOfURL(labsk_urls)
delta = datetime.now() - starttime

print "----------------------------------------------"
print "Total time: ", delta
print "Page limit ", threads.pagelimit, " Msg page limit ", threads.msgpagelimit
print str(listener)

mr = db.merge('link')
print str(mr)


print "Scrapping planeta ludico"
blogs = PlanetaLudicoScrap(db.blogs_collection())
listener = BlogListener()
blogs.setListener(listener)
blogs.scrapListOfURL(planetaludico_urls)

print "----------------------------------------------"
print str(listener)

#------------------------------------------------
# Build reports

print "Building reports"


def write(name, html_text):
    path = '../webgui/templates/'
    filename = 'static_'+name+'.html'
    phorumledge_path = "C:/code/workspaces/Github/phorumledge/wsgi/templates/"
    print "Writing: ", path + filename
    with open(path + filename, 'w') as template_file:
        template_file.write(html_text.encode('utf8'))
    shutil.copyfile(path + filename, phorumledge_path + filename)


def create_builder():
    return ReportPresenter(ReportService(MongoDB(col="labsk_merge")))


def create_builder_new(filter_year):
    service = ReportBuilderServiceFactory.create_service_with_all_modules()
    if filter_year is not None:
        filter_service = FilteringServiceFactory.create_2_filters_same_year(filter_year)
        service.set_filter_service(filter_service)
    return ReportBuilderPresenter(service)


def generate_report(name, report_schema, filter_criterion=None):
    builder = create_builder()
    #builder = create_builder_new(filter_criterion)
    text = Text()
    env = Environment(loader=FileSystemLoader('../webgui/templates'))
    template = env.get_template("_static_report.html")
    result = builder.report_and_stats(report_schema, filter_year=filter_criterion)
    #result = builder.report_and_stats(report_schema)
    text.change_newline_in_report(report_schema['keywords'], result.report)
    xhtml = template.render(keywords=report_schema['keywords'],
                            report=result.report,
                            links=get_all_descs(),
                            stats=result.report_stats.get_text()
                            )
    write(name, xhtml)


# Multithread
def run_thread(name, report_schema, filter_threads=None):
    thread = threading.Thread(target=generate_report, args=(name, report_schema, filter_threads))
    thread.daemon = True
    thread.start()
    #thread.join()


run_thread("hootboardgame", PreGeneratedReports.report_hootboardgame)
run_thread("asylum_games", PreGeneratedReports.report_asylum_games)
run_thread("asmodee", PreGeneratedReports.report_asmodee, '2013')

#generate_report("morapiaf", PreGeneratedReports.report_morapiaf, '2013')
run_thread("morapiaf", PreGeneratedReports.report_morapiaf, '2013')

#run_thread("tienda_100_doblones", PreGeneratedReports.tienda_100_doblones, '2013')
#generate_report("tienda_zacatrus", PreGeneratedReports.tienda_zacatrus)
run_thread("tienda_zacatrus", PreGeneratedReports.tienda_zacatrus, '2013')
#generate_report("tienda_finplay", PreGeneratedReports.tienda_finplay, '2013')
run_thread("tienda_finplay", PreGeneratedReports.tienda_finplay, '2013')
#generate_report("tienda_tablerum", PreGeneratedReports.tienda_tablerum)
run_thread("tienda_tablerum", PreGeneratedReports.tienda_tablerum)
run_thread("tienda_demartina", PreGeneratedReports.tienda_demartina)

generate_report("tienda_evolution_goya", PreGeneratedReports.tienda_evolution_goya, '2013')
#generate_report("tienda_dungeon_marvels", PreGeneratedReports.tienda_dungeon_marvels)
generate_report("tienda_mas_que_oca", PreGeneratedReports.tienda_mas_que_oca, '2013')
generate_report("tienda_click_and_rol", PreGeneratedReports.tienda_click_and_rol)
#generate_report("moviles", PreGeneratedReports.report_moviles)
