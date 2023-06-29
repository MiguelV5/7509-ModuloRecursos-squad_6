import requests
from requests.exceptions import Timeout, RequestException
from src.lib.exceptions import *

# Se define un timeout de 6 minutos para la request considerando delay inicial de render para spin up de instancia
MAX_TIMEOUT = 360

GET_PROYECTOS_ENDPOINT = "https://api-proyectos.onrender.com/projects"


def getProyectosList():
    try:
        response = requests.get(GET_PROYECTOS_ENDPOINT, timeout=MAX_TIMEOUT)
        response.raise_for_status()
        return list(response.json())
    except Timeout:
        raise ExternalAPIException("Max Timeout reached")
    except RequestException as e:
        raise ExternalAPIException(f" {str(e)}")


def getProyectoPorId(id: int):
    for proyecto in getProyectosList():
        if proyecto["id"] == id:
            return proyecto
    raise ProyectoNoExistenteException(id)

def getTareasDeProyecto(id: int):
    try:
        response = requests.get(f"{GET_PROYECTOS_ENDPOINT}/{id}/tasks", timeout=MAX_TIMEOUT)
        response.raise_for_status()
        return list(response.json())
    except Timeout:
        raise ExternalAPIException("Max Timeout reached")
    except RequestException as e:
        raise ExternalAPIException(f" {str(e)}")