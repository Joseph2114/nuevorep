
from .mamifero import Mamifero
class Leon(Mamifero):
    def __str__(self):
        return "León -> " + super().__str__()
