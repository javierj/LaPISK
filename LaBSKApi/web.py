from urllib2 import urlopen

__author__ = 'Javier'


class WebClient(object):

    def __init__(self, url):
        self.url = url

    def sourceCode(self):
        return urlopen(self.url)

    def load(self, url):
        self.url = url
