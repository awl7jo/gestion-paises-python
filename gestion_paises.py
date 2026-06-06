from funciones_principales import *
import csv
import os

ARCHIVO_CSV = 'paises.csv'

# Validaciones

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
            

# Funciones de archivos
            
def cargar_paises():  #Lee el archivo CSV y devuelve una lista de diccionarios con los datos de cada país.#
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

def guardar_paises(paises):
    try:
        with open(ARCHIVO_CSV, 'w', encoding='utf-8', newline="") as archivo:
            campos = ['nombre', 'poblacion', 'superficie', 'continente']
            escritor = csv.DictWriter(archivo, fieldnames=campos)
            escritor.writeheader()
            escritor.writerows(paises)
            print('Datos guardados correctamente ')
    except PermissionError:
        print(f'Error, no tenes permisos para escribir en {ARCHIVO_CSV}')
    except Exception as e:
        print(f'Error inesperado al guardar: {e}')

# Funciones principales

def mostrar_paises(paises):

    print("\n=== LISTA DE PAÍSES ===")

    for pais in paises:

        print("----------------------------")
        print(f"Nombre: {pais['nombre']}")
        print(f"Población: {pais['poblacion']}")
        print(f"Superficie: {pais['superficie']} km²")
        print(f"Continente: {pais['continente']}")


def actualizar_datos_paises(paises):
    print("\n=== ACTUALIZAR PAIS ===")
    
    actualizar = pedir_texto("Ingrese el pais a actualizar: ")
    for pais in paises:
        if pais["nombre"].lower() == actualizar.lower():
            nueva_poblacion = pedir_entero("Ingrese la nueva población: ")
            nueva_superficie = pedir_entero("Defina la nueva superficie: ")
            pais["poblacion"] = nueva_poblacion
            pais["superficie"] = nueva_superficie
            
            guardar_paises(paises)
            print("Datos actualizados con exito")
            return
    print("Pais no encontrado")
    
def buscar_pais(paises):
    print("\n=== BUSCAR PAIS ===")
    buscar = pedir_texto("Ingrese el  nombre del pais o parte del nombre: ")
    encontrados = []
    for pais in paises:
        if buscar.lower() in pais["nombre"].lower():
            encontrados.append(pais)
    if len(encontrados) == 0:
        print("No se encontraron resultados.")
        return
    mostrar_paises(encontrados)
    
    

