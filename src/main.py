from fastapi import FastAPI, HTTPException, Request, Depends

from . import crud, schemas, models
from .database import SessionLocal, engine

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


@app.get("/")
def root(request: Request):
    return crud.get_mensaje_root()


@app.get("/recursos/")
def getRecursos():
    return crud.get_recursos()


@app.get("/recursos/{legajo}")
def getRecursosPorLegajo(legajo: int):
    recurso = crud.get_recurso_por_legajo(legajo)

    if not recurso:
        raise HTTPException(status_code=404, detail="Recurso no encontrado")

    return recurso


@app.get("/recursos/{legajo}/registros/")
def getRegistrosDeHoras(legajo: int, db: Session = Depends(get_db)):
    return crud.get_registros(db=db, legajo=legajo)


@app.post("/recursos/{legajo}/registros/", response_model=schemas.RegistroDeHoras)
def postRegistroDeHoras(legajo: int, registro: schemas.RegistroDeHorasCreate, db: Session = Depends(get_db)):
    return crud.post_registro(db=db, legajo=legajo, registro=registro)

# OBTENCION DE DATOS DE PROYECTOS (LA IDEA ES CONSUMIRLO ASI)


@app.get("/proyectos")
def getProyectos():
    proyectos = [
        {
            "id": 1,
            "nombre": "Proyecto 1",
            "fecha_inicio": "2023-06-07",
            "fecha_finalizacion": "2023-08-07"
        }, {
            "id": 2,
            "nombre": "Proyecto 2",
            "fecha_inicio": "2023-04-01",
            "fecha_finalizacion": "2023-10-31"
        }, {
            "id": 3,
            "nombre": "Proyecto 3",
            "fecha_inicio": "2023-01-01",
            "fecha_finalizacion": "2023-12-31"
        }]
    return proyectos


@app.get("/proyectos/{id}")
def getProyectoPorId(id: int):
    for proyecto in getProyectos():
        if proyecto["id"] == id:
            return proyecto
    raise HTTPException(status_code=404, detail="Proyecto no encontrado")
