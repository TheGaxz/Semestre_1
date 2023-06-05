#Se cuenta con dos sets, los cuales contienen precios de productos: 

set1 = [100, 250, 300, 1000]
set2 = [150, 250, 500, 1000]

#A) Verificar si el valor 100 está en ambos sets

if set1.count(100) and set2.count(100):
    print("Si se encuentran en ambos set")
else:
    print("No se encuentra en ningun set")

#B) Comprobar si al menos el valor 500 o 700 está en alguno de los sets

valor= set1.count(700)
valor2= set2.count(700)
valor3= set1.count(500)
valor4= set2.count(500)

if valor:
    print("Si se encuentra")
else:
    print("No se encuentra")

if valor2:
    print("Si se encuentra")
else:
    print("No se encuentra")

if valor3:
    print("Si se encuentra")
else:
    print("No se encuentra")

if valor4:
    print("Si se encuentra")
else:
    print("No se encuentra")

#C) Elevar a 3 todos los valores dentro de los sets
'''sets_elevado1 = set1**3
sets_elevado2 = set2**3

print(sets_elevado1)
print(sets_elevado2)'''

#D) Unir ambos sets en uno solo
sets=(set1+set2)

se=set(sets)

print(se)