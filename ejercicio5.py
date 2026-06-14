nota = float(input("Insertar nota: "))

if nota < 0 or nota > 10:
    print("nota no valida")
elif nota < 5:
    print("suspenso")
elif nota < 7:
    print("aprobado")
elif nota < 8:
    print("notable")
else:
    print("sobresaliente")