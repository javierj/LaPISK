from bs4 import UnicodeDammit, BeautifulSoup
from LaBSKPage import LaBSKPage
from LaBSKPages import LaBSKMessagesPage
from LaBSKApi.web import WebClient


class LaBSKMessagesPageFactory(object):
    def create(self, url):
        return LaBSKMessagesPage(WebClient(url))
        #return None

class LaBSKThreadListPage(LaBSKPage):
    def __init__(self, webclient, msgpages_factory = LaBSKMessagesPageFactory()):
        super(LaBSKThreadListPage, self).__init__(webclient)
        self.msgpages_factory = msgpages_factory

    def count(self, word):
        count = 0
        for line in self.titles_table():
            field = line.find("td", "subject windowbg2")
            if self.title_contains_word(field, word):
                count += 1
            else:
                if field <> None:
                    url = self.getURLForThread(field)
                    page = self.msgpages_factory.create(url)
                    count += page.count(word)

        return count

    def titles_table(self):
        return self.soup.find("table", "table_grid").tbody.find_all("tr")

    def title_contains_word(self, field, word):
        if field <> None:
            ud = UnicodeDammit(field.a.contents[0])
            title = ud.unicode_markup
            #print "LaBSKThreadListPage::count -- ", ud.unicode_markup
            if word in title:
                return True
        return False

    def getURLForThread(self, field):
        #print type(field)
        return field.a['href']