direccion_ip = input("Ingrese una dirección IPv4: ")

parte = ""
partes = []
i = 0

while i < len(direccion_ip):
    caracter = direccion_ip[i]

    if caracter == ".":  
        partes.append(parte)
        parte = ""
    else:
        parte = parte + caracter 
    i = i + 1

partes.append(parte)

if len(partes) != 4:
    print("Dirección IPv4 inválida (debe tener 4 bloques).")
else:
    es_valida = True
    for p in partes:
        j = 0
        while j < len(p):
            if p[j] < "0" or p[j] > "9":  
                es_valida = False
            j = j + 1

        numero = 0
        k = 0
        while k < len(p):
            numero = numero * 10 + (ord(p[k]) - ord("0"))
            k = k + 1

        if numero < 0 or numero > 255:
            es_valida = False

    if es_valida:
        print("Dirección IP válida.")
    else:
        print("Dirección IP inválida.")
