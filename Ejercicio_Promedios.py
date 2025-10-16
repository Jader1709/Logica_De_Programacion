n=int(input("Número de estudiantes: "))
suma=0
muy_fuertes=fuertes=recomendados=no_rec=0

for _ in range(n):
    cod=input("Código: ")
    prom=float(input("Promedio: "))
    suma+=prom
    if prom>=4.8:
        rec="Muy fuerte recomendación"; muy_fuertes+=1
    elif prom>=4.5:
        rec="Fuerte recomendación"; fuertes+=1
    elif prom>=4.0:
        rec="Recomendado"; recomendados+=1
    else:
        rec="No recomendado"; no_rec+=1
    print(cod, prom, rec)

print("Promedio general:",suma/n)
print("Muy fuerte:",muy_fuertes,"Fuerte:",fuertes,"Recomendado:",recomendados,"No recomendado:",no_rec)