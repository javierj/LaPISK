Feature: generar informe de menciones
	In order of concoer las menciones de un juego o editorial en LaBSK
	As a usuario anonimo del sistema
	I want to generar un informe con los hilos y mensajes y toda su informacion asociada donde aparaezcan las menciones


    Scenario: encontrar hilos que mencionan un juego
		Given las noticias de LaBSK
		When solicito el informe del juego "EONS"
		Then el informe contiene el hilo "EONS, para los creadores de universos"

    Scenario: encontrar hilos que mencionan una editorial
		Given las noticias de LaBSK
		When solicito el informe de la editorial "MasQueOca"
		Then el informe contiene "2" hilos que la mencionan en el titulo
        And "2" hilos que la mencionan en un mensaje


	Scenario: encontrar mensajes que mencionan un juego
		Given las noticias de LaBSK
		When solicito el informe del juego "Grenadier"
		Then obtengo el hilo con enlace "http://labsk.net/index.php?topic=127181.0"
        And "1" mensaje del usuairo "Ech-Pi-El"

    Scenario: sin menciones del juego
		Given Las noticias de LaBSK
		When solicito el informe del juego "Castle Rising"
		Then el informe esta vacio

"""
	Scenario: encontrar mensajes que mencionan un juego
		Given las noticias de LaBSK
		When solicito el informe del juego "Mansiones"
		Then obtengo un hilo con "2" mensajes

    # AD&D no lo encuentra, no se por que


"""