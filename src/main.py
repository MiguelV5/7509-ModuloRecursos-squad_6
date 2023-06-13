from fastapi import FastAPI, HTTPException, Request, Depends, status

from lib import crud, models

from lib import schemas
from lib.database import SessionLocal, engine

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
    return crud.get_recursos_desde_endpoint()


@app.get("/recursos/{legajo}")
def getRecursosPorLegajo(legajo: int):
    recurso = crud.get_recurso_por_legajo_desde_endpoint(legajo)

    if not recurso:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Recurso no encontrado")

    return recurso


@app.get("/recursos/allRegistros/")
def getTodosLosRegistrosDeHoras(db: Session = Depends(get_db)):
    return crud.get_all_registros_desde_db(db=db)


@app.get("/recursos/{legajo}/registros/")
def getRegistrosDeHoras(legajo: int, db: Session = Depends(get_db)):
    return crud.get_registro_por_legajo_desde_db(db=db, legajo=legajo)


@app.post("/recursos/{legajo}/registro/", response_model=schemas.RegistroDeHoras)
def postRegistroDeHoras(legajo: int, registro: schemas.RegistroDeHorasCreate, db: Session = Depends(get_db)):
    return crud.post_registro(db=db, legajo=legajo, registro=registro)
