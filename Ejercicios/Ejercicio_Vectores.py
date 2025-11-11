Datos = []
Rango = int(input("Ingrese el rango del vector: "))

Promedio = 0
Varianza = 0

for i in range(Rango):
    Dato = float(input(f"Ingrese el dato {i+1}: "))
    Datos.append(Dato)
    Promedio += Dato

Promedio = Promedio / Rango 

for j in range(Rango):
    Varianza += (Datos[j] - Promedio) ** 2

Varianza = Varianza / Rango 


Desviacion = Varianza ** 0.5

print(f"\nEl promedio es: {Promedio}")
print(f"La varianza es: {Varianza}")
print(f"La desviacion es: {Desviacion}")
