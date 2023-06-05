nombre = input("¿Cual es nombre del estudiante?\n")
asignatura = input("¿Cual es la asignatura?\n")
nota_lab1 = float(input("¿Cual es la primera nota de laboratorio del estudiante\n"))
nota_lab2 = float(input("¿Cual es la segunda nota de laboratorio del estudiante\n"))
promedio = float(nota_lab1*0.3 + nota_lab2*0.7)
datos = {
    "Nombre": nombre,
    "Asignatura": asignatura,
    "Nota Lab1": nota_lab1,
    "Nota Lab2": nota_lab2,
    "Nota final": round(promedio, 1),
}

print(datos)

