"""
Problema II
Se desea registrar las temperaturas de una ciudad durante una semana (7 días).
Escribe un pseudocódigo que:
• Almacene las 7 temperaturas en un arreglo.
• Calcule y muestre la temperatura promedio de la semana.
• Determine y muestre la temperatura más alta y la más baja.
• Cuente cuántos días tuvieron una temperatura superior al promedio."""

Temperaturas = []
Dias = 7
n = 0
Prom = 0
Mayor = 0


while n < Dias:
    n += 1
    Temperatura = float(input(f"Ingrese la temperatuda del dia {n}: "))
    Temperaturas.append(Temperatura)
    Prom += Temperatura
Prom /= Dias

for i in range(Dias -1):
    for j in range(Dias -1 -i):
        if Temperaturas[j] > Temperaturas[j +1]:
            x = Temperaturas[j]
            Temperaturas[j] = Temperaturas[j + 1]
            Temperaturas[j + 1] = x
x = len(Temperaturas)
for m in range(x):
    if Temperaturas[m] > Prom:
        Mayor += 1
    m += 1

#Mostrar las temperaturas almacenadas
print(Temperaturas) 

#Promedio de temperaturas
print(Prom)

#Temperaturas más altas y bajas
print(f"La temperatura más alta alcanzada fue de", Temperaturas[0])
print(f"La temperatura más baja alcanzada fue de", Temperaturas[6])

#Dias con la temperatura mayor al promedio
print(Mayor)





