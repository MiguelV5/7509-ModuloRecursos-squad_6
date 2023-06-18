Feature: Asignar horas de recurso a tareas

    Como usuario quiero poder seleccionar una cantidad de horas
    de una tarea de un proyecto para asignarlas a un recurso

    Scenario: Asignar horas sin tarea
        Given soy un usuario
        When cargo una cantidad de horas trabajadas y no selecciono una tarea
        Then recibo un error por no seleccionar una tarea

    Scenario: Asignar horas con tarea
        Given soy un usuario
        When cargo una cantidad de horas trabajadas y selecciono una tarea
        Then la carga de horas a la tarea es satisfactoria

    Scenario: Asignar demasiadas horas
        Given soy un usuario
        When cargo una cantidad de horas excesiva
        Then recibo un error por exceso de horas

    # Scenario: Asignar cantidad de horas adecuadas
    #     Given soy un usuario
    #     When cargo una cantidad de horas adecuadas
    #     Then la carga de horas es satisfactoria

    # Scenario: Asignar horas negativas
    #     Given soy un usuario
    #     When cargo una cantidad de horas negativas
    #     Then recibo un error por carga de horas menor a cero