
from .transporte import Transporte

class Cuadraciclo(Transporte):
    def __str__(self):
        return "Cuadraciclo -> " + super().__str__()
