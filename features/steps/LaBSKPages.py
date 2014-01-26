__author__ = 'Javier'

from bs4 import UnicodeDammit, BeautifulSoup
from bs4.element import Tag
from LaBSKApi.HTML2Objects import MsgFactory


class LaBSKPage(object):
    def __init__(self, webclient, pageslimit):
        self.webclient = webclient
        self.soup = BeautifulSoup(webclient.sourceCode())
        self.pageslimit = pageslimit
        self.pagecount = 0
        self.factory = MsgFactory()

    def search_next_page(self):
        for link in self.soup.find_all("a", "navPages"):
            content = str(link.contents[0])
            #print "Search: ", content
            if  content == ">>":
		        return link['href']
        return None

    def manage_next_page(self):
        nextlink = self.search_next_page()
        if nextlink == None:
            print "No more pages"
            return False
        print "Next page "
        self.load_new_page(nextlink)
        if (self.pagecount >= self.pageslimit):
            print "Page limit reached"
        return (self.pagecount < self.pageslimit)

    def load_new_page(self, nextlink):
        self.webclient.load(nextlink)
        self.soup = BeautifulSoup(self.webclient.sourceCode())
        self.pagecount += 1


class LaBSKMessagesPage(LaBSKPage):

    def __init__(self, webclient, pageslimit = 1):
        super(LaBSKMessagesPage, self).__init__(webclient, pageslimit)



    def count(self, word):
        report = []
        self.pagecount = 0
        morepages = True
        while morepages:
            #msgs = self.soup.find_all("div", "inner")
            msgs = self.soup.find_all("div", "post_wrapper")
            for msg in msgs:
                body = self.build_msg(msg)
                #print body
                #print "--------------------"
                if word in body:
                    self.add_to_report(report, msg, body)
            morepages = self.manage_next_page()
        return report


    def add_to_report(self, report, msg, body):
        line = self.factory.createMsg(msg, body)
        report.append(line)

    def build_msg(self, fullmsg):
        body = ""
        contents = fullmsg.find("div", "inner")
        for content in contents:
            if type(content) <> Tag:
                ud = UnicodeDammit(content)
                body = body + ud.unicode_markup
        return body


