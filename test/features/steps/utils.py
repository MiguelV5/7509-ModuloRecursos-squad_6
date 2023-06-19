from datetime import date, timedelta
import random
import requests

BASE_URL = "http://localhost:8000"


def random_date():
    start_date = date.min
    limit_date = date.today()
    delta_days = limit_date - start_date
    random_days = random.randint(0, delta_days.days)
    return str(start_date + timedelta(days=random_days))


def borrar_cargas_de_horas(legajo):
    url = f"{BASE_URL}/recursos/{legajo}/registros"
    response = requests.get(url)
    json_response = response.json()
    for registro in json_response:
        id = registro["id"]
        url_delete = f"{BASE_URL}/recursos/{legajo}/registros/{id}"
        requests.delete(url_delete)


def cargar_horas(legajo):
    url = f"{BASE_URL}/recursos/{legajo}/registros"
    for i in range(3):
        registro = {
            "cantidad": 2,
            "fecha_de_registro": random_date(),
            "id_proyecto": 1,
            "id_tarea": 1,
        }
        requests.post(url, json=registro)


def cargar_registro(legajo):
    registro = {
        "cantidad": 2,
        "fecha_de_registro": random_date(),
        "id_proyecto": 1,
        "id_tarea": 1,
    }

    return requests.post(
        url=f"{BASE_URL}/recursos/{legajo}/registros", json=registro
    )


def eliminar_registro(legajo, id):
    return requests.delete(url=f"{BASE_URL}/recursos/{legajo}/registros/{id}")

def get_recursos():
    url = f"{BASE_URL}/recursos"
    return requests.get(url)
