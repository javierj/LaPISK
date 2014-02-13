__author__ = 'Javier'

from bs4 import UnicodeDammit, BeautifulSoup, Tag
from web import WebClient


class MsgFactory(object):

    def __init__(self, webclient=None):
        self.webclient = webclient
        self.soup = None

    # Private method
    def createMsg(self, soupfragment, body=""):
        result = {"user": soupfragment.find('a').contents[0],
                  "date": soupfragment.find('div', 'smalltext').contents[2],
                  "body": self._build_msg(soupfragment)
                 }
        return result

    def _build_msg(self, fullmsg):
        body = ""
        contents = fullmsg.find("div", "inner")
        for content in contents:
            if type(content) is not Tag:
                ud = UnicodeDammit(content)
                body = body + ud.unicode_markup
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
            if  content == ">>":
		        return link['href']
        return ""

    def changeUrl(self, url):
        self.webclient.load(url)
        self.soupfragment = BeautifulSoup(self.webclient.sourceCode())

class MsgPageFactory(object):

    def create(self, thread):
        return MsgFactory(WebClient(thread['link']))


class AsuntoFactory(object):

    def __init__(self, webclient=None):
        self.webclient = webclient
        if webclient is not None:
            #print webclient.sourceCode()
            self.soupfragment = BeautifulSoup(webclient.sourceCode())

    def create(self, soupfragment):
        result = dict()
        field = soupfragment.find("td", "subject windowbg2")
        title = ""
        link = ""
        if field <> None:
            title = UnicodeDammit(field.a.contents[0]).unicode_markup
            link = soupfragment.find("td", "subject windowbg2").a['href']

        result["title"]= title.strip()
        result["link"] = link
        #result['next_url'] = _nextUrl(soupfragment)

        return result

    def createListOfAsuntos(self, soupFragment = None):
        if soupFragment is None:
            soupFragment = self.soupfragment
        result = list()
        for asunto in soupFragment.find("table", "table_grid").tbody.find_all("tr"):
            result.append(self.create(asunto))
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


