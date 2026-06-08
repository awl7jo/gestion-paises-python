
def filtrar_paises(paises):
    print('\n--- FILTRAR PAISES ---')
    try:
        if not paises:
            raise ValueError('No hay paises cargados')
        print('1. Por continente')
        print('2. Por rango de poblacion')
        print('3. Por rango de superficie')
        print('0. Volver al menu principal')
        opcion = int(input('Ingrese una opcion ')).strip()

        opciones = {'1': filtrar_continente,
                    '2': filtrar_por_poblacion,
                    '3': filtrar_por_superficie

                    }
        if opcion == '0':
            return
        if opcion not in opciones:
            raise ValueError('Opcion invalida. ingresa un numero del 0 al 3.')
        opciones[opcion](paises)
    except ValueError as e:
        print(f'Error: {e}')