

personas = []
mascotas = []
vehiculos = []


def mostrar_menu():
    print("\nMENU PRINCIPAL")
    print("1. Crear persona")
    print("2. Crear mascota")
    print("3. Crear vehiculo")
    print("4. Imprimir personas")
    print("5. Imprimir mascotas")
    print("6. Imprimir vehiculos")
    print("7. Imprimir todas las entidades")
    print("8. Salir")


def crear_persona():
    print("\n-- Crear Persona --")
    nombre = input("Nombre: ")
    edad = input("Edad: ")
    ocupacion = input("Ocupacion: ")
    estado_animo = input("Estado de animo: ")
    persona = Persona(nombre, edad, ocupacion, estado_animo)
    personas.append(persona)
    print("Persona creada correctamente.")


def crear_mascota():
    print("\n-- Crear Mascota --")
    nombre = input("Nombre: ")
    especie = input("Especie: ")
    raza = input("Raza: ")
    edad = input("Edad: ")
    mascota = Mascota(nombre, especie, raza, edad)
    mascotas.append(mascota)
    print("Mascota creada correctamente.")


def crear_vehiculo():
    print("\n-- Crear Vehiculo --")
    marca = input("Marca: ")
    modelo = input("Modelo: ")
    anio = input("Anio: ")
    color = input("Color: ")
    vehiculo = Vehiculo(marca, modelo, anio, color)
    vehiculos.append(vehiculo)
    print("Vehiculo creado correctamente.")


def imprimir_personas():
    print("\n-- Lista de Personas --")
    if not personas:
        print("No hay personas registradas.")
    else:
        for i, p in enumerate(personas, 1):
            print(f"\n[{i}]")
            print(p)


def imprimir_mascotas():
    print("\n-- Lista de Mascotas --")
    if not mascotas:
        print("No hay mascotas registradas.")
    else:
        for i, m in enumerate(mascotas, 1):
            print(f"\n[{i}]")
            print(m)


def imprimir_vehiculos():
    print("\n-- Lista de Vehiculos --")
    if not vehiculos:
        print("No hay vehiculos registrados.")
    else:
        for i, v in enumerate(vehiculos, 1):
            print(f"\n[{i}]")
            print(v)


def imprimir_todas():
    print("\n-- Todas las Entidades --")
    imprimir_personas()
    imprimir_mascotas()
    imprimir_vehiculos()


def main():
    while True:
        mostrar_menu()
        opcion = input("\nSeleccione una opcion: ")

        if opcion == "1":
            crear_persona()
        elif opcion == "2":
            crear_mascota()
        elif opcion == "3":
            crear_vehiculo()
        elif opcion == "4":
            imprimir_personas()
        elif opcion == "5":
            imprimir_mascotas()
        elif opcion == "6":
            imprimir_vehiculos()
        elif opcion == "7":
            imprimir_todas()
        elif opcion == "8":
            print("Saliendo del programa.")
            break
        else:
            print("Opcion no valida. Ingrese un numero del 1 al 8.")


if __name__ == "__main__":
    main()