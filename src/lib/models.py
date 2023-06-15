from sqlalchemy import Column, Integer, Date

from .database import Base


class RegistroDeHoras(Base):
    __tablename__ = "registro_de_horas"

    id = Column(Integer, primary_key=True, index=True)
    legajo_recurso = Column(Integer)
    cantidad = Column(Integer)
    fecha_de_registro = Column(Date)
    id_proyecto = Column(Integer)
    id_tarea = Column(Integer)
