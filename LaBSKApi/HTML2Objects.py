__author__ = 'Javier'

from bs4 import UnicodeDammit, BeautifulSoup, Tag
from web import WebClient


class MsgFactory(object):

    def __init__(self, webclient=None):
        self.webclient = webclient
        self.soup = None

    # Private method
    def createMsg(self, soupfragment):
        result = {"user": soupfragment.find('a').contents[0],
                  "date": soupfragment.find('div', 'smalltext').contents[2],
                  "body": self._build_msg(soupfragment),
                  "id": soupfragment.find('div', 'inner')['id']
                 }
        return result

    def _build_msg(self, fullmsg):
        body = ""
        contents = fullmsg.find("div", "inner")
        for content in contents:
            if type(content) is not Tag:
                ud = UnicodeDammit(content)
                body = body + ud.unicode_markup + '\n'
        return body

    # Deprecated. dont cll his methid
    def create(self):
        soup = BeautifulSoup(self.webclient.sourceCode())
        return self.createMsg(soup)

    def createListOfMsgs(self):
        l = list()
        self.soup = BeautifulSoup(self.webclient.sourceCode())
        for msg in self.soup.find_all("div", "post_wrapper"):
            l.append(self.createMsg(msg))

        return l

    def nextUrl(self):
        for link in self.soup.find_all("a", "navPages"):
            content = str(link.contents[0])
            #print "Search: ", content
            if content == ">>":
                return link['href']
        return ""

    def changeUrl(self, url):
        self.webclient.load(url)
        self.soupfragment = BeautifulSoup(self.webclient.sourceCode())


class MsgPageFactory(object):

    def create(self, thread):
        return MsgFactory(WebClient(thread['link']))


class AsuntoFactory(object):

    @staticmethod
    def createFromURLObject(urlobject):
        factory = AsuntoFactory(url = urlobject.url)
        factory.urlobject = urlobject
        return factory

    def __init__(self, webclient=None, url = None):
        self.urlobject = None
        self.webclient = webclient
        self.soupfragment = None
        if webclient is not None:
            #print webclient.sourceCode()
            self.soupfragment = BeautifulSoup(webclient.sourceCode())
        if url is not None:
            self.webclient = WebClient(url)
            #self.soupfragment = BeautifulSoup(self.webclient.sourceCode())

    def create(self, soupfragment):
        result = dict()
        field = soupfragment.find("td", "subject windowbg2")
        title = ""
        result["link"] = ""
        result["answers"] = ""
        result["views"] = ""
        result["location"] = ""
        if self.urlobject is not None:
            result["location"] = self.urlobject.desc

        #result['location'] = self.webclient.get_url_desc()
        if field is not None:
            title = UnicodeDammit(field.a.contents[0]).unicode_markup
            result["link"] = soupfragment.find("td", "subject windowbg2").a['href']
            result["answers"] = self._get_number_from(soupfragment.find('td', 'stats windowbg').contents[0].strip())
            result["views"] = self._get_number_from(soupfragment.find('td', 'stats windowbg').contents[2].strip())
        result["title"]= title.strip()

        #result['next_url'] = _nextUrl(soupfragment)
        return result

    def append_if_valid(self, l, msg):
        if msg['link'] is not "":
            l.append(msg)

    def createListOfAsuntos(self, soupFragment = None):
        if soupFragment is None:
            if self.soupfragment is None:
                self.soupfragment = BeautifulSoup(self.webclient.sourceCode())
            soupFragment = self.soupfragment
        result = list()
        for asunto in soupFragment.find("table", "table_grid").tbody.find_all("tr"):
            self.append_if_valid(result, self.create(asunto))
        return result

    def nextUrl(self):
        for link in self.soupfragment.find_all("a", "navPages"):
            content = str(link.contents[0])
            #print "Search: ", content
            if  content == ">>":
		        return link['href']
        return ""

    def changeUrl(self, url):
        self.webclient.load(url)
        self.soupfragment = BeautifulSoup(self.webclient.sourceCode())

    def _get_number_from(self, txt):
        return txt.split(' ')[0]


