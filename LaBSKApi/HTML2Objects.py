__author__ = 'Javier'

from bs4 import UnicodeDammit, BeautifulSoup, Tag
from web import WebClient
from LaBSKApi.modelobjects import DateManager


class MsgFactory(object):

    def __init__(self, webclient=None):
        self.webclient = webclient
        self.soup = None
        self.soupfragment = None
        self.date_manager = DateManager()

    # Private method
    def createMsg(self, soupfragment):
        result = {"user": soupfragment.find('a').contents[0],
                    "date": self._get_date(soupfragment),
                    "body": self._build_msg(soupfragment),
                    "id": soupfragment.find('div', 'inner')['id']
        }
        return result

    def _get_date(self, soupfragment):
        """ If date is 'hoy' changes it for the actual date
        """
        date = soupfragment.find('div', 'smalltext').contents[2]
        if date == ' ':
            date = self.date_manager.hoy() + "," + soupfragment.find('div', 'smalltext').contents[4]
        return date

    def _build_msg(self, fullmsg):
        contents = fullmsg.find("div", "inner")
        return self._get_content_recursively(contents)

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

    def _get_content_recursively(self, bs):
        result = ""
        for c in bs.contents:
            if type(c) is not Tag:
                ud = UnicodeDammit(c)
                result += ud.unicode_markup + '\n'
            else:
                ud = UnicodeDammit(self._get_content_recursively(c))
                result += ud.unicode_markup
        return result


class MsgPageFactory(object):

    def create(self, thread, last_msg_id=None):
        if last_msg_id is None:
            return self._create_without_id(thread)
        if thread['link'].endswith(".0"):
            link = thread['link'][:-2]
        else:
            link = thread['link']
        url = link + "." + last_msg_id
        return MsgFactory(WebClient(url))

    def _create_without_id(self, thread):
        return MsgFactory(WebClient(thread['link']))


class AsuntoFactory(object):

    @staticmethod
    def createFromURLObject(urlobject):
        factory = AsuntoFactory(url=urlobject.url)
        factory.urlobject = urlobject
        return factory

    def __init__(self, webclient=None, url = None):
        self.urlobject = None
        self.webclient = webclient
        self.soupfragment = None
        if webclient is not None:
            self.soupfragment = BeautifulSoup(webclient.sourceCode())
        if url is not None:
            self.webclient = WebClient(url)
            #self.soupfragment = BeautifulSoup(self.webclient.sourceCode())

    # Untested
    def _getfield_info(self, soupfragment):
        info = soupfragment.find("td", "subject windowbg2")
        if info is None:
            # It is a closed thread
            info = soupfragment.find("td", "subject lockedbg2")
        if info is None:
            print "Unkwon HTML for url: ", self.webclient
        return info

    def _get_answer_and_viewa_fragment(self, soupfragment):
        fragment = soupfragment.find('td', 'stats windowbg')
        if fragment is None:
            fragment = soupfragment.find('td', 'stats stickybg')
        if fragment is None:
            fragment = soupfragment.find('td', 'stats lockedbg')
        return fragment

    def create(self, soupfragment):
        result = dict()
        field = self._getfield_info(soupfragment)
        title = ""
        result["link"] = ""
        result["answers"] = ""
        result["views"] = ""
        result["location"] = ""
        if self.urlobject is not None:
            result["location"] = self.urlobject.description()

        #result['location'] = self.webclient.get_url_desc()
        if field is not None:
            title = UnicodeDammit(field.a.contents[0]).unicode_markup
            result["link"] = field.a['href']
            fragment = self._get_answer_and_viewa_fragment(soupfragment)
            if fragment is not None:
                result["answers"] = self._get_number_from(fragment.contents[0].strip())
                result["views"] = self._get_number_from(fragment.contents[2].strip())
            else:
                print "No answer and view bloq identified in thread: ", result["link"]
                result["answers"] = -1
                result["views"] = -1

        result["title"] = title.strip()

        #result['next_url'] = _nextUrl(soupfragment)
        return result

    def append_if_valid(self, l, msg):
        if len(msg['link']) > 0:
            l.append(msg)

    def createListOfAsuntos(self, soupFragment=None):
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
            if content == ">>":
                return link['href']
        return ""

    def changeUrl(self, url):
        self.webclient.load(url)
        self.soupfragment = BeautifulSoup(self.webclient.sourceCode())

    def _get_number_from(self, txt):
        return txt.split(' ')[0]