
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