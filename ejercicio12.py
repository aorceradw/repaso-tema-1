contraseña_buena = "python123"
intentos = 1
contraseña = input("Escriba una contraseña: ")

while contraseña != contraseña_buena:
    print("Contraseña incorrecta")
    intentos = intentos + 1
    contraseña = input("Escriba una contraseña: ")

print("Contraseña correcta")
print(f"Has necesitado {intentos}, intentos")