def filtrar_superficie(paises):

    minimo = pedir_entero("Superficie mínima: ")
    maximo = pedir_entero("Superficie máxima: ")

    filtrados = []

    for pais in paises:

        if minimo <= pais["superficie"] <= maximo:
            filtrados.append(pais)

    if len(filtrados) == 0:
        print("No se encontraron países.")
    else:
        mostrar_paises(filtrados)

def filtrar_continente(paises):
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