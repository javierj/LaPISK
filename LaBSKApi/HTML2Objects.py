__author__ = 'Javier'

from bs4 import UnicodeDammit, BeautifulSoup

class MsgFactory(object):

    def createMsg(self, soupfragment, body = ""):
        result = {"user": soupfragment.find('a').contents[0],
                  "date": soupfragment.find('div', 'smalltext').contents[2],
                  "body": body
        }
        return result

class AsuntoFactory(object):

    def create(self, soupfragment):
        result = dict()
        field = soupfragment.find("td", "subject windowbg2")
        title = ""
        link = ""
        if field <> None:
            title = UnicodeDammit(field.a.contents[0]).unicode_markup
            link = soupfragment.find("td", "subject windowbg2").a['href']

        result["title"]= title
        result["link"] = link

        return result