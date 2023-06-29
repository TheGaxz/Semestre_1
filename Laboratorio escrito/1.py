
pacientes = [["Pedro", 1.78], ["Constanza", 1.56], ["Amanda", 1.62], ["Dario", 1.89], ["Fernanda", 1.67]]

#A
def minima():
    min(round(pacientes,1))

#B
def agregar():
    pacientes.append(["Ricardo", 1.71])

#C
def Dario():
    if "Dario" == pacientes:
        print("Si se encuentra")
    else:
        print("No se encuentra")

#D
print(minima)
print(agregar)
print(Dario)