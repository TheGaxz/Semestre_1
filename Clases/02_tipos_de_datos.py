edad = 18
peso = 69
estatura = 1.74

imc = peso/(estatura**2)

print (" Mi imc es de: {:.5f}".format(imc),"\n") #formateando el valor

asignatura = "programacion"
carrera = "Ingenieria civil en informatica"
print("La asignatura de", asignatura, "corresponde a la carrera de", carrera)
print("La cantidad de caracteres de la palabra", asignatura, "es de:", len(asignatura))

ampolleta = False
interruptor = True

print(ampolleta,interruptor)
print("La variable ampolleta es de tipo",type(ampolleta),"\n")

print(bool(0))
print(bool(none))

nueva_list = list()
otra_lista = []
print("Esta es una lista vacia:", nueva_lista)
print("Esta es otra lista vacia:", otra_lista)
print(type(otra_lista))

estudiantes = ["Matias", "Marco", "Cristobal", "Sebastian", "Marco"]
num = [1,2,3,4,5,6,1]
lenguaje = ["Phyton"]

data = ["Osorno", {"UV" : "nivel bajo", "temp C" :15},(-40.5725, -73.1353)]
listamixta = ("Felipe", 100, True)

print("Lista de cadena de caracteres:", estudiantes)
print("Lista de numeros:", num)
print("Lista de un elemento", lenguaje)
print("Esta lista mixta", listamixta)
print("Esto igual es una lista", data)
print(len(listamixta))

print(list("Python"))
print(list(range(1,3)))
print("\n") 

newtubla = tuple()
grupo1 = ("Daniel","Cristian", "Felipe",)

#muestra el indice del primer elemento buscado
print("Indice del elemento:", grupo1.index ("Daniel"))

grupo[0] = "Constanza"
print(grupo1)

#Se pueden sumar las tuplas?

#obteniendo un trozo de la tupla
grupo2 = ("Pedro",100, "Felipe","Diego", 2020, "Alejandra")
print("trozo de la tupla",grupo2[0:3])

#entonces como no puedo modificar una tupla, que puedo hacer?
grupo1 = list(grupo1)
print("la tupla ahora es de tipo:", type(grupo1), "\n")
#si sabes de antemano que vas a editar la tupla, mejor crea una lista

#set (conjuntos) - estructura fija
print ("######## 06-SETS ######")
conjunto_vacio = set()
conjunto_vacio1 = {} #diccionario o set?
print(type(conjunto_vacio1))
conjunto_colores = set ({"Azul", "Rojo", "Verde"}) #utilizando la funcion set
conjunto_animales = {"Gato", "Perro", "Loro"} #utilizando llaves 

print(type(conjunto_colores))
print("EL primer set contiene los siguientes colores", conjunto_colores)

print(conjunto_animales[0]) #accediendo al primer elemento del set
conjunto_colores.add("Celeste")
print("El set de colores lo conforman:". conjunto_colores)

diccionario1 = dict()
diccionario2 = {}

datos_personales = {
    "Nombre" : "Gabriel",
    "Instituciòn" : "ULA",
    "Edad" : 18,
    "Asignatura" : ("Estructura de Datos", "Programacion")
    }

print("Diccionario actualizado:", datos_personales)

#consulta la cantidad de elementos del diccionario
print(len(datos_personales))

#es facilmente accesible a los elementos

#como actualizamos el valor de una clave dentro de un diccionario
datos_personales["Institucion"] = "uss"

datos_personales["Ciudad"] = "Osorno"
print



