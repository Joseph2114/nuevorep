
from .animal import Animal
class Anfibio(Animal):
    def __str__(self):
        return "Anfibio -> " + super().__str__()
