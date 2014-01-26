from bs4 import UnicodeDammit, BeautifulSoup
from LaBSKPages import LaBSKMessagesPage, LaBSKPage
from LaBSKApi.web import WebClient
from LaBSKApi.HTML2Objects import AsuntoFactory


class LaBSKMessagesPageFactory(object):
    def create(self, url):
        return LaBSKMessagesPage(WebClient(url))
        #return None

class LaBSKThreadListPage(LaBSKPage):
    def __init__(self, webclient, msgpages_factory = LaBSKMessagesPageFactory(), pageslimit = 1):
        super(LaBSKThreadListPage, self).__init__(webclient, pageslimit)
        self.msgpages_factory = msgpages_factory
        self.reportfactory = AsuntoFactory()

    def count(self, word):
        #count = 0
        report = []
        morepages = True
        while morepages:
            for line in self.titles_table():
                #field = line.find("td", "subject windowbg2")

                info = self.reportfactory.create(line)
                if word in info["title"]:
                #if self.title_contains_word(field, word):
                    #count += 1
                    report.append(info)
                    #add_thread_to_report(report, field)
                    print "Skipping ", info["title"] #self.getURLForThread(field)
                else:
                    info["msgs"] = self.count_in_new_page(info["link"], word)
                    # count += self.count_in_new_page(field, word)
                    if (len(info["msgs"]) > 0):
                        report.append(info)

            morepages = self.manage_next_page()
        return report

    def count_in_new_page(self, field, word):
        if field == None or field == "":
            return list()

        #url = self.getURLForThread(field)
        #print "Searching in ", url
        page = self.msgpages_factory.create(field)
        return page.count(word)

    def titles_table(self):
        return self.soup.find("table", "table_grid").tbody.find_all("tr")

    def title_contains_word(self, field, word):
        if field <> None:
            ud = UnicodeDammit(field.a.contents[0])
            #title = ud.unicode_markup
            #print "LaBSKThreadListPage::count -- ", ud.unicode_markup
            if word in ud.unicode_markup:
                return True
        return False

    def getURLForThread(self, field):
        #print type(field)
        return field.a['href']