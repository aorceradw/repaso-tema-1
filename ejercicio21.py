nombres =[]

nombre= input("Escribe un nombre: ")
nombres.append(nombre)
nombre= input("Escribe otro nombre: ")
nombres.append(nombre)
nombre = input("Introduce el ultimo nombre: ")
nombres.append(nombre)

for nombre in nombres:
    print(nombre)