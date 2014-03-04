Feature: obtener estadisticas del uso de HootBoardGame
	In order of conocer el uso del sistema por parte de los visitantes
    and validar o descartar hipotesis sobre que funcionalidad es la mas demandada
	As propietario del sistema
	I want to obtener estadisticas del uso que un visitante hace de HootBoardGame


    Scenario: Visita de la pagina principal
		Given un visitante que accede a la pagina principal a las "12:00" del "01/01/2014"
		When obtengo las estadisticas
		Then veo una visita a "/" a la hora de la visita

    # El mismo escenario pero con la IP y con otras paginas

    Scenario: Visitante de la pagina principal
		Given un visitante que accede a la pagina principal con la IP "http://localhost/"
		When obtengo las estadisticas
		Then veo una visita a "/" desde la IP del visitante


    Scenario: Visitante administrador
		Given el administrador accede a la pagina principal con la IP "188.78.230.48"
		When obtengo las estadisticas
		Then no veo ninguna visita desde la IP del administrador


"""


    # Ya mas adelante porcesaremos esta informacion

    Scenario: informes consultados
		Given dado un visitante de la aplicacion
		When solicita el informe de 'Asylum-Games'
         And son las '12:05' del '01/01/2013'
		Then las estadisticas me muestran la hora y el dia que solicito el informe
         And las estadisticas memmuestra el informe de 'Asylum-Games'
         And las estadisticas me muestra el resultado del informe de 'Asylum-Games'
"""