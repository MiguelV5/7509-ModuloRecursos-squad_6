# Backend Modulo Recursos TPG - [75.09] Analisis de la Informacion - Curso Villagra (1c2023)

---

<br>
<p align="center">
  <a href="#/"><img src="https://raw.githubusercontent.com/MiguelV5/MiguelV5/main/misc/logofiubatransparent_partialwhite.png" height="180"/></a>
</p>
<br>

---

## Squad 6

| Integrantes                                                         |
| ------------------------------------------------------------------- |
| [Mauricio Davico](https://github.com/mdavic0)                       |
| [Mateo Lardiez](https://github.com/Mateolardiez)                    |
| [Ramiro Gestoso](https://github.com/ramirogestoso)                  |
| [Manuel Dieguez](https://github.com/jmdieguez)                      |
| [Miguel Vasquez](https://github.com/MiguelV5)                       |


---

## Dependencias

Se puede realizar la instalación de los paquetes por medio de:

```bash
pip install -r requirements.txt
```

## Ejecución local

```bash
python3 -m uvicorn src.main:app --reload
```

## Implementación de API REST

Para la implementación de la API se utilizó el framework [FastAPI](https://fastapi.tiangolo.com/) para python.

## Despliegue    

Se desplegó en [Render](https://render.com/) junto con la base de datos SQLite (su uso viene con la instalación de sqlalchemy, por lo tanto en el despliegue solo se requiere 
solicitar el web service a Render).

La API está desplegada [aquí](https://rrhh-squad6-1c2023.onrender.com).

Para ver documentación de la misma se utiliza swagger. Se puede visualizar accediendo al [endpoint de docs](https://rrhh-squad6-1c2023.onrender.com/docs).

## Tests BDD

Se utlizó la libreria [behave](https://behave.readthedocs.io/en/latest/) para los tests de Gherkin en Python

Instalar librería behave:

```bash
pip install behave
```

***Nota: Los tests requieren que se esté ejecutando previamente la API de manera local.***

Para correr los tests singularmente, posicionarse en el directorio /test/features/ y ejecutar el siguiente comando en la consola:
```bash
behave <test>.feature
```

Alternativamente se pueden correr todos los tests a la vez, ejecutando desde la raíz del directorio:
```bash
behave test\features
```

## APIs externas con las que se interactua

- [Módulo de Proyectos](https://api-proyectos.onrender.com/projects) 
- [Sistema externo de recursos](https://anypoint.mulesoft.com/mocking/api/v1/sources/exchange/assets/754f50e8-20d8-4223-bbdc-56d50131d0ae/recursos-psa/1.0.0/m/api/recursos). 

Para realizar requests HTTP a APIs externas se usa la librería [requests](https://requests.readthedocs.io/en/latest/). 
Suele venir por defecto con la instalación de python.

