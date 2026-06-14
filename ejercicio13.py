contraseña_buena = "python123"
intentos = 1
contraseña = input("Ponga una contraseña: ")

while contraseña != contraseña_buena and intentos <= 3:
    print("Contraseña incorrecta")
    intentos = intentos + 1
    contraseña = input("Ponga una contraseña: ")

if contraseña == contraseña_buena:
    print("Contraseña correcta")
    print(f"Has necesitado {intentos}, intentos")
else:
    print("Has superado el número de intentos")

