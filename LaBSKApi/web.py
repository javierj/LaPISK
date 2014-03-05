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


labsk_msgs_per_page = 15
labsk_urls = (
        URL("http://labsk.net/index.php?board=18.0;sort=last_post;desc", "Novedades / Actualidad"),
        URL("http://labsk.net/index.php?board=19.0;desc", "Jornadas"),
        URL("http://labsk.net/index.php?board=158.0;desc", "Juegos de mesa en los medios"),
        URL("http://labsk.net/index.php?board=4.0;desc", "Ayudas de juegos"),
        URL("http://labsk.net/index.php?board=5.0;desc", "Variantes"),
        URL("http://labsk.net/index.php?board=11.0;desc", "Dudas de reglas"),
        URL("http://labsk.net/index.php?board=133.0;desc", "Componentes y erratas"),
        URL("http://labsk.net/index.php?board=21.0;desc", "Software"),
        URL("http://labsk.net/index.php?board=25.0;desc", "Videojuegos"),
        URL("http://labsk.net/index.php?board=77.0;desc", "Resenyas escritas"),
        URL("http://labsk.net/index.php?board=69.0;desc", "Videoresenyas"),
        URL("http://labsk.net/index.php?board=78.0;desc", "Otras resenyas"),
        URL("http://labsk.net/index.php?board=62.0;desc", "Sesiones de juego"),
        URL("http://labsk.net/index.php?board=7.0;desc", "Divulgacion ludica"),
        URL("http://labsk.net/index.php?board=38.0;desc", "Recomendados"),
        URL("http://labsk.net/index.php?board=27.0;desc", "Ezines"),
        URL("http://labsk.net/index.php?board=212.0;desc", "Podcasts"),
        URL("http://labsk.net/index.php?board=53.0;desc", "Juego del mes"),
        URL("http://labsk.net/index.php?board=20.0;desc", "Enlaces")
)

def get_all_descs():
    result = list()
    for url in labsk_urls:
        result.append(url.desc)
    return result