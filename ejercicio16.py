opcion = 1

while opcion != 4:
    print("")
    print("1. SUMAS")
    print("2. RESTAS")
    print("3. MULTIPLICACIONES")
    print("4. DIVISION")
    print("5. SALIR")
    
    print("")

    opcion=int(input("Ingresa un numerito:"))

    if opcion == 1:
        num1= int(input("Inserta el primer numero: "))
        num2= int(input("Ingresa el segundo: "))
        total = num1 + num2
        print(f"El resultado es, {total}")
    elif opcion == 2:
        num1= int(input("Inserta el primer numero: "))
        num2= int(input("Ingresa el segundo: "))
        total = num1 - num2
        print(f"El resultado es, {total}")

    elif opcion == 3:
        num1= int(input("Inserta el primer numero: "))
        num2= int(input("Ingresa el segundo: "))
        total = num1 * num2
        print(f"El resultado es, {total}")
    elif opcion == 4:
        num1= int(input("Inserta el primer numero: "))
        num2= int(input("Ingresa el segundo: "))
        if num2 == 0:
            print("No se puede dividir a cero")
        else:
            total = num1 / num2
        print(f"El resultado es, {total}")
    elif opcion == 5:
        print("Saliendo...")
    else:
        print("OPCION INVALIDA")