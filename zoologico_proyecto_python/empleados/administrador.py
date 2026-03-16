
from .empleado import Empleado

class Administrador(Empleado):
    def __str__(self):
        return "Administrador -> " + super().__str__()
