__author__ = 'Javier'

from bs4 import UnicodeDammit, BeautifulSoup

class LaBSKPage(object):
    def __init__(self, webclient):
        self.webclient = webclient
        self.soup = BeautifulSoup(webclient.sourceCode())
