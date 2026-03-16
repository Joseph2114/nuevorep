
class Transporte:
    """Clase padre que representa un medio de transporte dentro del zoológico."""

    def __init__(self, marca, velocidad):
        self.__marca = marca
        self.__velocidad = velocidad

    @property
    def marca(self):
        return self.__marca

    @marca.setter
    def marca(self, valor):
        self.__marca = valor

    @property
    def velocidad(self):
        return self.__velocidad

    @velocidad.setter
    def velocidad(self, valor):
        self.__velocidad = valor

    def __str__(self):
        return f"Marca: {self.__marca}, Velocidad: {self.__velocidad}"
