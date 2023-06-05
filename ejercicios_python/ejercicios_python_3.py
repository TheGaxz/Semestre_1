
a = float(input("Ingrese el primer lado del triangulo: "))
b = float(input("Ingrese el segundo lado del triangulo: "))                  
c = float(input("Ingrese el tercer lado del triangulo: "))

p=(a+b+c) / 2
area=p*(p-a)*(p-b)*(p-c)

if a==b==c:
    print("El triangulo es equilatero")
elif a!=b and b!=c:
    print("El triangulo es escaleno")
else:
    print("El triangulo es isoceles")

print("El area del triangulo es: ", area)





