
#01-Declarando la primera funcion
print("###### Declarando la primera funcion #####")
def mi_primera__funcion():
    print("Esta es mi primera funcion")

mi_primera__funcion()

#02- Declarando un funcion y utilizando listas
print("##### Declarando un funcion y utilizando listas #####")

#Scope local es 
def concatenar(lista1,lista2):
    return lista1 + lista2

lista1 = [1,2,3]
lista2 = [4,5,6]

#concatenar()
print(concatenar(lista1,lista2))

#03- Declarando una funcion multiplicacion pasando parametro
print("##### Declarando una funcion multiplicacion pasando parametro #####")

def multiplicacion (num1,num2):
    return num1*num2

#Multiplicacion()
print(multiplicacion(10,2))

#04-Ejemplo de una funcion
print("##### Funciones suma y resta por teclado")

def suma(a,b):
    return a+b

def resta(a,b):
    return a-b

a=int(input("Ingrese el valor de a: "))
b=int(input("Ingrese el valor de b: "))

#Se llama a la funcion suma
resultado = suma(a,b)
print("La suma es de:", resultado)

#Se llama a la funcion resta
resultado2 = resta(a,b)
print("La suma es de:", resultado2)