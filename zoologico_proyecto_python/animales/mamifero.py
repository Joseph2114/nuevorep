
from .animal import Animal
class Mamifero(Animal):
    def __str__(self):
        return "Mamífero -> " + super().__str__()
