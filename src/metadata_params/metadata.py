description = """
## Features

La API pone a disposición los siguientes endpoints *CRUD* principales:

- Obtener todos los recursos
- Obtener un recurso por legajo
- Obtener todos los registros de un recurso
- Obtener un registro de un recurso
- Crear un registro de un recurso
- Modificar un registro de un recurso
- Eliminar un registro de un recurso
"""


FASTAPI_METADATA = {
    "title": "PSA - Human Resources Module API",
    "description": description,
    "version": "0.1.0",
    "openapi_tags": [
        {
            "name": "Root",
            "description": "Obtención de información basica de la API",
        },
        {
            "name": "Recursos",
            "description": "Endpoints para obtener recursos",
        },
        {
            "name": "Registros",
            "description": "Endpoints para obtener, crear, modificar y eliminar registros",
        },
    ],
}
