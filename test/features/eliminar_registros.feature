Feature: Eliminar registros

        Como usuario quiero poder eliminar un registro
        de horas ya cargado para corregir datos en caso de 
        una carga incorrecta

    Scenario: Eliminación satisfactoria
        Given soy un usuario
        When elimino un registro de horas
        Then el registro no existe mas

    Scenario: Eliminar registro no valido
        Given soy un usuario
        When intento eliminar un registro inexistente para un legajo
        Then recibo un error de no existencia