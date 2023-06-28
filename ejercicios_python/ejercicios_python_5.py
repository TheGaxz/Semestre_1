
n1 = float(input("Ingrese la primera nota: "))
n2 = float(input("Ingrese la segunda nota: "))
n3 = float(input("Ingrese la tercera nota: "))

pp=(n1*0.3)+(n2*0.4)+(n3*0.3)

print(pp)
if pp >= 6.0:
    print("El estudiante aprobo la asignatura con distinción")
elif pp >= 4.0:
    print("El estudiante aprobo la asignatura")
else:
    print("El estudiante reprobo la asignatura")

