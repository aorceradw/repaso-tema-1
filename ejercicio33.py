def mostrar_doble():
    """Funcion para mostrar la multiplicacion de un numero"""
    try:
        numero = int(input("Digame un numero:"))
        doble = numero * 2
        print(doble)
    except ValueError:
        print("Ese valor no es valido")

if __name__ == "__main__":
        mostrar_doble()