"""
Feature: Modificar registros

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
"""

from behave import *
import utils
import requests
# from requests.exceptions import InvalidSchema

BASE_URL = "http://localhost:8000"

@when("elimino un registro de horas")
def step_impl(context):
    context.legajo = 1
    context.id = utils.cargar_registro(context.legajo).json()["id"]
    context.response = utils.eliminar_registro(context.legajo, context.id)


@then("el registro no existe mas")
def step_impl(context):
    response = requests.get(url=f"{BASE_URL}/recursos/{context.legajo}/registros/{context.id}")

    assert context.response.status_code == 200 and response.status_code == 404

@when("intento eliminar un registro inexistente para un legajo")
def step_impl(context):
    context.legajo = 1
    context.id = utils.cargar_registro(context.legajo).json()["id"]
    context.response = utils.eliminar_registro(context.legajo, context.id + 1)


@then("recibo un error de no existencia")
def step_impl(context):
    assert context.response.status_code == 404
