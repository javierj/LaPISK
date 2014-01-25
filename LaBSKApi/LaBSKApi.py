__author__ = 'Javier'

from bs4 import UnicodeDammit, BeautifulSoup
from bs4.element import Tag


class LaBSKMessagesPage:
    def __init__(self, source):
        self.soup = BeautifulSoup(source)
        print self.soup

    def count(self, word):
        count = 0
        msgs = self.soup.find_all("div", "inner")
        for msg in msgs:
            body = ""
            for content in msg.contents:
                if type(content) != Tag:
                    ud = UnicodeDammit(content)
                if ud.unicode_markup <> None:
                    body = body + ud.unicode_markup
                    print body
                    print "--------------------"
                    if word in body:
                        count = count + 1
        return 0


class LaBSKThreadListPage:
    def __init__(self, source):
        self.soup = BeautifulSoup(source)
        print self.soup

    def count(self, word):
        count = 0
        for line in self.soup.find("table", "table_grid").tbody.find_all("tr"):
            field = line.find("td", "subject windowbg2")
            if field <> None:
                ud = UnicodeDammit(field.a.contents[0])
                title = ud.unicode_markup
                print "LaBSKThreadListPage::count -- ", title
                if title != None:
                    if word in title:
                        count = count + 1
        return count