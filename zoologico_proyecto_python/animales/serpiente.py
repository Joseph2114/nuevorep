
from .reptil import Reptil
class Serpiente(Reptil):
    def __str__(self):
        return "Serpiente -> " + super().__str__()
