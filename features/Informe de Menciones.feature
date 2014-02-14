Feature: generar informe de menciones
	In order of concoer las menciones de un juego o editorial en LaBSK
	As a usuario anonimo del sistema
	I want to generar un informe con los hilos y mensajes y toda su informacion asociada donde aparaezcan las menciones


    Scenario: encontrar hilos que mencionan un juego
		Given Las noticias de LaBSK
		When solicito el informe del juego "EONS"
		Then el informe contiene el hilo "EONS, para los creadores de universos"

"""
	Scenario: encontrar mensajes que mencionan un juego
		given el informe de Lost Games que busca menciones del juego XX
		when obtengo el informe
		then obtengo el hilo "xxx" con 4 mensajes porque mencionan el juego


	Scenario: sin menciones del juego
		given Las noticias de LaBSK
		when solicito el informe de "Lost Games" y su juego "Castle Rising" 
		then el informe esta vacio
"""