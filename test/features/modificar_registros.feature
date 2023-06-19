Feature: Modificar registros

        Como usuario quiero poder modificar un registro 
        de horas ya cargado para corregir datos en caso 
        de una carga con errores

    Scenario: Modificación satisfactoria
        Given soy un usuario
        When cargo un registro de horas
        Then puedo modificar datos como: cantidad de horas, fecha, proyecto y tarea

    Scenario: Modificación fallida
        Given soy un usuario
        When intento modificar un registro pero no informo ningún dato
        Then recibo un error