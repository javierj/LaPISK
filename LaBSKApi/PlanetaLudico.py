__author__ = 'Javier'

from LaBSKApi.web import RESTReader
from LaBSKApi.Process import VoidListener

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
        return {'title':self._title, 'date':self._date, 'link':self._link, 'source':self._source}