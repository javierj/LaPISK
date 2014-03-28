Feature: generar seguimiento semanal de los informes
	In order of conocer la popularidad de un conjunto de temas sobre juegos de mesa.
	As a usuario del sistema
	I want to generar un inform que me muestre los hilos, mensajes y post de blogs de un determinado tema y como han variado a lo largo del tiempo


    Scenario: Estadisticas diarias de EDGE
		Given las estadisticas de lo que se habla cada dia
		When solicito las estadisticas del informe "Editorial EDGE Entertainment"
		Then el informe contiene informacion de la fecha "2014-3-26"
         And muestra "0" blogs, "324" asuntos y "1207" mensajes
         And muestra un incemento de "0" blogs, "0" asuntos y "0" mensajes
