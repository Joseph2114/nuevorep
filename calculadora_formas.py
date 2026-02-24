import numpy as np
print("Calculadora de Volumen de Figuras Geométricas")

def calcular_volumen_figura(figura):
    if figura == "cubo":
        lado = float(input("Ingrese la longitud del lado del cubo: "))
        volumen = lado ** 3
    elif figura == "esfera":
        radio = float(input("Ingrese el radio de la esfera: "))
        volumen = (4/3) * np.pi * radio ** 3
    elif figura == "cilindro":
        radio = float(input("Ingrese el radio de la base del cilindro: "))
        altura = float(input("Ingrese la altura del cilindro: "))
        volumen = np.pi * radio ** 2 * altura
    elif figura == "Parapalelepípedo":
        largo = float(input("Ingrese el largo del paralelepípedo: "))
        ancho = float(input("Ingrese el ancho del paralelepípedo: "))
        altura = float(input("Ingrese la altura del paralelepípedo: "))
        volumen = largo * ancho * altura
    elif figura == "cono":
        radio = float(input("Ingrese el radio de la base del cono: "))
        altura = float(input("Ingrese la altura del cono: "))
        volumen = (1/3) * np.pi * radio ** 2 * altura
    elif figura == "esfera":
        radio = float(input("Ingrese el radio de la esfera: "))
        volumen = (4/3) * np.pi * radio ** 3
    else:
        print("Figura no reconocida.")
        return None
    return volumen