class persona:
    def __init__(self, nombre, edad, ):  
        self.nombre = nombre
        self.edad = edad
    def mostrar(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}")
class mascota:
    def __init__(self, nombre, raza, edad):  
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
    def mostrar(self):
        print(f"Nombre: {self.nombre}, Raza: {self.raza}, Edad: {self.edad}")
class vehiculo:
    def __init__(self, marca, modelo, año):  
        self.marca = marca
        self.modelo = modelo
        self.año = año
    def mostrar(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Año: {self.año}")

