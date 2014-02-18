__author__ = 'Javier'

from LaBSKApi.Process import ProcessThreads
from LaBSKApi.MongoDB import MongoDB
from LaBSKApi.reports import ReportBuilder
from LaBSKApi.HTML2Objects import MsgPageFactory, AsuntoFactory
from tests.Harness import MockMongo
from datetime import datetime

db = MongoDB(col="labsk_asylum_2")
#db = MockMongo()

starttime = datetime.now()

informe = {'name': 'Informe de Asylum Games',
           'keywords': ["Asylum", "Polis", "Munities", "Banjooli"]}

builder = ReportBuilder(db)
report = builder.build_report(informe)

print report
print "Informe: "

for keyword in informe['keywords']:
    print "Keyword ", keyword
    threads = report[keyword]
    for thread in threads:
        print "Thread ", thread['title'], " URL:", thread['link']
        for msg in thread['msgs']:
            print msg['date'] \
                #, " / ", msg['url']
            print msg['body']
        print "----------------------"
    print " "


