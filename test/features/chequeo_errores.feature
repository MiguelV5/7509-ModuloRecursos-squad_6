Feature: Chequear errores en aplicacion

    Distintos escenarios adicionales que devuelven errores
    al ejecutar ciertas acciones.
    Desde la interfaz de usuario se deben atrapar antes,
    pero definiendolas aca evitamos que se salten tal seguridad.

    Scenario: Recurso que no existe
        Given soy un usuario
        When hago alguna accion con un recurso no existente
        Then recibo un error de no existencia

    Scenario: Registro que no existe
        Given soy un usuario
        When hago alguna accion con un registro no existente
        Then recibo un error de no existencia

    Scenario: Registro con fecha no valida
        Given soy un usuario
        When a un registro le asigno una fecha futura
        Then recibo un error

    Scenario: Registro con proyecto que no existe
        Given soy un usuario
        When a un registro le asigno un proyecto no existente
        Then recibo un error de no existencia

    Scenario: Registro con tarea que no existe
        Given soy un usuario
        When a un registro le asigno una tarea no existente
        Then recibo un error de no existencia

    Scenario: Registro horas menos del mínimo
        Given soy un usuario
        When a un registro le asigno menos horas del minimo
        Then recibo un error

    Scenario: Registro horas más que el máximo
        Given soy un usuario
        When a un registro le asigno mas horas que el maximo
        Then recibo un error

    Scenario: Registro horas más que el máximo de jornada
        Given soy un usuario
        When a un registro le asigno mas horas que el maximo en una misma jornada
        Then recibo un error

    Scenario: Registro con fecha inicial mayor a la final
        Given soy un usuario
        When consulto registros entre dos fechas y la fecha inicial es mayor a la final
        Then recibo un error

    