
class Empleado:
    """Clase padre que representa a un empleado del zoológico."""

    def __init__(self, nombre, edad, salario):
        self.__nombre = nombre
        self.__edad = edad
        self.__salario = salario

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

    @property
    def salario(self):
        return self.__salario

    @salario.setter
    def salario(self, valor):
        self.__salario = valor

    def __str__(self):
        return f"Nombre: {self.__nombre}, Edad: {self.__edad}, Salario: {self.__salario}"
