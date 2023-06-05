
superficie1= 23890
habitantes1= 1556805

datos_biobio={
    "ID region": 8,
    "Nombre": "BioBio", 
    "Superficie": superficie1,
    "Habitantes":habitantes1,
}

superficie2= 48583
habitantes2= 828708

datos_lagos={
    "ID region": 10,
    "Nombre": "Los Lagos",
    "Superficie": superficie2,
    "Habitantes": habitantes2
}

print(datos_biobio)
print(datos_lagos)

densidad= habitantes1/superficie1
densidad2= habitantes2/superficie2
datos_biobio["densidad"]= densidad
datos_lagos["densidad"]= densidad2

datos_biobio["capital"]= "Concepcion"
datos_lagos["capital"]= "Puerto Montt"

comunas1=("Lebu", "Lota", "Los Angeles")
comunas2=("Castro", "Puerto Varas", "Purranque")
datos_biobio["Comunas"]= comunas1
datos_lagos["Comunas"]= comunas2

provincias1= {"Bio Bio", "Arauco", "Concepcion"}
provincias2= {"Osorno", "LLanquihue", "Chiloe", "Palena"}
datos_biobio["Provincias"]= provincias1
datos_lagos["Provincias"]= provincias2

print("Los datos de la region del BioBio son: ",datos_biobio)
print("Los datos de la region de Los Lagos son: ",datos_lagos)
