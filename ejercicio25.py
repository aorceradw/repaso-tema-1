media = 0
suma = 0
notas  = []

for i in range(5):
    nota = int(input("Introduce notas aqui: "))
    notas.append(nota)

for nota in notas:
    suma = suma + nota
    media = suma / len(notas)

print(media)