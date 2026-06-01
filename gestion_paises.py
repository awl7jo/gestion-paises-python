from funciones_principales import *
import csv
import os
ARCHIVO_CSV = 'paises.csv'
def cargar_paises():
    paises = []

    try:
        with open(ARCHIVO_CSV, mode="r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)

            for fila in lector:
                try:
                    pais = {
                        "nombre": fila["nombre"],
                        "poblacion": int(fila["poblacion"]),
                        "superficie": int(fila["superficie"]),
                        "continente": fila["continente"]
                    }

                    paises.append(pais)

                except:
                    print("Error en una fila del CSV.")

    except FileNotFoundError:
        print("Archivo CSV no encontrado. Se creará uno nuevo.")

    return paises

def pedir_texto(mensaje):
    while True:
        texto = input(mensaje).strip()

        if texto != "":
            return texto

        print("No se permiten campos vacíos.")


def pedir_entero(mensaje):
    while True:
        try:
            numero = int(input(mensaje))

            if numero > 0:
                return numero

            print("Ingrese un número mayor a 0.")

        except:
            print("Debe ingresar un número válido.")