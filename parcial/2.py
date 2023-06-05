#Calcular la media de calificaciones de la asignatura de Programación. Deducir cuántas son más altas que 
#la media y cuántas más bajas que dicha media. Se solicita un mínimo de 10 notas. Estas calificaciones se 
#ingresarán por teclado y no se permite notas inferiores a 1.0 ni mayores a 7.0

nota = float(input("Ingrese la nota: "))

for nota in range(10):
    nota = float(input("Ingrese la nota: "))
    lista = []

if nota in range(1,8):
    print(" ")
else:
    nota = float(input("Ingrese la nota valida: "))

media = round(sum([nota])/len([nota]),1)

'''if nota < media:
    print("La nota es menor")
else:
    nota>media
    print("La nota es mayor")'''

print("La media de las notas es: ",media)
#print("Las notas menores a la media son: ", bajo, " y altas a la media son: ", alto)

