Feature: obtener estadisticas dek uso de la aplicacion
	In order of concoer el uso del sistema por parte de los visitantes
    and validar o descartar hipotesis
	As propietario del sistema
	I want to obtner estadisticas del uso que uso que un visitante ha hecho del siste,a


    Scenario: tiempo en la pagina principal
		Given dado un visitante de la aplicacion
		When visita la pagina principal
         And son las '12:00' del '01/01/2013'
		Then las estadisticas me muestran la hora y el dia que visito la pagina

    Scenario: tiempo en la pagina de informes
		Given dado un visitante de la aplicacion
		When visita la pagina de informes
         And son las '12:05' del '01/01/2013'
		Then las estadisticas me muestran la hora y el dia que visito la pagina

    # Ya mas adelante porcesaremos esta informacion

    Scenario: informes consultados
		Given dado un visitante de la aplicacion
		When solicita el informe de 'Asylum-Games'
         And son las '12:05' del '01/01/2013'
		Then las estadisticas me muestran la hora y el dia que solicito el informe
         And las estadisticas memmuestra el informe de 'Asylum-Games'
         And las estadisticas me muestra el resultado del informe de 'Asylum-Games'
