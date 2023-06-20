from enum import auto

RECURSO_NO_EXISTE = auto()
REGISTRO_NO_EXISTE = auto()
FECHA_NO_VALIDA = auto()
PROYECTO_NO_EXISTE = auto()
TAREA_NO_EXISTE = auto()
CANTIDAD_HORAS_NULAS = auto()
CANTIDAD_HORAS_EXCESIVAS = auto()
CANTIDAD_HORAS_EXCESIVAS_EN_JORNADA = auto()
FECHA_INICIAL_MAYOR = auto()
REGISTRO_VACIO = auto()


class RecursoNoExistenteException(Exception):
    message = ""
    type = RECURSO_NO_EXISTE

    def __init__(self, id):
        self.message = f"Recurso no encontrado: {id}"


class RegistroNoExistenteException(Exception):
    message = ""
    type = REGISTRO_NO_EXISTE

    def __init__(self, idRecurso, id):
        self.message = f"Registro de recurso {idRecurso} no encontrado: {id}"


class FechaNoValidaException(Exception):
    message = ""
    type = FECHA_NO_VALIDA

    def __init__(self):
        self.message = (
            "La fecha ingresada no es válida, por favor ingrese la fecha hoy o del pasado"
        )


class ProyectoNoExistenteException(Exception):
    message = ""
    type = PROYECTO_NO_EXISTE

    def __init__(self, idProyecto):
        self.message = f"No existe el proyecto (id dada: {idProyecto}) al que se quiere registrar horas"


class TareaNoExistenteException(Exception):
    message = ""
    type = TAREA_NO_EXISTE

    def __init__(self, idTarea):
        self.message = f"No existe la tarea (id dada: {idTarea}) a la que se quieren registrar horas"


class CantidadDeHorasNulasException(Exception):
    message = ""
    type = CANTIDAD_HORAS_NULAS

    def __init__(self):
        self.message = "Cantidad de horas no puede ser negativa o nula"


class CantidadDeHorasExcesivasException(Exception):
    message = ""
    type = CANTIDAD_HORAS_EXCESIVAS

    def __init__(self, maxHoras):
        self.message = f"Cantidad de horas no puede ser mayor a {maxHoras}"


class CantidadDeHorasExcesivasEnJornadaException(Exception):
    message = ""
    type = CANTIDAD_HORAS_EXCESIVAS_EN_JORNADA

    def __init__(self, horasACargar, fecha, horasEnFecha, maxHoras):
        self.message = f"Con la cantidad de horas a cargar dada (horas: {horasACargar}), el recurso tendría una cantidad excesiva de horas cargadas en la fecha (fecha: {fecha}, cantidad de horas cargadas previamente en la fecha: {horasEnFecha}, cantidad maxima de una fecha: {maxHoras})"


class FechaInicialMayorAFinalException(Exception):
    message = ""
    type = FECHA_INICIAL_MAYOR

    def __init__(self, fechaInicio, fechaFinal):
        self.message = f"La fecha de inicio: {fechaInicio} debe ser menor o igual a la fecha final: {fechaFinal}"


class RegistroVacioException(Exception):
    message = ""
    type = REGISTRO_VACIO

    def __init__(self, camposModificables):
        self.message = f"Para modificar el registro debe indicar al menos un campo modificable: {camposModificables}"
