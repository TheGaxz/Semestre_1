'''
Utilizar una funcion que permita ingresar nombres para que el usuario ingrese nombres
uno por uno. Los nombres se deben almacenar en una lista. Luego, crear otra funcion
que permita contar las letras, la cual debe recorrer la lista de nombres y cuente la canti-
dad total de letras de todos los nombres ingresados. Por ultimo, crear una funcion para
que imprima los resultados y muestre en pantalla los nombres ingresados y el total de
letras contadas.
'''

def solicitud_nombres():
    nombres=[]
    print("escriba 'termino' para que deje de pedir datos")
    while True:
        n=str(input("ingrese un nombre: "))
        if n == "termino":
            break
        nombres.append(n)
    return nombres

nombre=solicitud_nombres()

def letra(nombres):
    letras=0
    for i in nombres:
        letras += len(i)
    return letras 

letras=letra(nombre)

def total(nombres,letras):
    for i in nombres:
        print(i)
    print("el total de letras de los nombres ingresados es: ",letras)

total(nombre,letras)


