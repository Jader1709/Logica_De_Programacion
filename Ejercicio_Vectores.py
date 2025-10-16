# Hacer un algoritmo que calcule el valor promedio y la varianza
# de un grupo de datos positivos, dispuestos de a uno por registro.

Datos = []
Rango = int(input("Ingrese el rango del vector: "))

Promedio = 0
Varianza = 0

# Leer los datos y calcular el promedio
for i in range(Rango):
    Dato = float(input(f"Ingrese el dato {i+1}: "))
    Datos.append(Dato)
    Promedio += Dato

Promedio = Promedio / Rango  # Calcular promedio total

# Calcular la varianza
for j in range(Rango):
    Varianza += (Datos[j] - Promedio) ** 2

Varianza = Varianza / Rango  # Varianza poblacional

#Para sacar la desviacion debemos sacar la raiz de la varianza
Desviacion = Varianza ** 0.5

# Mostrar resultados
print(f"\nEl promedio es: {Promedio}")
print(f"La varianza es: {Varianza}")
print(f"La desviacion es: {Desviacion}")
