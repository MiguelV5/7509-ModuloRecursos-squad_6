from pydantic import BaseModel
from typing import Union
import datetime


class RegistroDeHorasBase(BaseModel):
    cantidad: int
    fecha_de_registro: datetime.date
    id_proyecto: int
    id_tarea: int


class RegistroDeHorasCreate(RegistroDeHorasBase):
    pass


class RegistroDeHorasPatch(BaseModel):
    cantidad: Union[int, None] = None
    fecha_de_registro: Union[datetime.date, None] = None
    id_proyecto: Union[int, None] = None
    id_tarea: Union[int, None] = None


class RegistroDeHoras(RegistroDeHorasBase):
    legajo_recurso: int
    id: int

    class Config:
        orm_mode = True
