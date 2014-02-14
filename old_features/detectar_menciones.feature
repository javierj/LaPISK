# Los : son obligatorios
Feature: Detectar menciones en el foro
	In order of XXXX


Scenario: Buscar menciones en el cuerpo del mensajes sin mirar titulo ni etiquetas o enlaces

given una pagina de mensajes LaBSK con un listado de mensajes del juego Fief
when quiero saber las menciones del juego "Fief" dentro de los mensajes
then el resultado es 2 mencion



Scenario: Buscar menciones en el cuerpo del mensajes de dos paginas

given dos paginas de mensajes LaBSK con un listado de mensajes del juego Fief
  and limite de 2 paginas
when quiero saber las menciones del juego "Fief" dentro de los mensajes visitanfo ambas paginas
then el resultado es 4 menciones


Scenario: Buscar menciones en el listado de asuntos (limite 1 por defecto)

given una pagina de mensajes LaBSK con 20 asuntos
  and uno de los asuntos menciona el juego Sushi
when quiero entrar en asuntos que no mencionen "Sushi"
then el resultado es 1 mencion (en la primera pagina)
then entro en 19 asuntos a buscar menciones



