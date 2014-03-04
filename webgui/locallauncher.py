__author__ = 'Javier'

from flaskweb import app as application
from LaBSKApi.statistics import Statistics
from LaBSKApi.MongoDB import MongoDB
import flaskweb

# Setup

#MONGODB_URI = os.environ['OPENSHIFT_MONGODB_DB_HOST']+":"+os.environ['OPENSHIFT_MONGODB_DB_PORT']
#connection_url = "mongodb://" + MONGODB_URI + "/"
db = MongoDB(col = 'stats')
flaskweb.set_stats_module(Statistics(db))
#app = flaskweb.create_app()
flaskweb.app.run()
