feature Detectar versiones dle juego

scenario Recuperar versiones de un juego

given El juego 'Fortuna' y ninguna editorial concreta
when el sistema recupera el n�mero d eusuarios que tienen una copia
then 2.000 usuarios poseen una copia (own) seg�n la BGG.

given El juego 'Fortuna' y la editorial 'Ludonova'
when el sistema recupera el n�mero de usuarios que tienen una copia
then 500 usuarios poseen una copia de Ludonova (own) seg�n la BGG.

given El juego 'Fortuna' y la editorial 'Ludonova'
when solicito la proporci�n de copias de 'Ludonova'
then 0.4 (40%) de las copias son de Ludonova.

/* 
	La valoraci�n de una versi�n se tiene en cuenta contando s�lo las 
   puntuaciones de esa versi�n concreta del juego 
*/
scenario Valoraci�n de versiones de un juego

given El juego 'Fortuna' y la editorial 'Ludonova'
when Solicito la puntuaci�n de esa versi�n del juego
then La media d epuntuaciones de esa veris�n concreto es de 6.5


feature Evoluci�n de un juego: own, whichlist, etc.
feature Eoluci�n de todos los juegos d euna editorial
feature Concoe rlos usuaros que quieren tu juego.
feature Usuarios que m�s y menos valoran tu juego
feature Valoraci�n y comentarios d eun juego por �rea geogr�fica.

( �Y si hago un volcado de datos de la BGG y hago el dataminning en modo local? 
  Puedo busar s�lo usuarios d enacionalidad espa�ola e ir actualiz�ndolos peri�dicamente.
  Lo malo es tener que estructurar la informaic�n si saber qu� voy a ahcer con ella. 
  Igual un NoSQL puede ayudarme si convierno el XML en JSon
)