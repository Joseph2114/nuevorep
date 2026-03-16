
from empleados.administrador import Administrador
from empleados.guardian import Guardian
from empleados.conserje import Conserje
from empleados.veterinario import Veterinario

from transportes.bicicleta import Bicicleta
from transportes.cuadraciclo import Cuadraciclo
from transportes.patineta import Patineta

from animales.reptil import Reptil
from animales.mamifero import Mamifero
from animales.ave import Ave
from animales.pez import Pez
from animales.anfibio import Anfibio

empleados = []
transportes = []
animales = []

def agregar_empleado():
    print("\n1. Administrador")
    print("2. Guardián")
    print("3. Conserje")
    print("4. Veterinario")
    op = input("Seleccione: ")

    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    salario = float(input("Salario: "))

    if op == "1":
        empleados.append(Administrador(nombre,edad,salario))
    elif op == "2":
        empleados.append(Guardian(nombre,edad,salario))
    elif op == "3":
        empleados.append(Conserje(nombre,edad,salario))
    elif op == "4":
        empleados.append(Veterinario(nombre,edad,salario))

def listar_empleados():
    for e in empleados:
        print(e)

def agregar_transporte():
    print("\n1. Bicicleta")
    print("2. Cuadraciclo")
    print("3. Patineta")
    op = input("Seleccione: ")

    marca = input("Marca: ")
    velocidad = input("Velocidad: ")

    if op == "1":
        transportes.append(Bicicleta(marca,velocidad))
    elif op == "2":
        transportes.append(Cuadraciclo(marca,velocidad))
    elif op == "3":
        transportes.append(Patineta(marca,velocidad))

def listar_transportes():
    for t in transportes:
        print(t)

def agregar_animal():
    print("\n1. Reptil")
    print("2. Mamífero")
    print("3. Ave")
    print("4. Pez")
    print("5. Anfibio")
    op = input("Seleccione: ")

    nombre = input("Nombre: ")
    edad = int(input("Edad: "))

    if op == "1":
        animales.append(Reptil(nombre,edad))
    elif op == "2":
        animales.append(Mamifero(nombre,edad))
    elif op == "3":
        animales.append(Ave(nombre,edad))
    elif op == "4":
        animales.append(Pez(nombre,edad))
    elif op == "5":
        animales.append(Anfibio(nombre,edad))

def listar_animales():
    for a in animales:
        print(a)

def menu():
    while True:
        print("\n--- ZOOLÓGICO ---")
        print("1. Agregar empleado")
        print("2. Listar empleados")
        print("3. Agregar transporte")
        print("4. Listar transportes")
        print("5. Agregar animal")
        print("6. Listar animales")
        print("7. Salir")

        op = input("Seleccione una opción: ")

        if op == "1":
            agregar_empleado()
        elif op == "2":
            listar_empleados()
        elif op == "3":
            agregar_transporte()
        elif op == "4":
            listar_transportes()
        elif op == "5":
            agregar_animal()
        elif op == "6":
            listar_animales()
        elif op == "7":
            break

if __name__ == "__main__":
    menu()
