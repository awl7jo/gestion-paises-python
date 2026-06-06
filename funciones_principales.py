
from gestion_paises import *
from gestion_paises import ARCHIVO_CSV
import csv

def guardar_paises(paises): #Sobreescribe el archivo CSV con la lista de países actualizada.#
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
def agregar_pais(paises): #Pide los datos de un nuevo país al usuario, los valida y los agrega a la lista.
    print('\n----AGREGAR PAIS----')
    print("(escribi 'cancelar' para volver al menu)\n")
    while True:
        try:
            nombre = input("Nombre del pais: ").strip()
            if nombre.lower() == 'volver':
                print('Volviendo al menu principal...')
                return
            if not nombre:
                raise ValueError("El nombre no puede estar vacio")
            if not all(c.isalpha() or c.isspace() for c in nombre):
                raise ValueError("El nombre solo puede contener letras y espacios.")
            if buscar_exacto(paises, nombre) is not None:
                raise ValueError(f"Ya existe un pais llamado {nombre}")
            break
        except ValueError as e:
            print(f"Error, {e}")
    while True:
        try:
            entrada = input("Poblacion del pais: ").strip()
            if entrada.lower() == 'volver':
                print('Volviendo al menu principal...')
                return
            poblacion = int(entrada)
            if poblacion <= 0:
                raise ValueError("La poblacion debe ser mayor a 0.")
            break
        except ValueError as e:
            print(f"Error: {e}")
    while True:
        try:
            entrada = input("Superficie en km²: ").strip()
            if entrada.lower() == "cancelar":
                print("Operación cancelada.")
                return
            superficie = int(entrada)
            if superficie <= 0:
                raise ValueError("La superficie debe ser mayor a 0.")
            break
        except ValueError as e:
            print(f"Error: {e}")


    while True:
        try:
            continente = input("Continente: ").strip()
            if continente.lower() == 'volver':
                print('Volviendo al menu principal...')
                return
            if not continente:
                raise ValueError("El continente no puede estar vacio")
            if not all(c.isalpha() or c.isspace()for c in continente):
                raise ValueError('El continente solo puede contener letras y espacios')
            break
        except ValueError as e:
            print(f"Error, {e}")
    paises.append({
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    })
    guardar_paises(paises)
    print(f"País '{nombre}' agregado exitosamente.")
    
    ###
    #Busca un país por nombre exacto sin distinguir mayúsculas.
    #Devuelve el diccionario del país o None si no lo encuentra.
    #Se usa internamente por agregar_pais y actualizar_pais.
    ###
def buscar_exacto(paises, nombre):
    try:
        if not nombre or not isinstance(nombre, str):
            raise ValueError("Nombre inválido.")
        for pais in paises:
            if pais["nombre"].lower() == nombre.lower():
                return pais
    except ValueError:
        return None
    return None




