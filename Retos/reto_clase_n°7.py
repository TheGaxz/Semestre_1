#Escribir una funcion que reciba una frase por teclado y devuelva un diccionario con las palabras que contiene y su longitud.

texto = input("Ingrese el texto: ")


eliminar = ",;.:!\n"

for caracter in eliminar:
    texto = texto.replace(caracter, "")

texto = texto.lower()
var_1 = len(texto)
var_2 = texto.split()

diccionario = {
    var_1 : var_2,
}


print(diccionario)
