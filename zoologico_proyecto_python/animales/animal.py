
class Animal:
    """Clase padre que representa un animal del zoológico."""

    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        self.__nombre = valor

    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, valor):
        self.__edad = valor

    def __str__(self):
        return f"Nombre: {self.__nombre}, Edad: {self.__edad}"
