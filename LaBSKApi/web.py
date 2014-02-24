from urllib2 import urlopen

__author__ = 'Javier'



class URL(object):
    def __init__(self, url, desc):
        self.url = url
        self.desc = desc

class WebClient(object):

    def __init__(self, url):
        self.url = url

    def sourceCode(self):
        return urlopen(self.url)

    def load(self, url):
        self.url = url



labsk_urls = (URL("http://labsk.net/index.php?board=18.0;sort=last_post;desc", "Noticias"),
        URL("http://labsk.net/index.php?board=158.0;desc", "Juegos en los medios"),
        URL("http://labsk.net/index.php?board=11.0;desc", "Dudas de reglas"),
        URL("http://labsk.net/index.php?board=133.0;desc", "Compponentes y erratas"),
        URL("http://labsk.net/index.php?board=77.0;desc", "Resenyas escritas"),
        URL("http://labsk.net/index.php?board=20.0;desc", "Enlaces")
)

def get_all_descs():
    result = list()
    for url in labsk_urls:
        result.append(url.desc)
    return result