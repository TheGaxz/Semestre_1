#Construir un algoritmo que permita generar enteros de 3 en 3 comenzado por el 2 hasta el
#valor máximo que será menor que 30. Calcular la suma de los enteros generados que sean
#divisibles por 5, y la suma de los enteros generados que sean impares.

i = 2

while i<30:
    print(i)
    i +=3

suma_divisible= i % 5 == 0

if i % 5 == 0:
    suma_divisible += i
    
