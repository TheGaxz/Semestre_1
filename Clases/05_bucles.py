
edad= 15
num=0

#Bucle infinito
#while edad < 18:
#    print("Eres menor de edad, no puedes manejar")

#Bucle infinito
while num<=100:
    print(num)
    num+=2
else:
    print("Mi condicion es igual o mayor a 100")


while num <=300:
    print(num)
    num+=2
    if num == 250:
        print("Mi condicion es igual a 250")

while num <= 400:
    print(num)
    num+=2
    if num == 350:
        print("Se detiene la ejecucion")
        break  #Con el BREAK se corta el ciclo
#BREAK solo se usa en los bucle, no en los condicionales.

#while True:
#    parametro = input(">")
#    if parametro == "exit":
#        break
#    else:
#        print(parametro)

#no esta optimizado
for i in (1,2,3,4,5,6,7,8,9,10):
    print(i)

print("For N°2")
newlista = [1,2,3,4,5,6,7,8,9,10]
for i in newlista:
    print(i)

print("For N°3")
for i in range(1,11):
    print(i)

#RANGE= rango, decir el limite. EJ: rango(5) se imprimen: 0,1,2,3,4
#Y si es range(2,6)= 2,3,4,5

