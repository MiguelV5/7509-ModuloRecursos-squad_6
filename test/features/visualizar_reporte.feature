Feature: Visualizar reporte de un recurso

    Como usuario quiero visualizar todas las cargas de horas
    de un recurso para generar estadísticas

    Scenario: El recurso todavia no tiene carga de horas
        Given soy un usuario
        When selecciono para ver el reporte de un recurso y todavía no cargó horas en ninguna tarea
        Then recibo una lista vacia

    Scenario: El recruso tiene carga de horas
        Given soy un usuario
        When selecciono para ver el reporte de un recurso y ya tiene carga de horas en al menos una tarea
        Then recibo una lista de las cargas de horas del recurso