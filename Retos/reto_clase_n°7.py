#Escribir una funcion que reciba una frase por teclado y devuelva un diccionario con las palabras 
#que contiene y su longitud.

def funcion() :
    texto= str(input("Ingrese el texto: "))
    division = texto.split()
    diccionario= {}

    for i in division:
        diccionario[i] = len(i)

    print(diccionario)
funcion()

 


