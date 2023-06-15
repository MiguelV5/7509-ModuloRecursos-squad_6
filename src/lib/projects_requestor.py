from lib.exceptions import *

# revisar despues de que los de proyectos nos pasen la url
GET_PROYECTOS_ENDPOINT = "https://[placeholder_for_api_name].render.com/api/proyectos"


def getProyectosList():
    # communicate with the projects microservice api (its a render webservice api)
    # it would be something like:
    # return list(requests.get(PROYECTOS_BASE_URL).json())

    proyectos = [
        {
            "id": 1,
            "nombre": "Proyecto 1",
            "fecha_inicio": "2023-06-07",
            "fecha_finalizacion": "2023-08-07",
            "tareas": [
                {
                    "id": 1,
                    "nombre": "Tarea 1",
                    "fecha_inicio": "2023-06-07",
                    "fecha_finalizacion": "2023-06-14"
                },
                {
                    "id": 2,
                    "nombre": "Tarea 2",
                    "fecha_inicio": "2023-06-15",
                    "fecha_finalizacion": "2023-06-30"
                },
                {
                    "id": 3,
                    "nombre": "Tarea 3",
                    "fecha_inicio": "2023-07-01",
                    "fecha_finalizacion": "2023-07-15"
                }
            ]
        },
        {
            "id": 2,
            "nombre": "Proyecto 2",
            "fecha_inicio": "2023-04-01",
            "fecha_finalizacion": "2023-10-31",
            "tareas": [
                {
                    "id": 1,
                    "nombre": "Tarea 1",
                    "fecha_inicio": "2023-06-07",
                    "fecha_finalizacion": "2023-06-14"
                },
                {
                    "id": 2,
                    "nombre": "Tarea 2",
                    "fecha_inicio": "2023-06-15",
                    "fecha_finalizacion": "2023-06-30"
                },
                {
                    "id": 3,
                    "nombre": "Tarea 3",
                    "fecha_inicio": "2023-07-01",
                    "fecha_finalizacion": "2023-07-15"
                }
            ]
        },
        {
            "id": 3,
            "nombre": "Proyecto 3",
            "fecha_inicio": "2023-01-01",
            "fecha_finalizacion": "2023-12-31",
            "tareas": [
                {
                    "id": 1,
                    "nombre": "Tarea 1",
                    "fecha_inicio": "2023-06-07",
                    "fecha_finalizacion": "2023-06-14"
                },
                {
                    "id": 2,
                    "nombre": "Tarea 2",
                    "fecha_inicio": "2023-06-15",
                    "fecha_finalizacion": "2023-06-30"
                },
                {
                    "id": 3,
                    "nombre": "Tarea 3",
                    "fecha_inicio": "2023-07-01",
                    "fecha_finalizacion": "2023-07-15"
                }
            ]
        }
    ]
    return proyectos


def getProyectoPorId(id: int):
    for proyecto in getProyectosList():
        if proyecto["id"] == id:
            return proyecto
    raise ProyectoNoExistenteException(id)
