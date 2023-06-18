Feature: Visualizar recursos

    Como usuario, quiero poder consultar todos los recursos
    disponibles para así realizar tareas sobre uno de ellos.

    Scenario: Ver recursos satisfactoriamente
        Given soy un usuario
        When consulto los recursos y hay recursos disponibles
        Then puedo ver información de todos los recursos