from sqlalchemy.orm import Session
import requests
from datetime import date

from . import projects_requestor
from lib.exceptions import *
from .models import RegistroDeHoras
from . import schemas
from datetime import date


RECURSOS_ENDPOINT = "https://anypoint.mulesoft.com/mocking/api/v1/sources/exchange/assets/754f50e8-20d8-4223-bbdc-56d50131d0ae/recursos-psa/1.0.0/m/api/recursos"
MENSAJE_ROOT = "PSA API Recursos. Ver documentacion en /docs "

MAX_HORAS_A_REGISTRAR = 12
MIN_HORAS_A_REGISTRAR = 1
# REVISAR VALORES

# ========================= GET: =========================


def get_mensaje_root():
    return MENSAJE_ROOT


def get_recursos_desde_endpoint():
    return requests.get(RECURSOS_ENDPOINT).json()


def get_recurso_por_legajo_desde_endpoint(legajo: int):
    recursos = get_recursos_desde_endpoint()

    for r in recursos:
        if r["legajo"] == legajo:
            return r

    raise RecursoNoExistenteException(legajo)


def get_all_registros_desde_db(
    db: Session, fechaInicio: date | None = None, fechaFin: date | None = None
):
    if fechaFin is None or fechaFin > date.today():
        fechaFin = date.today()

    if fechaInicio is None:
        fechaInicio = date.min

    if fechaInicio > fechaFin:
        raise FechaInicialMayorAFinalException(fechaInicio, fechaFin)

    return (
        db.query(RegistroDeHoras)
        .filter(RegistroDeHoras.fecha_de_registro.between(fechaInicio, fechaFin))
        .order_by(RegistroDeHoras.fecha_de_registro)
        .all()
    )


def get_registro_por_legajo_desde_db(
    db: Session,
    legajo: int,
    fechaInicio: date | None = None,
    fechaFin: date | None = None,
):
    if fechaFin is None:
        fechaFin = date.today()

    if fechaInicio is None:
        fechaInicio = date.min

    if fechaInicio > fechaFin:
        raise FechaInicialMayorAFinalException(fechaInicio, fechaFin)

    return (
        db.query(RegistroDeHoras)
        .filter(RegistroDeHoras.legajo_recurso == legajo)
        .filter(RegistroDeHoras.fecha_de_registro.between(fechaInicio, fechaFin))
        .order_by(RegistroDeHoras.fecha_de_registro)
        .all()
    )


def get_registro(db: Session, legajo: int, idRegistro: int):
    recvd_registro = (
        db.query(RegistroDeHoras)
        .filter_by(legajo_recurso=legajo, id=idRegistro)
        .first()
    )
    if not recvd_registro:
        raise RegistroNoExistenteException(legajo, idRegistro)

    return recvd_registro


# ========================= POST: =========================


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


def _check_fecha_recibida_es_valida(recvd_registro: RegistroDeHoras):
    fecha_actual = date.today()
    if recvd_registro.fecha_de_registro > fecha_actual:
        raise FechaNoValidaException()


def _check_existencia_de_proyecto_y_tarea(recvd_registro: RegistroDeHoras):
    projects = projects_requestor.getProyectosList()
    if recvd_registro.id_proyecto not in _parse_projects_ids_to_list(projects):
        raise ProyectoNoExistenteException(recvd_registro.id_proyecto)
    elif recvd_registro.id_tarea not in _parse_tasks_ids_to_list(projects):
        raise TareaNoExistenteException(recvd_registro.id_tarea)


def _check_cantidad_de_horas_del_registro_recibido(recvd_registro: RegistroDeHoras):
    if recvd_registro.cantidad < MIN_HORAS_A_REGISTRAR:
        raise CantidadDeHorasNulasException()
    elif recvd_registro.cantidad > MAX_HORAS_A_REGISTRAR:
        raise CantidadDeHorasExcesivasException(MAX_HORAS_A_REGISTRAR)


def _check_total_cantidad_de_horas_en_fecha(
    recvd_registro: RegistroDeHoras, db: Session
):
    registros_misma_fecha: list = get_registro_por_legajo_desde_db(
        db,
        recvd_registro.legajo_recurso,
        recvd_registro.fecha_de_registro,
        recvd_registro.fecha_de_registro,
    )

    cantidad_total_de_horas_en_fecha = sum(
        registro.cantidad
        for registro in registros_misma_fecha
        if registro.id != recvd_registro.id
    )

    if (
        cantidad_total_de_horas_en_fecha + recvd_registro.cantidad
    ) > MAX_HORAS_A_REGISTRAR:
        raise CantidadDeHorasExcesivasEnJornadaException(
            recvd_registro.cantidad,
            recvd_registro.fecha_de_registro,
            cantidad_total_de_horas_en_fecha,
            MAX_HORAS_A_REGISTRAR,
        )


def _check_body_registro(recvd_registro: RegistroDeHoras, db: Session):
    _check_fecha_recibida_es_valida(recvd_registro)
    _check_cantidad_de_horas_del_registro_recibido(recvd_registro)
    _check_existencia_de_proyecto_y_tarea(recvd_registro)
    _check_total_cantidad_de_horas_en_fecha(recvd_registro, db)


def post_registro(db: Session, legajo: int, registro: schemas.RegistroDeHorasCreate):
    recvd_registro = RegistroDeHoras(**registro.dict(), legajo_recurso=legajo)

    _check_body_registro(recvd_registro, db)

    db.add(recvd_registro)
    db.commit()
    db.refresh(recvd_registro)
    return recvd_registro


def patch_registro(
    db: Session, legajo: int, idRegistro: int, registro: schemas.RegistroDeHorasPatch
):
    if not any(registro.dict().values()):
        raise RegistroVacioException(list(registro.dict().keys()))

    recvd_registro = get_registro(db, legajo, idRegistro)
    for key, value in registro.dict().items():
        if value is None:
            continue
        setattr(recvd_registro, key, value)

    _check_body_registro(recvd_registro, db)

    db.commit()
    db.refresh(recvd_registro)
    return recvd_registro


# ========================= DEL: =========================


def delete_registro(db: Session, legajo: int, idRegistro: int):
    recvd_registro = get_registro(db, legajo, idRegistro)
    db.delete(recvd_registro)
    db.commit()
    return recvd_registro
