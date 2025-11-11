numero = int(input("Digite un número entero positivo: "))
invertido = 0

while numero > 0:
    digito = numero % 10
    invertido = invertido * 10 + digito
    numero //= 10

print("Número invertido:", invertido)