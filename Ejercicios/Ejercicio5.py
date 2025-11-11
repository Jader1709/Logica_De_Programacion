numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))

while True: 
    opcion = int(input("Selecciona la opción que desees operar:\n"
                       "1. Suma\n"
                       "2. Resta\n"
                       "3. División\n"
                       "4. Multiplicación\n"
                       "5. Salir\n"
                       "Opción: "))

    if opcion == 1:
        print("Resultado:", numero1 + numero2)
    elif opcion == 2:
        print("Resultado:", numero1 - numero2)
    elif opcion == 3:
        if numero2 == 0:
            print("No se puede dividir por 0")
        else:
            print("Resultado:", numero1 / numero2)
    elif opcion == 4:
        print("Resultado:", numero1 * numero2)
    elif opcion == 5:
        print("Saliendo...")
        break
    else:
        print("Opción inválida, intenta de nuevo.")
