__author__ = 'Javier'

from LaBSKApi.web import RESTReader
from LaBSKApi.Process import VoidListener
from LaBSKApi.reports import ReportStats


class PlanetaLudicoScrap(object):

    def __init__(self, col):
        self._collection = col
        self._listener = VoidListener()

    def setListener(self, listener):
        self._listener = listener

    def scrapListOfURL(self, list_url):
        #list_entries = []
        for url in list_url:
            self._process_url(url)

    def _process_url(self, url):
        json_entries = self._read_entries(url)
        #print json_entries
        for json_entry in json_entries['results']['titles']:
            entry = self._build_entry(json_entry)
            self._save(entry)

    def _save(self, entry):
        old = self._collection.find_one('link', entry.link)
        if old is None:
            self._collection.save(entry.json())
        else:
            self._listener.skippingUnmodifiedThread(old, entry)

    def _read_entries(self, url_obj):
        return RESTReader.read(url_obj)

    def _build_entry(self, json_entry):
        entry = Entry(json_entry['title']['text'],
                      json_entry['date'],
                      json_entry['title']['href'],
                      json_entry['source']['text'])
        self._listener.enteringThread(entry)
        return entry


class Entry(object):

    def __init__(self, title, date, link, source):
        self._title = title
        self._date = date
        self._link = link
        self._source = source

    @property
    def title(self):
        return self._title

    @property
    def date(self):
        return self._date

    @property
    def link(self):
        return self._link

    @property
    def source(self):
        return self._source

    def json(self):
        return {'title': self._title, 'date': self._date, 'link': self._link, 'source': self._source}


######################################################################

class BlogEntry(object):
    """ Models a message from a blog.
    """

    def __init__(self, jsondoc):
        self._json = jsondoc

    def json(self):
        return self._json


class PlanetaLudicoReport(object):

    def __init__(self, builder = None):
        self._report_builder = builder

    def build_report(self, report_request, report, stats):
        """ This mehtods search for ocurrences of the key words y reporr reest in
        the information from PlanetaLudico blogs and tores them in report updatind stats object
        """
        report_result = self._report_builder.build_report(report_request)
        new_stats = ReportStats()
        for keyword in report_request['keywords']:
            for entry in report_result[keyword]:
                report[keyword].append(BlogEntry(entry))
            new_stats.inc_blogs(len(report_result[keyword]))
        #stats = self._generate_stats(report_request, report_result)
        # Merge stats
        stats.merge(new_stats)

"""
    def _generate_stats(self, report_request, report_result):
        stats =  ReportStats()
"""