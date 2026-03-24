
from .empleado import Empleado

class Veterinario(Empleado):
    def __str__(self):
        return "Veterinario -> " + super().__str__()
