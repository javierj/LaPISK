from urllib2 import urlopen

__author__ = 'Javier'


class URL(object):
    def __init__(self, url, desc):
        self.url = url
        self.desc = desc

    def description(self):
        """ Returns the description of the URL
        """
        return self.desc

    def __str__(self):
        return str(self.desc) + ", " + str(self.url)


class WebClient(object):

    def __init__(self, url):
        self.url = url

    def sourceCode(self):
        return urlopen(self.url)

    def load(self, url):
        self.url = url

    def __str__(self):
        return str(self.url)


labsk_msgs_per_page = 15
labsk_urls = (
        URL("http://labsk.net/index.php?board=18.0;sort=last_post;desc", "Novedades / Actualidad"),
        URL("http://labsk.net/index.php?board=19.0;desc", "Jornadas"),
        URL("http://labsk.net/index.php?board=158.0;desc", "Juegos de mesa en los medios"),
        URL("http://labsk.net/index.php?board=20.0;desc", "Enlaces"),
        URL("http://labsk.net/index.php?board=10.0;desc", "Reglamentos"),
        URL("http://labsk.net/index.php?board=41.0;desc", "Reglamentos / Traducciones en proceso"),

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
        URL("http://labsk.net/index.php?board=185.0;desc", "Recomendados / 10 juegos"),
        URL("http://labsk.net/index.php?board=144.0;desc", "Recomendados / Iniciacion"),
        URL("http://labsk.net/index.php?board=149.0;desc", "Recomendados / Tiendas on-line"),

        URL("http://labsk.net/index.php?board=27.0;desc", "Ezines"),
        URL("http://labsk.net/index.php?board=212.0;desc", "Podcasts"),
        URL("http://labsk.net/index.php?board=53.0;desc", "Juego del mes"),
        URL("http://labsk.net/index.php?board=207.0;desc", "Wargames"),

        URL("http://labsk.net/index.php?board=37.0;desc", "Humor grafico"),
        URL("http://labsk.net/index.php?board=61.0;desc", "Curiosidades"),
        URL("http://labsk.net/index.php?board=24.0;desc", "Pasatiempos"),
        URL("http://labsk.net/index.php?board=39.0;desc", "De jugon a jugon"),
        URL("http://labsk.net/index.php?board=199.0;desc", "Que os parece"),
        URL("http://labsk.net/index.php?board=204.0;desc", "Analizando a..."),
        URL("http://labsk.net/index.php?board=182.0;desc", "Ayudadme a elegir"),
        URL("http://labsk.net/index.php?board=23.0;desc", "BSK"),
        URL("http://labsk.net/index.php?board=159.0;desc", "Besequero de la semana"),
        URL("http://labsk.net/index.php?board=55.0;desc", "Sondeos"),
        URL("http://labsk.net/index.php?board=17.0;desc", "Quedadas"),
        URL("http://labsk.net/index.php?board=45.0;desc", "Quedadas en Madrid"),
        URL("http://labsk.net/index.php?board=46.0;desc", "Quedadas en Barcelona"),
        URL("http://labsk.net/index.php?board=57.0;desc", "Quedadas en Zaragoza"),

        URL("http://labsk.net/index.php?board=200.0;desc", "Quedadas en Sevilla"),

        URL("http://labsk.net/index.php?board=14.0;desc", "Jugar en Linea"),
        URL("http://labsk.net/index.php?board=153.0;desc", "Jugar en Linea / Juegos por software"),
        URL("http://labsk.net/index.php?board=154.0;desc", "Jugar en Linea / Juegos por web"),

        URL("http://labsk.net/index.php?board=92.0;desc", "Print and Play"),
        URL("http://labsk.net/index.php?board=90.0;desc", "Print and Play / Juegos descatalogados"),

        URL("http://labsk.net/index.php?board=40.0;desc", "Talleres"),
        URL("http://labsk.net/index.php?board=50.0;desc", "Talleres / Manualidades"),

        URL("http://labsk.net/index.php?board=47.0;desc", "Concurso"),

        URL("http://labsk.net/index.php?board=22.0;desc", "Compro-Vendo-Cambio"),
        URL("http://labsk.net/index.php?board=131.0;desc", "Mathtrade"),
        URL("http://labsk.net/index.php?board=171.0;desc", "Componentes y partes de juegos"),
        URL("http://labsk.net/index.php?board=193.0;desc", "Pintores, escultores y artistas"),

        URL("http://labsk.net/index.php?board=15.0;desc", "Consulta de compras en tiendas"),
        URL("http://labsk.net/index.php?board=2.0;desc", "Publicidad"),
        URL("http://labsk.net/index.php?board=71.0;desc", "Ofertas"),
        URL("http://labsk.net/index.php?board=179.0;desc", "Pedidos masivos y Preorders"),
        #URL("http://labsk.net/index.php?board=177.0;desc", "Valoraciones de tiendas"), -- Solo para usuarios registrados
        URL("http://labsk.net/index.php?board=178.0;desc", "Tiendas fisicas en el mundo"),

        URL("http://labsk.net/index.php?board=1.0;desc", "Cajon desastre")

)


def get_all_descs():
    result = list()
    for url in labsk_urls:
        result.append(url.desc)
    return result