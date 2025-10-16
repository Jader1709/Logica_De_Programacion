import random
num = random.randint(1,50)

while True:
    numero = int(input("Ingrese un numero: "))
    if numero > num:
        print("Demasiado alto")
    elif numero < num:
        print("Demasiado bajo")
    elif numero == num:
        print("Adivinaste el numero")
