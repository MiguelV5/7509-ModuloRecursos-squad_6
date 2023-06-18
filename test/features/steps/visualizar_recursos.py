'''
Feature: Visualizar recursos

    Como usuario, quiero poder consultar todos los recursos
    disponibles para así realizar tareas sobre uno de ellos.

    Scenario: Ver recursos satisfactoriamente
        Given soy un usuario
        When cuando consulto los recursos y hay recursos disponibles
        Then puedo ver información de todos los recursos
'''

from behave import *
from src.lib import crud

@when('consulto los recursos y hay recursos disponibles')
def step_impl(context):
    context.recursos = crud.get_recursos_desde_endpoint()

@then('puedo ver información de todos los recursos')
def step_impl(context):
    assert len(context.recursos) != 0 