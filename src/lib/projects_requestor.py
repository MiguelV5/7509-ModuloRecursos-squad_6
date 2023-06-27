import requests
from src.lib.exceptions import *

GET_PROYECTOS_ENDPOINT = "https://api-proyectos.onrender.com/projects"


def getProyectosList():
    return list(requests.get(GET_PROYECTOS_ENDPOINT).json())


def getProyectoPorId(id: int):
    for proyecto in getProyectosList():
        if proyecto["id"] == id:
            return proyecto
    raise ProyectoNoExistenteException(id)
