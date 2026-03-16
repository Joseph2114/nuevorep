
from .transporte import Transporte

class Patineta(Transporte):
    def __str__(self):
        return "Patineta -> " + super().__str__()
