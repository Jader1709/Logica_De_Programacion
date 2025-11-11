"""
Problema I
Desarrolla un pseudocódigo que permita registrar las calificaciones de N
estudiantes, cada uno con 4 notas. El programa debe:
• Calcular el promedio de cada estudiante.
• Mostrar si cada estudiante aprueba o reprueba (nota ≥ 3.0).
• Al final, mostrar el número total de estudiantes aprobados y reprobados.
"""

N = int(input("Ingrese el numero de estudiantes: "))
Notas = 4
Aprueban = 0
NoAprueban = 0

for i in range(N):
    i += 1
    promedio = 0
    Total = 0
    for j in range(Notas):
        j += 1
        Nota = float(input(f"Ingrese la nota {j} del estudiante {i}: "))
        Total += Nota
        Promedio = Total/Notas    
    if Promedio >= 3:
        Aprueban += 1
        print(f"El promedio del estudiante {i} es de {Promedio}, el estudiante APRUEBA")
    else:
        NoAprueban += 1
        print(f"El promedio del estudiante {i} es de {Promedio}, el estudiante NO APRUEBA")

print(f"Los estudiantes que APRUEBAN son {Aprueban}")
print(f"Los estudiantes que NO APRUEBAN son {NoAprueban}")
