
#Obtener los números del rango 10 al 30, incrementando de 2 en 2. A continuación, sumar todos los números
#obtenidos.

datos = []

for i in range(10,31):
    print(i)
    i + 2
    datos.append(i)
print(sum(datos))

