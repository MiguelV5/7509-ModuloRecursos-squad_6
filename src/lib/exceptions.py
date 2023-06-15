class RecursoNoExistenteException(Exception):
    message = ""

    def __init__(self, id):
        self.message = f"Recurso no encontrado: {id}"


class RegistroNoExistenteException(Exception):
    message = ""

    def __init__(self, idRecurso, id):
        self.message = f"Registro de recurso {idRecurso} no encontrado: {id}"


class FechaNoValidaException(Exception):
    message = ""

    def __init__(self):
        self.message = "La fecha ingresada no es válida, por favor ingrese una fecha del pasado"


class ProyectoNoExistenteException(Exception):
    message = ""

    def __init__(self, idProyecto):
        self.message = f"No existe el proyecto (id dada: {idProyecto}) al que se quiere registrar horas"


class TareaNoExistenteException(Exception):
    message = ""

    def __init__(self, idTarea):
        self.message = f"No existe la tarea (id dada: {idTarea}) a la que se quieren registrar horas"


class CantidadDeHorasNulasException(Exception):
    message = ""

    def __init__(self):
        self.message = "Cantidad de horas no puede ser negativa o nula"


class CantidadDeHorasExcesivasException(Exception):
    message = ""

    def __init__(self, maxHoras):
        self.message = f"Cantidad de horas no puede ser mayor a {maxHoras}"


class CantidadDeHorasExcesivasEnJornadaException(Exception):
    message = ""

    def __init__(self, horasACargar, fecha, horasEnFecha, maxHoras):
        self.message = f"Con la cantidad de horas a cargar dada (horas: {horasACargar}), el recurso tendría una cantidad excesiva de horas cargadas en la fecha (fecha: {fecha}, cantidad de horas cargadas previamente en la fecha: {horasEnFecha}, cantidad maxima de una fecha: {maxHoras})"

class FechaInicialMayorAFinalException(Exception):
    message = ""

    def __init__(self, fechaInicio, fechaFinal):
        self.message = f"La fecha de inicio: {fechaInicio} debe ser menor o igual a la fecha final: {fechaFinal}"