from fastapi import FastAPI, Depends, responses
from fastapi.middleware.cors import CORSMiddleware

from src.lib import crud, models
from typing import Union
from src.lib import schemas
from src.lib.database import SessionLocal, engine
from src.lib.exceptions import *
from src.metadata_params.metadata import FASTAPI_METADATA
from sqlalchemy.orm import Session
from datetime import date

models.Base.metadata.create_all(bind=engine)

app = FastAPI(**FASTAPI_METADATA)


# Define the allowed origins (frontend URLs for fetching)
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


PROYECTOS_BASE_URL = ""


@app.get("/", summary="Obtener mensaje root", tags=["Root"])
def getRoot():
    return crud.get_mensaje_root()


@app.get("/recursos", summary="Obtener recursos", tags=["Recursos"])
def getRecursos():
    return crud.get_recursos_desde_endpoint()


@app.get("/recursos/registros", summary="Obtener todos los registros de todos los recursos", tags=["Registros"])
def getTodosLosRegistrosDeHoras(
    db: Session = Depends(get_db),
    fechaInicio: Union[date, None] = None,
    fechaFin: Union[date, None] = None,
):
    return crud.get_all_registros_desde_db(
        db=db, fechaInicio=fechaInicio, fechaFin=fechaFin
    )


@app.get("/recursos/{legajo}", summary="Obtener recurso por legajo", tags=["Recursos"])
def getRecursosPorLegajo(legajo: int):
    return crud.get_recurso_por_legajo_desde_endpoint(legajo)


@app.get("/recursos/{legajo}/registros", summary="Obtener registros de un legajo", tags=["Registros"])
def getRegistrosDeHoras(
    legajo: int,
    db: Session = Depends(get_db),
    fechaInicio: Union[date, None] = None,
    fechaFin: Union[date, None] = None,
    idProyecto: Union[int, None] = None,
    idTarea: Union[int, None] = None
):
    return crud.get_registro_por_legajo_desde_db(
        db=db, legajo=legajo, fechaInicio=fechaInicio, fechaFin=fechaFin, idProyecto=idProyecto, idTarea=idTarea
    )


@app.post(
    "/recursos/{legajo}/registros",
    response_model=schemas.RegistroDeHoras,
    summary="Crear un registro de un legajo",
    tags=["Registros"],
)
def postRegistroDeHoras(
    legajo: int, registro: schemas.RegistroDeHorasCreate, db: Session = Depends(get_db)
):
    return crud.post_registro(db=db, legajo=legajo, registro=registro)


@app.get(
    "/recursos/{legajo}/registros/{idRegistro}",
    response_model=schemas.RegistroDeHoras,
    summary="Obtener un registro de un legajo",
    tags=["Registros"],
)
def getRegistroDeHoras(legajo: int, idRegistro: int, db: Session = Depends(get_db)):
    return crud.get_registro_por_id_desde_db(db=db, legajo=legajo, idRegistro=idRegistro)


@app.patch(
    "/recursos/{legajo}/registros/{idRegistro}",
    response_model=schemas.RegistroDeHoras,
    summary="Modificar un registro de un legajo",
    tags=["Registros"],
)
def patchRegistroDeHoras(
    legajo: int,
    idRegistro: int,
    registro: schemas.RegistroDeHorasPatch,
    db: Session = Depends(get_db),
):
    return crud.patch_registro(
        db, legajo=legajo, idRegistro=idRegistro, registro=registro
    )


@app.delete(
    "/recursos/{legajo}/registros/{idRegistro}",
    response_model=schemas.RegistroDeHoras,
    summary="Eliminar un registro de un legajo",
    tags=["Registros"],
)
def deleteRegistroDeHoras(legajo: int, idRegistro: int, db: Session = Depends(get_db)):
    return crud.delete_registro(db=db, legajo=legajo, idRegistro=idRegistro)


@app.exception_handler(Exception)
def validation_exception_handler(request, err):
    status_code = 400
    errs_404 = [
        ProyectoNoExistenteException,
        TareaNoExistenteException,
        RecursoNoExistenteException,
        RegistroNoExistenteException,
    ]
    if type(err) in errs_404:
        status_code = 404
    base_error_message = f"Failed to execute: {request.method}: {request.url}"
    return responses.JSONResponse(
        status_code=status_code,
        content={"message": f"{base_error_message}",
                 "detail": f"{err.message}"},
        headers={"Access-Control-Allow-Origin": "*"}
    )
