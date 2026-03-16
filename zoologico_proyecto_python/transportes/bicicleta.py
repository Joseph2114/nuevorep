
from .transporte import Transporte

class Bicicleta(Transporte):
    def __str__(self):
        return "Bicicleta -> " + super().__str__()
