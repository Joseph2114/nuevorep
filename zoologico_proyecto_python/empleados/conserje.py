
from .empleado import Empleado

class Conserje(Empleado):
    def __str__(self):
        return "Conserje -> " + super().__str__()
