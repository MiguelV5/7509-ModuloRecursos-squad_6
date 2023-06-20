"""
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
"""

from behave import *
import utils
import requests
# from requests.exceptions import InvalidSchema

BASE_URL = "http://localhost:8000"


@when("cargo un registro de horas")
def step_impl(context):
    context.legajo = 1
    context.id = utils.cargar_registro(context.legajo).json()["id"]


@then("puedo modificar datos como: cantidad de horas, fecha, proyecto y tarea")
def step_impl(context):
    registro = {
        "cantidad": 3,
        "fecha_de_registro": utils.random_date(),
        "id_proyecto": 2,
        "id_tarea": 2
    }
    response = requests.patch(
        url=f"{BASE_URL}/recursos/{context.legajo}/registros/{context.id}", json=registro
    )
    assert response.status_code == 200


@when("intento modificar un registro pero no informo ningún dato")
def step_impl(context):
    legajo = 1
    id = utils.cargar_registro(legajo).json()["id"]
    registro = {}
    context.response = requests.patch(
        url=f"{BASE_URL}/recursos/{legajo}/registros/{id}", json=registro
    )
