numeros = []
numeros_pares = []
numeros_impares = []
rango = int(input("Ingrese el tamaño del arreglo: "))
i = 0
for i in range(rango):
    i += 1
    numero = int(input(f'Ingrese el numero {i}: '))
    numeros.append(numero)
    if numero % 2 == 0:
        numeros_pares.append(numero)
    else:
        numeros_impares.append(numero)

print(f'El arreglo de numeros es: {numeros}')
print(f'Los numeros pares son: {numeros_pares}') 
print(f'Los numeros pares son: {numeros_impares}') 