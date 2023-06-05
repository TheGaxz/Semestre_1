
ciudades= ["Santiago", "Temuco", "Osorno", "Punta Arenas"]
indice= [134, 99, 245, 50]

ciudades_aux= (zip(ciudades, indice))
maximoValor=max(ciudades_aux, key=lambda x : x[1])
print ("La ciudad con la peor calidad de aire es:",maximoValor[0],"con un valor de:",maximoValor[1])

if maximoValor[1]>=0 and maximoValor[1]<=50:
    print("El indice de ICA es buena")
elif maximoValor[1]>=51 and maximoValor[1]<=100:
    print("El indice de ICA es moderada")
elif maximoValor[1]>=101 and maximoValor[1]<=150:
    print("El indice de ICA es dañina a la saluda para grupos sensibles")
elif maximoValor[1]>=151 and maximoValor[1]<=200:
    print("El indice de ICA es dañina a la salud")
elif maximoValor[1]>=201 and maximoValor[1]<=300:
    print("El indice de ICA es muy dañina a la salud")
else:
    maximoValor[1]<300 
    print("El indice de ICA es peligrosa")
ciudades_aux2= (zip(ciudades, indice))


minimoValor=min(ciudades_aux2, key=lambda x : x[1])
print ("La ciudad con la mejor calidad de aire es:",minimoValor[0],"con un valor de:",minimoValor[1])


if minimoValor[1]>=0 and minimoValor[1]<=50:
    print("El indice de ICA es buena")
elif minimoValor[1]>=51 and minimoValor[1]<=100:
    print("El indice de ICA es moderada")
elif minimoValor[1]>=101 and minimoValor[1]<=150:
    print("El indice de ICA es dañina a la saluda para grupos sensibles")
elif minimoValor[1]>=151 and minimoValor[1]<=200:
    print("El indice de ICA es dañina a la salud")
elif minimoValor[1]>=201 and minimoValor[1]<=300:
    print("El indice de ICA es muy dañina a la salud")
else:
    minimoValor[1]<300 
    print("El indice de ICA es peligrosa")

