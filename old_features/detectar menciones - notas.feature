feature Detectar menciones en el listado de mensajes

/*
No puedo acceder a esta página si no estpy registrado
*/
scenario Leer la página principal

given la página principal de LaBSK con un listado de mensajes (página 'labsk_moticias.html')
  and con un mensaje que menciona en el titulo el juego 'Sushi'
when detecto las menciones de 'Sushi'
then el resultado es 1 mencion (en la primera página)


scenario Cambiar de pagina de listado de asuntos

given la página principal de LaBSK con un listado de asuntos (página 'labsk_main.html')
and estoy en el principio de la pagina
when voy a la siguiente pagina del listado de mensajes
then veo los mensajes a partir del 20


feature Detectar menciones en el cuerpo del mensaje

scenario Entrar en mensajes

/*
Esta historia no funciona
*/
given una página de LaBSK con un listado de asuntos
when quiero saber las menciones de algo
then entro en el primer mensaje y luego en el siguiente


given una página de LaBSK con un listado de 10 asuntos
  and el juego 'Sushi' 
when quiero saber las menciones del juego dentro de los asuntos
then en 1 asunto hay 3 mensajes que contienen el juego 'Sushi'
/*
soup = BeautifulSoup(urlopen("http://labsk.net/index.php?topic=123067.0"))
for link in soup.find_all("a", "navPages"):
	content = str(link.contents[0])
	if  content == ">>":
		link

*/


/*
from bs4 import BeautifulSoup
from urllib2 import urlopen

soup = BeautifulSoup(urlopen("http://labsk.net/index.php?topic=119300.0"))
from bs4 import UnicodeDammit, BeautifulSoup
from bs4.element import Tag

msgs = soup.find_all("div", "inner")

for msg in msgs:
	ud = UnicodeDammit(msg.contents[0])
	text = ud.unicode_markup
	print text
	print "--------------------"

for msg in msgs:
	msg.contents[0]
	print "--------------------"

Si el ensaje empieza con un salto de linea no esta en cntens[0]

body = ""
for content in msgs[0].contents:
	if type(content) <> Tag:
		type(content)
		ud = UnicodeDammit(content)
		body = body + ud.unicode_markup
print body

Ojo, co etse codigo no encentor menciones en etiuetas como enlaces.


Ya funciona.

for msg in msgs:
	body = ""
	for content in msg.contents:
		if type(content) <> Tag:
			ud = UnicodeDammit(content)
			body = body + ud.unicode_markup
	print body
	print "--------------------"
	
*/

scenario ¿cómo llego a un mensaje y como entro?

scenario ¿cómo cmabio de página en los mensajes?

scenatio ¿cómo detecto una mención en un mensaje?

/*

soup = BeautifulSoup(urlopen("http://labsk.net/index.php?action=unread;all"))
Sólamente para usuarios registrados.

from urllib2 import urlopen

Novedades actualidad : http://labsk.net/index.php?board=18.0;sort=last_post;desc
soup = BeautifulSoup(urlopen("http://labsk.net/index.php?board=18.0;sort=last_post;desc"))

Si funciona.

Así busco la tabla de mensajes, pero no encuentra nada
soup.find("<table class=\"table_grid\" cellspacing=\"0\">")
soup.find_all("<table class=\"table_grid\" cellspacing=\"0\">")
soup.find_all("<table class=\"table_grid\"")
soup.find_all("table class=\"table_grid\"")
soup.find_all("table_grid")

Esta sí la encuentra.

soup.find_all("table", "table_grid")
Devuelve un ResultSet que, relamente, es una lista

Como elr eusltado solo tiene un elemento, esta línea hace lo mismo
soup.find("table", "table_grid")
 
soup.find("table", "table_grid").tbody

soup.find("table", "table_grid").tbody.find_all("tr")

soup.find("table", "table_grid").tbody.find_all("tr")[0].find("td", "subject windowbg2")

soup.find("table", "table_grid").tbody.find_all("tr")[0].find("td", "subject windowbg2").a

soup.find("table", "table_grid").tbody.find_all("tr")[0].find("td", "subject windowbg2").a..contents[0]


entra en uan recursividad infinita:

for line in soup.find("table", "table_grid").tbody.find_all("tr"):
	field = line.find("td", "subject windowbg2")
	if type(field) is not None:
		print field.a.contents[0]

for line in soup.find("table", "table_grid").tbody.find_all("tr"):
	field = line.find("td", "subject windowbg2")
	if type(field) <> None:
		print field.a.contents[0]

for line in soup.find("table", "table_grid").tbody.find_all("tr"):
	field = line.find("td", "subject windowbg2")
	if field <> None:
		print field.a.contents[0]
		
for line in soup.find("table", "table_grid").tbody.find_all("tr"):
	field = line.find("td", "subject windowbg2")
	print field.a.contents[0]

Sin el 0 si que funciona

for line in soup.find("table", "table_grid").tbody.find_all("tr"):
	field = line.find("td", "subject windowbg2")
	print field.a.contents

Sin el print tambien funciona.

for line in soup.find("table", "table_grid").tbody.find_all("tr"):
	field = line.find("td", "subject windowbg2")
	field.a.contents[0]

Funcionan las dos:

for line in soup.find("table", "table_grid").tbody.find_all("tr"):
	field = line.find("td", "subject windowbg2")
	if field <> None:
		print field.a.contents

for line in soup.find("table", "table_grid").tbody.find_all("tr"):
	field = line.find("td", "subject windowbg2")
	if field <> None:
		field.a.contents[0]
		
	
Esta si funciona pero al final da un erro porque s eencuentra un None

for line in soup.find("table", "table_grid").tbody.find_all("tr"):
	line.find("td", "subject windowbg2").a.contents[0]

El error que se encuentra es este:

Traceback (most recent call last):
  File "<pyshell#82>", line 2, in <module>
    line.find("td", "subject windowbg2").a.contents[0]
AttributeError: 'NoneType' object has no attribute 'a'


Error, ver más abajo:

for line in soup.find("table", "table_grid").tbody.find_all("tr"):
	field = line.find("td", "subject windowbg2")
	if field <> None:
		str(field.a.contents[0])

		Traceback (most recent call last):
  File "<pyshell#103>", line 4, in <module>
    str(field.a.contents[0])
UnicodeEncodeError: 'ascii' codec can't encode character u'\xf3' in position 28: ordinal not in range(128)


for line in soup.find("table", "table_grid").tbody.find_all("tr"):
	field = line.find("td", "subject windowbg2")
	if field <> None:
		field.a.contents[0].decode("utf-8")

Sale el mismo error:

Traceback (most recent call last):
  File "<pyshell#112>", line 4, in <module>
    field.a.contents[0].decode("utf-8")
  File "C:\code\apps\python2.7.3\lib\encodings\utf_8.py", line 16, in decode
    return codecs.utf_8_decode(input, errors, True)
UnicodeEncodeError: 'ascii' codec can't encode character u'\xf3' in position 28: ordinal not in range(128)


for line in soup.find("table", "table_grid").tbody.find_all("tr"):
	field = line.find("td", "subject windowbg2")
	if field <> None:
		field.a.contents[0].decode("cp1252")
		

		
Este código está perfecto !!!
		
from bs4 import UnicodeDammit

for line in soup.find("table", "table_grid").tbody.find_all("tr"):
	field = line.find("td", "subject windowbg2")
	if field <> None:
		ud = UnicodeDammit(field.a.contents[0])
		print ud.unicode_markup
*/


/*
for link in soup.find_all("a", "navPages"):
    link.contents[0]

	
fullmsg = soup.find_all("div", "post_wrapper")

Para cada msg en fullmsg este es el usuario
fullmsg.find('a').contents[0]

Y en esta URL s epuede encontrar su Id de usuario
fullmsg.find('a')['href']


Vwntana con la fecha del mensaje

fullmsg.find('div', 'smalltext')

Fecha y hora en un mismo texto:
fullmsg.find('div', 'smalltext').contents[2]

Resultado: u' 25 de Octubre de 2013, 12:12:00 pm \xbb'

el cuerpo:
fullmsg.find("div", "inner")


			*/
