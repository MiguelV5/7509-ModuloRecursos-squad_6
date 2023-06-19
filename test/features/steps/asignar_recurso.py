"""
Feature: Asignar horas de recurso a tareas

    Como usuario quiero poder seleccionar una cantidad de horas
    de una tarea de un proyecto para asignarlas a un recurso

    Scenario: Asignar horas sin tarea
        Given soy un usuario
        When cargo una cantidad de horas trabajadas y no selecciono una tarea
        Then recibo un error por no completar toda la informacion requerida

    Scenario: Asignar horas con tarea
        Given soy un usuario
        When cargo una cantidad de horas trabajadas y selecciono una tarea
        Then la carga de horas a la tarea es satisfactoria

    Scenario: Asignar demasiadas horas
        Given soy un usuario
        When cargo una cantidad de horas excesiva
        Then recibo un error

    Scenario: Asignar cantidad de horas adecuadas
        Given soy un usuario
        When cargo una cantidad de horas adecuadas
        Then la carga de horas es satisfactoria

    Scenario: Asignar horas negativas
        Given soy un usuario
        When cargo una cantidad de horas negativas
        Then recibo un error
"""

from behave import *
import utils
import requests
from src.lib.exceptions import *

BASE_URL = "http://localhost:8000"

@when("cargo una cantidad de horas trabajadas y no selecciono una tarea")
def step_impl(context):
    context.registro = {
        "cantidad": 2,
        "fecha_de_registro": utils.random_date(),
        "id_proyecto": 1,
    }
    context.legajo = 1
    context.response = requests.post(
        url=f"{BASE_URL}/recursos/{context.legajo}/registros", json=context.registro
    )


@when("cargo una cantidad de horas trabajadas y selecciono una tarea")
def step_impl(context):
    context.registro = {
        "cantidad": 12,
        "fecha_de_registro": utils.random_date(),
        "id_proyecto": 1,
        "id_tarea": 1,
    }
    context.legajo = 1
    context.response = requests.post(
        url=f"{BASE_URL}/recursos/{context.legajo}/registros", json=context.registro
    )



@then("la carga de horas a la tarea es satisfactoria")
def step_impl(context):
    json_response = context.response.json()

    assert context.response.status_code == 200 and json_response["id"] > 0      


@when("cargo una cantidad de horas excesiva")
def step_impl(context):
    context.registro = {
        "cantidad": 13,
        "fecha_de_registro": utils.random_date(),
        "id_proyecto": 1,
        "id_tarea": 1,
    }
    context.legajo = 1
    context.response = requests.post(
        url=f"{BASE_URL}/recursos/{context.legajo}/registros", json=context.registro
    )

@when("cargo una cantidad de horas adecuadas")
def step_impl(context):
    context.registro = {
        "cantidad": 4,
        "fecha_de_registro": utils.random_date(),
        "id_proyecto": 1,
        "id_tarea": 1,
    }
    context.legajo = 1
    context.response = requests.post(
        url=f"{BASE_URL}/recursos/{context.legajo}/registros", json=context.registro
    )



@then("la carga de horas es satisfactoria")
def step_impl(context):

    json_response = context.response.json()

    assert context.response.status_code == 200 and json_response["id"] > 0


@when("cargo una cantidad de horas negativas")
def step_impl(context):
    context.registro = {
        "cantidad": -2,
        "fecha_de_registro": utils.random_date(),
        "id_proyecto": 1,
        "id_tarea": 1,
    }
    context.legajo = 1
    context.response = requests.post(
        url=f"{BASE_URL}/recursos/{context.legajo}/registros", json=context.registro
    )
