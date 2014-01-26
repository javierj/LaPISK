__author__ = 'Javier'

from bs4 import UnicodeDammit, BeautifulSoup
from bs4.element import Tag
from LaBSKPage import LaBSKPage


class LaBSKMessagesPage(LaBSKPage):
    def __init__(self, webclient):
        #LaBSKPage.__init__(self, webclient)
        super(LaBSKMessagesPage, self).__init__(webclient)
        #self.webclient = webclient
        #self.soup = BeautifulSoup(webclient.sourceCode())


    def count(self, word):
        count = 0
        morepages = True
        while morepages:
            msgs = self.soup.find_all("div", "inner")
            for msg in msgs:
                body = self.build_msg(msg.contents)
                #print body
                #print "--------------------"
                if word in body:
                    count = count + 1
            morepages = self.manage_next_page()

        return count

    def manage_next_page(self):
        nextlink = self.search_next_page()
        #print "Next link ", nextlink
        if nextlink == None:
            return False
        self.webclient.load(nextlink)
        self.soup = BeautifulSoup(self.webclient.sourceCode())
        return True

    def build_msg(self, contents):
        body = ""
        for content in contents:
            if type(content) <> Tag:
                ud = UnicodeDammit(content)
                body = body + ud.unicode_markup
        return body


    def search_next_page(self):
        for link in self.soup.find_all("a", "navPages"):
            content = str(link.contents[0])
            #print "Search: ", content
            if  content == ">>":
		        return link['href']
        return None