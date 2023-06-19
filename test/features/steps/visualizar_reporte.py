'''
Feature: Visualizar reporte de un recurso

    Como usuario quiero visualizar todas las cargas de horas
    de un recurso para generar estadísticas

    Scenario: El recurso todavia no tiene carga de horas
        Given soy un usuario
        When selecciono para ver el reporte de un recurso y todavía no cargó horas en ninguna tarea
        Then recibo una lista vacia

    Scenario: El recruso tiene carga de horas
        Given soy un usuario
        When selecciono para ver el reporte de un recurso y ya tiene carga de horas en al menos una tarea
        Then recibo una lista de las cargas de horas del recurso
'''
from behave import *
import requests
import utils

BASE_URL = "http://localhost:8000"


@when('selecciono para ver el reporte de un recurso y todavía no cargó horas en ninguna tarea')
def step_impl(context):
    context.legajo = 2
    utils.borrar_cargas_de_horas(context.legajo)


@then('recibo una lista vacia')
def step_impl(context):
    url = f"{BASE_URL}/recursos/{context.legajo}/registros"
    response = requests.get(url)
    json_response = response.json()
    assert len(json_response) == 0


@when('selecciono para ver el reporte de un recurso y ya tiene carga de horas en al menos una tarea')
def step_impl(context):
    context.legajo = 2
    utils.cargar_horas(context.legajo)

@then('recibo una lista de las cargas de horas del recurso')
def step_impl(context):
    url = f"{BASE_URL}/recursos/{context.legajo}/registros"
    response = requests.get(url)
    json_response = response.json()
    assert len(json_response) > 0 
