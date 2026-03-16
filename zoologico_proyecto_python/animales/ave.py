
from .animal import Animal
class Ave(Animal):
    def __str__(self):
        return "Ave -> " + super().__str__()
