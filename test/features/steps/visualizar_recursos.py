'''
Feature: Visualizar recursos

    Como usuario, quiero poder consultar todos los recursos
    disponibles para así realizar tareas sobre uno de ellos.

    Scenario: Ver recursos satisfactoriamente
        Given soy un usuario
        When cuando consulto los recursos y hay recursos disponibles
        Then recibo una lista de todos los recursos
'''

from behave import *
import utils


@when('consulto los recursos y hay recursos disponibles')
def step_impl(context):
    context.recursos = utils.get_recursos().json()


@then('recibo una lista de todos los recursos')
def step_impl(context):
    assert len(context.recursos) != 0
