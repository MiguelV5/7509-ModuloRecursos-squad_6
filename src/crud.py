from sqlalchemy.orm import Session
from requests import get
from . import models, schemas

RECURSOS_ENDPOINT = "https://anypoint.mulesoft.com/mocking/api/v1/sources/exchange/assets/754f50e8-20d8-4223-bbdc-56d50131d0ae/recursos-psa/1.0.0/m/api/recursos"
MENSAJE_ROOT = 'PSA API Recursos. Ver documentacion en /docs '

def get_mensaje_root():
    return MENSAJE_ROOT

def get_recursos():
    return get(RECURSOS_ENDPOINT).json()


def get_recurso_por_legajo(legajo: int):
    recursos = get_recursos()

    for r in recursos:
        if r["legajo"] == legajo:
            return r

    return None

def get_registros(db: Session, legajo: int):
    return db.query(models.RegistroDeHoras).filter(models.RegistroDeHoras.legajo_recurso == legajo).all()

def post_registro(db: Session, legajo: int, registro: schemas.RegistroDeHorasCreate):
    #Agregar validaciones de que el proyecto exista, la tarea exista en el proyecto
    
    db_registro = models.RegistroDeHoras(**registro.dict(), legajo_recurso=legajo)
    db.add(db_registro)
    db.commit()
    db.refresh(db_registro)
    return db_registro
