from fastapi import FastAPI, Depends, responses

from lib import crud, models

from lib import schemas
from lib.database import SessionLocal, engine
from lib.exceptions import *
from sqlalchemy.orm import Session

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
# Dependency


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


PROYECTOS_BASE_URL = ""


@app.get("/", summary="Raíz")
def root():
    return crud.get_mensaje_root()


@app.get("/recursos", summary="Obtener recursos")
def getRecursos():
    return crud.get_recursos_desde_endpoint()


@app.get("/recursos/registros", summary="Obtener todos los registros")
def getTodosLosRegistrosDeHoras(db: Session = Depends(get_db)):
    return crud.get_all_registros_desde_db(db=db)


@app.get("/recursos/{legajo}", summary="Obtener recurso por legajo")
def getRecursosPorLegajo(legajo: int):
    return crud.get_recurso_por_legajo_desde_endpoint(legajo)


@app.get("/recursos/{legajo}/registros", summary="Obtener registros de un legajo")
def getRegistrosDeHoras(legajo: int, db: Session = Depends(get_db)):
    return crud.get_registro_por_legajo_desde_db(db=db, legajo=legajo)


@app.post("/recursos/{legajo}/registros", response_model=schemas.RegistroDeHoras, summary="Crear un registro de un legajo")
def postRegistroDeHoras(legajo: int, registro: schemas.RegistroDeHorasCreate, db: Session = Depends(get_db)):
    return crud.post_registro(db=db, legajo=legajo, registro=registro)


@app.get("/recursos/{legajo}/registros/{idRegistro}", response_model=schemas.RegistroDeHoras, summary="Obtener un registro de un legajo")
def getRegistroDeHoras(legajo: int, idRegistro: int, db: Session = Depends(get_db)):
    return crud.get_registro(db=db, legajo=legajo, idRegistro=idRegistro)


@app.delete("/recursos/{legajo}/registros/{idRegistro}", response_model=schemas.RegistroDeHoras, summary="Eliminar un registro de un legajo")
def deleteRegistroDeHoras(legajo: int, idRegistro: int, db: Session = Depends(get_db)):
    return crud.delete_registro(db=db, legajo=legajo, idRegistro=idRegistro)


@app.exception_handler(Exception)
def validation_exception_handler(request, err):
    status_code = 400
    errs_404 = [ProyectoNoExistenteException, TareaNoExistenteException,
                RecursoNoExistenteException, RegistroNoExistenteException]
    if type(err) in errs_404:
        status_code = 404
    base_error_message = f"Failed to execute: {request.method}: {request.url}"
    return responses.JSONResponse(status_code=status_code, content={"message": f"{base_error_message}", "detail": f"{err.message}"})
