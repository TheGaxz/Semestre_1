import getopt


print("1-Operadores aritmeticos")
print("Suma entre a + b es:", a+b)
print("Resta entre a - b es:", a-b)
print("Multiplicacion entre a * b es:", a*b)
print("Division entre a/b es:", a/b)
print("")
print
print

T = 5.39 #tiempo en segundos
G = 9.81 #la aceleracion de gravedad
v = G*T

print(f"La velocidad del objeto en caida libre es de: ¨{v} n/s")

#complex= numeros complejos
#int = enteros
#float= decimales

c2 = complex(3, -5)
print("El numero complejo es:", c2)

#se puede multiplicar las palabras
print("Hola" * 5)

print("Operadores de comparacion")
print(a==b) #Igual a 
print(a!=b) #desigual a
print(a>b) #mayor a
print(a<b) #menor a 
print(a>=b) #mayor o igual a
print(a<=b) #menos o igual a 

print("Comparando caracteres")
animales_domesticos="gato"
animales_salvajes= "leopardo"
print(len(animales_domesticos)==len(animales_salvajes))

#no es lo mismo print(len(animales_domesticos)==animales_salvajes)) QUE print(animales_domesticos)==(animales_salvajes))

#condicionales 

#if = si
#sino = else
#fin si = no existe en python
#elif = nuevo en python

#a no b = not
#a y b = and
#a o b = or

bencina= True
encendido= False
edad= 19

#utilizando and
#para que de true tiene que anbas variables ser verdaderas
if bencina and encendido:
    print("El vehiculo puede avanzar")
else:
    print(" El vehiculo no puede arrancar")

#utilizando or
#para que de true una de las variables tiene que ser verdadera
if bencina or encendido:
    print("El vehiculo puede avanzar")
else:
    print(" El vehiculo no puede arrancar")

#utilizando not junto a and
#not invierte la variables, EJ: si es true: not true = false
if not bencina and encendido:
    print("El vehiculo puede avanzar")
else:
    print(" El vehiculo no puede arrancar")

#utilizando not junto a and y or
#ej:(encendido and edad >= 18) = false
#ej: si (encendido or edad >= 18)= true
if not bencina or (encendido and edad >= 18):
    print("El vehiculo puede avanzar")
else:
    print(" El vehiculo no puede arrancar")
















