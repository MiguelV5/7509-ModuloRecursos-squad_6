import requests
from requests.exceptions import Timeout, RequestException
from src.lib.exceptions import *

MAX_TIMEOUT = 120

GET_PROYECTOS_ENDPOINT = "https://api-proyectos.onrender.com/projects"


def getProyectosList():
    try:
        response = requests.get(GET_PROYECTOS_ENDPOINT, timeout=MAX_TIMEOUT)
        response.raise_for_status()  # Raise an exception for any non-successful status code
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
