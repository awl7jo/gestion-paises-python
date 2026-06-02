from gestion_paises import ARCHIVO_CSV
import csv

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

