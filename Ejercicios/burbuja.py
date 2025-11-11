numeros = []
numeros_pares = []
rango = int(input("Ingrese el tamaño del arreglo: "))

# Llenar la lista
for i in range(rango):
    numero = int(input(f'Ingrese el número {i + 1}: '))
    numeros.append(numero)

print("La lista original es: ",numeros)

# Ordenar la lista (burbuja)
for i in range(rango - 1):
    for j in range(rango - 1 - i):
        if numeros[j] > numeros[j + 1]:
            x = numeros[j]
            numeros[j] = numeros[j + 1]
            numeros[j + 1] = x

for i in range(len(numeros)):
    if numeros[i] % 2 == 0:
        numeros_pares.append(numeros[i])

print("Lista ordenada:", numeros)
print("Lista de pares:", numeros_pares)




