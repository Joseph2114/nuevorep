
from .anfibio import Anfibio
class Rana(Anfibio):
    def __str__(self):
        return "Rana -> " + super().__str__()
