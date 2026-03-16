
from .pez import Pez
class Tiburon(Pez):
    def __str__(self):
        return "Tiburón -> " + super().__str__()
