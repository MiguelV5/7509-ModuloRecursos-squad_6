from fastapi import HTTPException, status
from sqlalchemy.orm import Session
import requests
from datetime import date

from . import projects_requestor

from . import models
from . import schemas

RECURSOS_ENDPOINT = "https://anypoint.mulesoft.com/mocking/api/v1/sources/exchange/assets/754f50e8-20d8-4223-bbdc-56d50131d0ae/recursos-psa/1.0.0/m/api/recursos"
MENSAJE_ROOT = 'PSA API Recursos. Ver documentacion en /docs '

MAX_HORAS_A_REGISTRAR = 12
MIN_HORAS_A_REGISTRAR = 1
# REVISAR VALORES


def get_mensaje_root():
    return MENSAJE_ROOT


def get_recursos_desde_endpoint():
    return requests.get(RECURSOS_ENDPOINT).json()


def get_recurso_por_legajo_desde_endpoint(legajo: int):
    recursos = get_recursos_desde_endpoint()

    for r in recursos:
        if r["legajo"] == legajo:
            return r

    return None


def get_all_registros_desde_db(db: Session):
    return db.query(models.RegistroDeHoras).all()


def get_registro_por_legajo_desde_db(db: Session, legajo: int):
    return db.query(models.RegistroDeHoras).filter(models.RegistroDeHoras.legajo_recurso == legajo).all()


# ========================= POST: =========================

def _generate_new_registro_id(db: Session):
    registros = get_all_registros_desde_db(db)
    prev_last_idx = -1
    if registros:
        return registros[prev_last_idx].id + 1
    else:
        return 1


def _parse_projects_ids_to_list(projects: list):
    projects_ids = []
    for p in projects:
        projects_ids.append(p["id"])
    return projects_ids


def _parse_tasks_ids_to_list(projects: list):
    tasks_ids = []
    for p in projects:
        for t in p["tareas"]:
            tasks_ids.append(t["id"])
    return tasks_ids


def _check_fecha_recibida_es_valida(recvd_registro: models.RegistroDeHoras):
    fecha_actual = date.today()
    if recvd_registro.fecha_de_registro > fecha_actual:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="La fecha ingresada no es válida, por favor ingrese una fecha del pasado"
        )


def _check_existencia_de_proyecto_y_tarea(recvd_registro: models.RegistroDeHoras):
    projects = projects_requestor.getProyectosList()
    if recvd_registro.id_proyecto not in _parse_projects_ids_to_list(projects):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=f"No existe el proyecto (id dada: {recvd_registro.id_proyecto}) al que se quiere registrar horas")
    elif recvd_registro.id_tarea not in _parse_tasks_ids_to_list(projects):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=f"No existe la tarea (id dada: {recvd_registro.id_tarea}) a la que se quieren registrar horas")


def _check_cantidad_de_horas_del_registro_recibido(recvd_registro: models.RegistroDeHoras):
    if recvd_registro.cantidad < MIN_HORAS_A_REGISTRAR:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Cantidad de horas no puede ser negativa o nula")  # REVISAR
    elif recvd_registro.cantidad > MAX_HORAS_A_REGISTRAR:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=f"Cantidad de horas no puede ser mayor a {MAX_HORAS_A_REGISTRAR}")


def _check_total_cantidad_de_horas_en_fecha(recvd_registro: models.RegistroDeHoras, db: Session):
    registros_filtrados_de_db: list = get_registro_por_legajo_desde_db(
        db, recvd_registro.legajo_recurso)

    lista_de_fechas_de_registros_filtrados = []
    for r in registros_filtrados_de_db:
        lista_de_fechas_de_registros_filtrados.append(r.fecha_de_registro)

    if recvd_registro.fecha_de_registro in lista_de_fechas_de_registros_filtrados:
        cantidad_total_de_horas_en_fecha = 0
        for r in registros_filtrados_de_db:
            if r.fecha_de_registro == recvd_registro.fecha_de_registro:
                cantidad_total_de_horas_en_fecha += r.cantidad

        if cantidad_total_de_horas_en_fecha >= MAX_HORAS_A_REGISTRAR:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail=f"Con la cantidad de horas a cargar dada (horas: {recvd_registro.cantidad}), el recurso tendría una cantidad excesiva de horas cargadas en la fecha (fecha: {recvd_registro.fecha_de_registro}, cantidad de horas cargadas previamente en la fecha: {cantidad_total_de_horas_en_fecha}, cantidad maxima de una fecha: {MAX_HORAS_A_REGISTRAR})"
            )


def _check_body_registro(recvd_registro: models.RegistroDeHoras, db: Session):

    _check_fecha_recibida_es_valida(recvd_registro)
    _check_cantidad_de_horas_del_registro_recibido(recvd_registro)
    _check_existencia_de_proyecto_y_tarea(recvd_registro)
    _check_total_cantidad_de_horas_en_fecha(recvd_registro, db)


def post_registro(db: Session, legajo: int, registro: schemas.RegistroDeHorasCreate):
    recvd_registro = models.RegistroDeHoras(
        **registro.dict(), legajo_recurso=legajo)

    _check_body_registro(recvd_registro, db)

    # Necesario para que el id sea autoincremental. Antes dejaba postear con id identica porque lo pediamos en el body de la request.
    recvd_registro.id = _generate_new_registro_id(db)
    db.add(recvd_registro)
    db.commit()
    db.refresh(recvd_registro)
    return recvd_registro
