import csv
import json

def leer_csv(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        lector_csv = csv.DictReader(archivo)
        datos = [fila for fila in lector_csv]
    return datos

def leer_json(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        datos = json.load(archivo)
    return datos

formato = input(("Elige el formato del archivo a leer (CSV/JSON): ")).upper()
print(" Escribe CSV para leer un archivo CSV o JSON para leer un archivo JSON.")

if formato == "CSV":
    print("Datos del archivo CSV:")
    datos_csv = leer_csv('datos.csv')
    print(datos_csv)
elif formato == "JSON":
    print("Datos del archivo JSON:")
    datos_json = leer_json('datos.json')
    print(datos_json)
else:
    print("Formato no válido. Por favor, elige CSV o JSON.")
