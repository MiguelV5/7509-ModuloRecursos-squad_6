"""
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

    Scenario: Asignar cantidad de horas adecuadas
        Given soy un usuario
        When cargo una cantidad de horas adecuadas
        Then la carga de horas es satisfactoria

    Scenario: Asignar horas negativas
        Given soy un usuario
        When cargo una cantidad de horas negativas
        Then recibo un error por carga de horas menor a cero
"""

from behave import *
from utils import random_date
import requests
from requests.exceptions import InvalidSchema
from src.lib.exceptions import *

BASE_URL = "http://localhost:8000"

@when("cargo una cantidad de horas trabajadas y no selecciono una tarea")
def step_impl(context):
    context.registro = {
        "cantidad": 2,
        "fecha_de_registro": random_date(),
        "id_proyecto": 1,
    }
    context.legajo = 1
    pass


@then("recibo un error por no seleccionar una tarea")
def step_impl(context):
    response = requests.post(
        url=f"{BASE_URL}/recursos/{context.legajo}/registros", json=context.registro
    )
    assert response.status_code == 422


@when("cargo una cantidad de horas trabajadas y selecciono una tarea")
def step_impl(context):
    context.registro = {
        "cantidad": 12,
        "fecha_de_registro": random_date(),
        "id_proyecto": 1,
        "id_tarea": 1,
    }
    context.legajo = 1
    pass


@then("la carga de horas a la tarea es satisfactoria")
def step_impl(context):
    response = requests.post(
        url=f"{BASE_URL}/recursos/{context.legajo}/registros", json=context.registro
    )
    json_response = response.json()

    assert response.status_code == 200 and json_response["id"] > 0      


@when("cargo una cantidad de horas excesiva")
def step_impl(context):
    context.registro = {
        "cantidad": 13,
        "fecha_de_registro": random_date(),
        "id_proyecto": 1,
        "id_tarea": 1,
    }
    context.legajo = 1
    pass


@then("recibo un error por exceso de horas")
def step_impl(context):
    response = requests.post(
        url=f"{BASE_URL}/recursos/{context.legajo}/registros", json=context.registro
    )

    assert response.status_code == 400


@when("cargo una cantidad de horas adecuadas")
def step_impl(context):
    context.registro = {
        "cantidad": 4,
        "fecha_de_registro": random_date(),
        "id_proyecto": 1,
        "id_tarea": 1,
    }
    context.legajo = 1
    pass


@then("la carga de horas es satisfactoria")
def step_impl(context):
    response = requests.post(
        url=f"{BASE_URL}/recursos/{context.legajo}/registros", json=context.registro
    )

    json_response = response.json()

    assert response.status_code == 200 and json_response["id"] > 0


@when("cargo una cantidad de horas negativas")
def step_impl(context):
    context.registro = {
        "cantidad": -2,
        "fecha_de_registro": random_date(),
        "id_proyecto": 1,
        "id_tarea": 1,
    }
    context.legajo = 1


@then("recibo un error por carga de horas menor a cero")
def step_impl(context):
    response = requests.post(
        url=f"{BASE_URL}/recursos/{context.legajo}/registros", json=context.registro
    )

    assert response.status_code == 400
