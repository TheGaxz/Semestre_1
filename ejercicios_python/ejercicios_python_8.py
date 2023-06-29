
mes = input("Ingrese un mes: ")

if mes == "Enero" or mes == "Febrero" or mes == "Marzo":
    print("Corresponde a Verano")
elif mes == "Abril" or mes == "Mayo" or mes == "Junio":
    print("Corresponde a Invierno")
elif mes == "Julio" or mes == "Agosto" or mes == "Septiembre":
    print("Corresponde Otoño")
elif mes == "Octubre" or mes == "Noviembre" or mes == "Diciembre":
    print("Corresponde a Primavera")
else:
    print("No es un mes")

