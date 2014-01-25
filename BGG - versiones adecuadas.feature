feature Detectar versiones dle juego

scenario Recuperar versiones de un juego

given El juego 'Fortuna' y ninguna editorial concreta
when el sistema recupera el número d eusuarios que tienen una copia
then 2.000 usuarios poseen una copia (own) según la BGG.

given El juego 'Fortuna' y la editorial 'Ludonova'
when el sistema recupera el número de usuarios que tienen una copia
then 500 usuarios poseen una copia de Ludonova (own) según la BGG.

given El juego 'Fortuna' y la editorial 'Ludonova'
when solicito la proporción de copias de 'Ludonova'
then 0.4 (40%) de las copias son de Ludonova.

/* 
	La valoración de una versión se tiene en cuenta contando sólo las 
   puntuaciones de esa versión concreta del juego 
*/
scenario Valoración de versiones de un juego

given El juego 'Fortuna' y la editorial 'Ludonova'
when Solicito la puntuación de esa versión del juego
then La media d epuntuaciones de esa verisón concreto es de 6.5


feature Evolución de un juego: own, whichlist, etc.
feature Eolución de todos los juegos d euna editorial
feature Concoe rlos usuaros que quieren tu juego.
feature Usuarios que más y menos valoran tu juego
feature Valoración y comentarios d eun juego por área geográfica.

( ¿Y si hago un volcado de datos de la BGG y hago el dataminning en modo local? 
  Puedo busar sólo usuarios d enacionalidad española e ir actualizándolos periódicamente.
  Lo malo es tener que estructurar la informaicón si saber qué voy a ahcer con ella. 
  Igual un NoSQL puede ayudarme si convierno el XML en JSon
)