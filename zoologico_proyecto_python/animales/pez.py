
from .animal import Animal
class Pez(Animal):
    def __str__(self):
        return "Pez -> " + super().__str__()
