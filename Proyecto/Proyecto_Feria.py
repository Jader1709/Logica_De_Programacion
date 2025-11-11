zonas = {
    "Norte": {"min": 4, "max": 8},
    "Oriente": {"min": 7, "max": 13},
    "Sur": {"min": 3, "max": 7},
    "Occidente": {"min": 8, "max": 14},
    "Centro": {"min": 6, "max": 12}
}

empresas_visitantes = []
empresas_expositoras = []
puestos = []  

for zona in zonas:
    puestos.append([zona, 0, False])

def mostrar_menu():
    print("\n=== SISTEMA DE GESTIÓN DE FERIA EMPRESARIAL ===")
    print("1. Ingresar empresa visitante")
    print("2. Ingresar empresa expositora (ocupar puesto)")
    print("3. Desocupar un puesto")
    print("4. Sugerir puesto según número de expositores")
    print("5. Mostrar porcentaje de ocupación de puestos")
    print("6. Ver información de todas las empresas")
    print("0. Salir")
    print("=" * 50)

def ingresar_visitante():
    nombre = input("Ingrese el nombre de la empresa visitante: ")
    while True:
        try:
            num_asistentes = int(input("Ingrese el número de personas que asistirán (máx 20): "))
            if num_asistentes > 0 and num_asistentes <= 20:
                break
            else:
                print("El número debe ser entre 1 y 20.")
        except ValueError:
            print("Por favor ingrese un número válido.")
    
    empresas_visitantes.append([nombre, num_asistentes])
    print(f"✓ Empresa visitante '{nombre}' registrada con {num_asistentes} asistentes.")

def ingresar_expositora():
    nombre = input("Ingrese el nombre de la empresa expositora: ")
    
    while True:
        try:
            num_expositores = int(input("Ingrese el número de expositores: "))
            if num_expositores > 0:
                break
            else:
                print("El número debe ser mayor a 0.")
        except ValueError:
            print("Por favor ingrese un número válido.")
    
    print("\nZonas disponibles:")
    for i, zona in enumerate(zonas.keys()):
        print(f"{i+1}. {zona}")
    
    while True:
        try:
            opcion_zona = int(input("Seleccione la zona (número): "))
            if 1 <= opcion_zona <= len(zonas):
                zona_seleccionada = list(zonas.keys())[opcion_zona - 1]
                break
            else:
                print("Opción inválida.")
        except ValueError:
            print("Por favor ingrese un número válido.")
    
    min_exp = zonas[zona_seleccionada]["min"]
    max_exp = zonas[zona_seleccionada]["max"]
    
    if num_expositores < min_exp or num_expositores > max_exp:
        print(f"✗ Error: La zona {zona_seleccionada} requiere entre {min_exp} y {max_exp} expositores.")
        return
    
    puesto_asignado = -1
    for i in range(len(puestos)):
        if puestos[i][0] == zona_seleccionada and not puestos[i][2]:
            puestos[i][1] = num_expositores
            puestos[i][2] = True
            puesto_asignado = i
            break
    
    if puesto_asignado == -1:
        puestos.append([zona_seleccionada, num_expositores, True])
        puesto_asignado = len(puestos) - 1
    
    empresas_expositoras.append([nombre, num_expositores, zona_seleccionada, puesto_asignado])
    print(f"✓ Empresa expositora '{nombre}' registrada en zona {zona_seleccionada} con {num_expositores} expositores.")
    print(f"  Puesto asignado: #{puesto_asignado}")

def desocupar_puesto():
    if len(empresas_expositoras) == 0:
        print("No hay empresas expositoras registradas.")
        return
    
    print("\nEmpresas expositoras:")
    for i in range(len(empresas_expositoras)):
        print(f"{i+1}. {empresas_expositoras[i][0]} - Zona: {empresas_expositoras[i][2]} - Puesto: #{empresas_expositoras[i][3]}")
    
    while True:
        try:
            opcion = int(input("Seleccione la empresa a desocupar (número): "))
            if 1 <= opcion <= len(empresas_expositoras):
                empresa = empresas_expositoras[opcion - 1]
                puesto_num = empresa[3]
                
                puestos[puesto_num][2] = False
                puestos[puesto_num][1] = 0
                
                print(f"✓ Puesto #{puesto_num} de la empresa '{empresa[0]}' ha sido desocupado.")
                
                empresas_expositoras.pop(opcion - 1)
                break
            else:
                print("Opción inválida.")
        except ValueError:
            print("Por favor ingrese un número válido.")

def sugerir_puesto():
    while True:
        try:
            num_expositores = int(input("Ingrese el número de expositores: "))
            if num_expositores > 0:
                break
            else:
                print("El número debe ser mayor a 0.")
        except ValueError:
            print("Por favor ingrese un número válido.")
    
    print(f"\nZonas compatibles para {num_expositores} expositores:")
    zonas_compatibles = []
    
    for zona in zonas:
        if zonas[zona]["min"] <= num_expositores <= zonas[zona]["max"]:
            zonas_compatibles.append(zona)
            print(f"  • {zona} (rango: {zonas[zona]['min']}-{zonas[zona]['max']})")
    
    if len(zonas_compatibles) == 0:
        print("No hay zonas compatibles con ese número de expositores.")
    else:
        print("\nDisponibilidad de puestos:")
        for zona in zonas_compatibles:
            ocupados = 0
            disponibles = 0
            for puesto in puestos:
                if puesto[0] == zona:
                    if puesto[2]:
                        ocupados += 1
                    else:
                        disponibles += 1
            print(f"  {zona}: {disponibles} puestos disponibles, {ocupados} ocupados")

def mostrar_porcentaje_ocupacion():
    if len(puestos) == 0:
        print("No hay puestos registrados.")
        return
    
    total_puestos = len(puestos)
    puestos_ocupados = 0
    
    for puesto in puestos:
        if puesto[2]:
            puestos_ocupados += 1
    
    porcentaje = (puestos_ocupados / total_puestos) * 100
    
    print(f"\n=== OCUPACIÓN DE PUESTOS ===")
    print(f"Total de puestos: {total_puestos}")
    print(f"Puestos ocupados: {puestos_ocupados}")
    print(f"Puestos disponibles: {total_puestos - puestos_ocupados}")
    print(f"Porcentaje de ocupación: {porcentaje:.2f}%")
    
    print("\nOcupación por zona:")
    for zona in zonas:
        total_zona = 0
        ocupados_zona = 0
        for puesto in puestos:
            if puesto[0] == zona:
                total_zona += 1
                if puesto[2]:
                    ocupados_zona += 1
        if total_zona > 0:
            porcentaje_zona = (ocupados_zona / total_zona) * 100
            print(f"  {zona}: {ocupados_zona}/{total_zona} ({porcentaje_zona:.2f}%)")

def mostrar_informacion():
    print("\n=== EMPRESAS VISITANTES ===")
    if len(empresas_visitantes) == 0:
        print("No hay empresas visitantes registradas.")
    else:
        for i in range(len(empresas_visitantes)):
            print(f"{i+1}. {empresas_visitantes[i][0]} - Asistentes: {empresas_visitantes[i][1]}")
    
    print("\n=== EMPRESAS EXPOSITORAS ===")
    if len(empresas_expositoras) == 0:
        print("No hay empresas expositoras registradas.")
    else:
        for i in range(len(empresas_expositoras)):
            print(f"{i+1}. {empresas_expositoras[i][0]} - Expositores: {empresas_expositoras[i][1]} - Zona: {empresas_expositoras[i][2]}")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            ingresar_visitante()
        elif opcion == "2":
            ingresar_expositora()
        elif opcion == "3":
            desocupar_puesto()
        elif opcion == "4":
            sugerir_puesto()
        elif opcion == "5":
            mostrar_porcentaje_ocupacion()
        elif opcion == "6":
            mostrar_informacion()
        elif opcion == "0":
            break
        else:
            print("Opción inválida. Intente nuevamente.")
main()