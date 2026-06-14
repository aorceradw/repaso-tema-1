opcion= -1 
while opcion != 3:
    print("1.Saludar")
    print("2.Despedirse")
    print("3.Salir")
    opcion = int(input("INTRODUCE UNA OPCIÖN: "))
    print("---------------------------------------")

    if opcion == 1:
        print("HOLA")
    elif opcion == 2:
        print("Hasta luego")
    elif opcion == 3:
        print("Saliendo...")
    else:
        print("OPCIONNOT-F-F-FOUND")