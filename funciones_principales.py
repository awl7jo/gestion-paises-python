import csv
import os

ARCHIVO_CSV = 'paises.csv'

# ============================================================
# VALIDACIONES
# ============================================================

def pedir_texto(mensaje):
    """Pide un texto al usuario y valida que no esté vacío."""
    while True:
        texto = input(mensaje).strip()
        if texto != "":
            return texto
        print("No se permiten campos vacíos.")


def pedir_entero(mensaje):
    """Pide un número entero positivo al usuario."""
    while True:
        try:
            numero = int(input(mensaje))
            if numero > 0:
                return numero
            print("Ingrese un número mayor a 0.")
        except ValueError:
            print("Debe ingresar un número válido.")


# ============================================================
# FUNCIONES DE ARCHIVO
# ============================================================

def cargar_paises():
    """Lee el archivo CSV y devuelve una lista de diccionarios con los datos de cada país."""
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
                except ValueError:
                    print("Error en una fila del CSV: población o superficie no son números.")
                except KeyError as e:
                    print(f"Error en una fila del CSV: falta la columna {e}.")
    except FileNotFoundError:
        print("Archivo CSV no encontrado. Se creará uno nuevo al guardar.")
    return paises


def guardar_paises(paises):
    """Sobreescribe el archivo CSV con la lista de países actualizada."""
    try:
        with open(ARCHIVO_CSV, 'w', encoding='utf-8', newline="") as archivo:
            campos = ['nombre', 'poblacion', 'superficie', 'continente']
            escritor = csv.DictWriter(archivo, fieldnames=campos)
            escritor.writeheader()
            escritor.writerows(paises)
            print('Datos guardados correctamente.')
    except PermissionError:
        print(f'Error: no tenés permisos para escribir en {ARCHIVO_CSV}.')
    except Exception as e:
        print(f'Error inesperado al guardar: {e}')


# ============================================================
# FUNCIONES PRINCIPALES
# ============================================================

def mostrar_paises(paises):
    """Muestra todos los países cargados en el sistema."""
    try:
        if not paises:
            raise ValueError("No hay países cargados.")
        print("\n=== LISTA DE PAÍSES ===")
        for pais in paises:
            print("----------------------------")
            print(f"Nombre: {pais['nombre']}")
            print(f"Población: {pais['poblacion']}")
            print(f"Superficie: {pais['superficie']} km²")
            print(f"Continente: {pais['continente']}")
    except ValueError as e:
        print(e)


def buscar_exacto(paises, nombre):
    """Busca un país por nombre exacto sin distinguir mayúsculas.
    Devuelve el diccionario del país o None si no lo encuentra.
    Se usa internamente por agregar_pais y actualizar_pais."""
    try:
        if not nombre or not isinstance(nombre, str):
            raise ValueError("Nombre inválido.")
        for pais in paises:
            if pais["nombre"].lower() == nombre.lower():
                return pais
    except ValueError:
        return None
    return None


def buscar_pais(paises):
    """Busca y muestra países cuyo nombre contenga el texto ingresado por el usuario."""
    print("\n=== BUSCAR PAIS ===")
    buscar = pedir_texto("Ingrese el nombre del país o parte del nombre: ")
    encontrados = []
    for pais in paises:
        if buscar.lower() in pais["nombre"].lower():
            encontrados.append(pais)
    if len(encontrados) == 0:
        print("No se encontraron resultados.")
        return
    mostrar_paises(encontrados)


def agregar_pais(paises):
    """Pide los datos de un nuevo país al usuario, los valida y los agrega a la lista."""
    print('\n----AGREGAR PAIS----')
    print("(escribí 'cancelar' para volver al menú)\n")

    # Nombre
    while True:
        try:
            nombre = input("Nombre del pais: ").strip()
            if nombre.lower() == 'cancelar':
                print('Volviendo al menu principal...')
                return
            if not nombre:
                raise ValueError("El nombre no puede estar vacío.")
            if not all(c.isalpha() or c.isspace() for c in nombre):
                raise ValueError("El nombre solo puede contener letras y espacios.")
            if buscar_exacto(paises, nombre) is not None:
                raise ValueError(f"Ya existe un país llamado '{nombre}'.")
            break
        except ValueError as e:
            print(f"Error: {e}")

    # Población
    while True:
        try:
            entrada = input("Población del país: ").strip()
            if entrada.lower() == 'cancelar':
                print('Volviendo al menu principal...')
                return
            poblacion = int(entrada)
            if poblacion <= 0:
                raise ValueError("La población debe ser mayor a 0.")
            break
        except ValueError as e:
            print(f"Error: {e}")

    # Superficie
    while True:
        try:
            entrada = input("Superficie en km²: ").strip()
            if entrada.lower() == 'cancelar':
                print('Volviendo al menu principal...')
                return
            superficie = int(entrada)
            if superficie <= 0:
                raise ValueError("La superficie debe ser mayor a 0.")
            break
        except ValueError as e:
            print(f"Error: {e}")

    # Continente
    while True:
        try:
            continente = input("Continente: ").strip()
            if continente.lower() == 'cancelar':
                print('Volviendo al menu principal...')
                return
            if not continente:
                raise ValueError("El continente no puede estar vacío.")
            if not all(c.isalpha() or c.isspace() for c in continente):
                raise ValueError('El continente solo puede contener letras y espacios.')
            break
        except ValueError as e:
            print(f"Error: {e}")

    paises.append({
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    })
    guardar_paises(paises)
    print(f"País '{nombre}' agregado exitosamente.")


def actualizar_datos_paises(paises):
    """Busca un país por nombre y permite modificar su población y superficie."""
    print("\n=== ACTUALIZAR PAIS ===")
    actualizar = pedir_texto("Ingrese el país a actualizar: ")
    for pais in paises:
        if pais["nombre"].lower() == actualizar.lower():
            nueva_poblacion = pedir_entero("Ingrese la nueva población: ")
            nueva_superficie = pedir_entero("Defina la nueva superficie: ")
            pais["poblacion"] = nueva_poblacion
            pais["superficie"] = nueva_superficie
            guardar_paises(paises)
            print("Datos actualizados con éxito.")
            return
    print("País no encontrado.")


# ============================================================
# FILTROS
# ============================================================

def filtrar_continente(paises):
    """Filtra y muestra los países que pertenecen al continente ingresado."""
    try:
        continente = input("Ingresá el continente: ").strip()
        if not continente:
            raise ValueError("El continente no puede estar vacío.")
        filtrados = []
        for pais in paises:
            if pais["continente"].lower() == continente.lower():
                filtrados.append(pais)
        if len(filtrados) == 0:
            raise ValueError(f"No se encontraron países en '{continente}'.")
        mostrar_paises(filtrados)
    except ValueError as e:
        print(f"Error: {e}")


def filtrar_poblacion(paises):
    """Filtra y muestra los países cuya población esté dentro del rango ingresado."""
    try:
        minima = pedir_entero("Ingrese la población mínima: ")
        maxima = pedir_entero("Ingrese la población máxima: ")
        if minima > maxima:
            raise ValueError("El mínimo no puede ser mayor que el máximo.")
        filtrados = []
        for pais in paises:
            if minima <= pais["poblacion"] <= maxima:
                filtrados.append(pais)
        if len(filtrados) == 0:
            raise ValueError("No se encontraron países en ese rango.")
        mostrar_paises(filtrados)
    except ValueError as e:
        print(f"Error: {e}")


def filtrar_superficie(paises):
    """Filtra y muestra los países cuya superficie esté dentro del rango ingresado."""
    try:
        minima = pedir_entero("Ingrese la superficie mínima: ")
        maxima = pedir_entero("Ingrese la superficie máxima: ")
        if minima > maxima:
            raise ValueError("La mínima no puede ser mayor que la máxima.")
        filtrados = []
        for pais in paises:
            if minima <= pais["superficie"] <= maxima:
                filtrados.append(pais)
        if len(filtrados) == 0:
            raise ValueError("No se encontraron países en ese rango.")
        mostrar_paises(filtrados)
    except ValueError as e:
        print(f"Error: {e}")


def filtrar_paises(paises):
    """Muestra el submenú de filtros y llama a la función correspondiente."""
    print('\n--- FILTRAR PAISES ---')
    try:
        if not paises:
            raise ValueError('No hay países cargados.')
        print('1. Por continente')
        print('2. Por rango de población')
        print('3. Por rango de superficie')
        print('0. Volver al menú principal')
        opcion = input('Ingrese una opción: ').strip()
        opciones = {
            '1': filtrar_continente,
            '2': filtrar_poblacion,
            '3': filtrar_superficie
        }
        if opcion == '0':
            return
        if opcion not in opciones:
            raise ValueError('Opción inválida. Ingresá un número del 0 al 3.')
        opciones[opcion](paises)
    except ValueError as e:
        print(f'Error: {e}')


# ============================================================
# ORDENAMIENTO
# ============================================================

def obtener_nombre(pais):
    return pais["nombre"]


def obtener_poblacion(pais):
    return pais["poblacion"]


def obtener_superficie(pais):
    return pais["superficie"]


def ordenar_paises(paises):
    """Ordena y muestra los países por nombre, población o superficie de forma ascendente o descendente."""
    print("\n=== ORDENAR PAÍSES ===")
    print("1. Nombre")
    print("2. Población")
    print("3. Superficie")

    opcion = input("Seleccione opción: ").strip()

    if opcion == "1":
        tipo = input("Ascendente (A) o Descendente (D): ").upper()
        descendente = (tipo == "D")
        ordenados = sorted(paises, key=obtener_nombre, reverse=descendente)

    elif opcion == "2":
        tipo = input("Ascendente (A) o Descendente (D): ").upper()
        descendente = (tipo == "D")
        ordenados = sorted(paises, key=obtener_poblacion, reverse=descendente)

    elif opcion == "3":
        tipo = input("Ascendente (A) o Descendente (D): ").upper()
        descendente = (tipo == "D")
        ordenados = sorted(paises, key=obtener_superficie, reverse=descendente)

    else:
        print("Opción inválida.")
        return

    mostrar_paises(ordenados)


# ============================================================
# ESTADÍSTICAS
# ============================================================

def mostrar_estadisticas(paises):
    """Calcula y muestra estadísticas del dataset: máximos, mínimos, promedios y cantidad por continente."""
    print("\n=== ESTADÍSTICAS ===")

    if len(paises) == 0:
        print("No hay países cargados.")
        return

    # Buscar mayor y menor población
    mayor = paises[0]
    menor = paises[0]
    for pais in paises:
        if pais["poblacion"] > mayor["poblacion"]:
            mayor = pais
        if pais["poblacion"] < menor["poblacion"]:
            menor = pais

    # Buscar mayor y menor superficie
    mayor_sup = paises[0]
    menor_sup = paises[0]
    for pais in paises:
        if pais["superficie"] > mayor_sup["superficie"]:
            mayor_sup = pais
        if pais["superficie"] < menor_sup["superficie"]:
            menor_sup = pais

    # Promedios
    suma_poblacion = 0
    suma_superficie = 0
    for pais in paises:
        suma_poblacion += pais["poblacion"]
        suma_superficie += pais["superficie"]

    promedio_poblacion = suma_poblacion / len(paises)
    promedio_superficie = suma_superficie / len(paises)

    # Cantidad por continente
    continentes = {}
    for pais in paises:
        continente = pais["continente"]
        if continente in continentes:
            continentes[continente] += 1
        else:
            continentes[continente] = 1

    print("\nPaís con mayor población:", mayor["nombre"], "-", mayor["poblacion"])
    print("País con menor población:", menor["nombre"], "-", menor["poblacion"])
    print("\nPaís con mayor superficie:", mayor_sup["nombre"], "-", mayor_sup["superficie"])
    print("País con menor superficie:", menor_sup["nombre"], "-", menor_sup["superficie"])
    print(f"\nPromedio de población: {promedio_poblacion:.2f}")
    print(f"Promedio de superficie: {promedio_superficie:.2f}")
    print("\nCantidad de países por continente:")
    for continente in continentes:
        print(continente, ":", continentes[continente])


# ============================================================
# MENÚ PRINCIPAL
# ============================================================

def menu():
    """Función principal. Carga los datos y controla el flujo del programa mediante el menú."""
    paises = cargar_paises()
    while True:
        print("""
=== SISTEMA DE GESTIÓN DE PAÍSES ===
1) Mostrar todos los países
2) Agregar un país
3) Actualizar un país
4) Buscar un país
5) Filtrar países
6) Ordenar países
7) Mostrar estadísticas
8) Salir""")
        print("=" * 40)
        opcion = input("Elija una opción: ")
        match opcion:
            case "1":
                mostrar_paises(paises)
            case "2":
                agregar_pais(paises)
            case "3":
                actualizar_datos_paises(paises)
            case "4":
                buscar_pais(paises)
            case "5":
                filtrar_paises(paises)
            case "6":
                ordenar_paises(paises)
            case "7":
                mostrar_estadisticas(paises)
            case "8":
                print("Saliendo...")
                break
            case _:
                print("Opción inválida.")


menu() #hola