from behave import *
import utils
import requests
from datetime import date, timedelta
# from requests.exceptions import InvalidSchema

BASE_URL = "http://localhost:8000"


@when("hago alguna accion con un recurso no existente")
def step_impl(context):
    legajo = 99999
    context.response = requests.get(f"{BASE_URL}/recursos/{legajo}")


@when("hago alguna accion con un registro no existente")
def step_impl(context):
    legajo = 1
    registro = 99999
    context.response = requests.get(
        f"{BASE_URL}/recursos/{legajo}/registros/{registro}")


@when("a un registro le asigno una fecha futura")
def step_impl(context):
    legajo = 1
    fecha_futura = str(date.today() + timedelta(days=1))
    registro = {
        "cantidad": 2,
        "fecha_de_registro": fecha_futura,
        "id_proyecto": 1,
        "id_tarea": 1
    }
    context.response = requests.post(
        f"{BASE_URL}/recursos/{legajo}/registros", json=registro)


@when("a un registro le asigno un proyecto no existente")
def step_impl(context):
    legajo = 1
    registro = {
        "cantidad": 2,
        "fecha_de_registro": utils.random_date(),
        "id_proyecto": 9999,
        "id_tarea": 1
    }
    context.response = requests.post(
        f"{BASE_URL}/recursos/{legajo}/registros", json=registro)


@when("a un registro le asigno una tarea no existente")
def step_impl(context):
    legajo = 1
    registro = {
        "cantidad": 2,
        "fecha_de_registro": utils.random_date(),
        "id_proyecto": 1,
        "id_tarea": 9999
    }
    context.response = requests.post(
        f"{BASE_URL}/recursos/{legajo}/registros", json=registro)


@when("a un registro le asigno menos horas del minimo")
def step_impl(context):
    legajo = 1
    registro = {
        "cantidad": 0,
        "fecha_de_registro": utils.random_date(),
        "id_proyecto": 1,
        "id_tarea": 1
    }
    context.response = requests.post(
        f"{BASE_URL}/recursos/{legajo}/registros", json=registro)


@when("a un registro le asigno mas horas que el maximo")
def step_impl(context):
    legajo = 1
    registro = {
        "cantidad": 13,
        "fecha_de_registro": utils.random_date(),
        "id_proyecto": 1,
        "id_tarea": 1
    }
    context.response = requests.post(
        f"{BASE_URL}/recursos/{legajo}/registros", json=registro)


@when("a un registro le asigno mas horas que el maximo en una misma jornada")
def step_impl(context):
    legajo = 1
    registro = {
        "cantidad": 10,
        "fecha_de_registro": utils.random_date(),
        "id_proyecto": 1,
        "id_tarea": 1
    }
    requests.post(f"{BASE_URL}/recursos/{legajo}/registros", json=registro)

    registro["cantidad"] = 4
    context.response = requests.post(
        f"{BASE_URL}/recursos/{legajo}/registros", json=registro)


@when("consulto registros entre dos fechas y la fecha inicial es mayor a la final")
def step_impl(context):
    params = {
        "fechaInicio": "2020-07-30",
        "fechaFin": "2020-07-29"
    }
    context.response = requests.get(
        f"{BASE_URL}/recursos/registros", params=params)
