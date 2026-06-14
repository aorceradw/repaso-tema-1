suma = 0
media = 0
notas =  [5,7,8,4,9]

for nota in notas:
    suma = suma + nota
    media = suma /len(notas)

print(f"La nota es {media}")