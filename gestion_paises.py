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