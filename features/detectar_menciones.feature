Feature: Detectar menciones en el listado de asuntos
	In order of XXXX


Scenario: Buscar menciones en el cuerpo del mensajes sin mirar titulo ni etiquetas o enlaces

given una pagina de mensajes LaBSK con un listado de mensajes del juego Fief
when quiero saber las menciones del juego "Fief" dentro de los mensajes
then el resultado es 2 mencion


Scenario: Leer lista de asuntos

given la pagina de noticias de LaBSK con un listado de asuntos (pagina "labsk_moticias.html")
  and con un mensaje que menciona en el titulo el juego "Sushi"
when detecto las menciones de "Sushi"
then el resultado es 1 mencion (en la primera pagina)


Scenario: Buscar menciones en el cuerpo del mensajes de dos paginas

given dos paginas de mensajes LaBSK con un listado de mensajes del juego Fief
when quiero saber las menciones del juego "Fief" dentro de los mensajes visitanfo ambas paginas
then el resultado es 4 menciones



