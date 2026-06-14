nota = float(input("Pon una nota: "))

if nota < 4.99:
    print("SUSPENSO")
elif nota <7:
    print("APROBADO")    
elif nota < 9:
    print("NOTABLE")
else:
    print("SOBRESALIENTE")