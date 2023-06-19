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

def cargar_registro(legajo):
    registro = {
        "cantidad": 2,
        "fecha_de_registro": utils.random_date(),
        "id_proyecto": 1,
        "id_tarea": 1
    }

    response = requests.post(
        url=f"{BASE_URL}/recursos/{legajo}/registros", json=registro
    )

    return response.json()["id"]

@when("cargo un registro de horas")
def step_impl(context):
    context.legajo = 1
    context.id = cargar_registro(context.legajo)


@then("puedo modificar datos como: cantidad de horas, fecha, proyecto y tarea")
def step_impl(context):
    registro = {
        "cantidad": 6,
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
    id = cargar_registro(legajo)
    registro = {}
    context.response = requests.patch(
        url=f"{BASE_URL}/recursos/{legajo}/registros/{id}", json=registro
    )

@then("recibo un error")
def step_impl(context):
    assert context.response.status_code == 400