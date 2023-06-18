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

@given('soy un usuario')
def step(context):
    pass

@when('consulto los recursos y hay recursos disponibles')
def step_consulto_recursos(context):
    context.recursos = crud.get_recursos_desde_endpoint()

@then('puedo ver información de todos los recursos')
def step_verificar_recursos(context):
    assert len(context.recursos) != 0 