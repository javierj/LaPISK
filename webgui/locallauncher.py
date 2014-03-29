__author__ = 'Javier'

from LaBSKApi.statistics import Statistics
from LaBSKApi.MongoDB import MongoDB
from LaBSKApi.reportstats import ReportStatsService
from presenter.ReportStatsPresenter import ReportStatsPresenter
import flaskweb

# Setup

#MONGODB_URI = os.environ['OPENSHIFT_MONGODB_DB_HOST']+":"+os.environ['OPENSHIFT_MONGODB_DB_PORT']
#connection_url = "mongodb://" + MONGODB_URI + "/"
db = MongoDB(col = 'stats')
flaskweb.set_stats_module(Statistics(db))
flaskweb.set_reportstats_module(ReportStatsPresenter(ReportStatsService(db)))
#app = flaskweb.create_app()
flaskweb.app.run()
