
from .empleado import Empleado

class Guardian(Empleado):
    def __str__(self):
        return "Guardián -> " + super().__str__()
