# =====================================================================
# EcoAudit CLI - Módulo Principal
# Autores: [Nombre Alumno 1] & [Nombre Alumno 2]
# =====================================================================

while True:
    print("\n=========================================")
    print(" 🌿 ECOAUDIT CLI - MENÚ PRINCIPAL 🌿 ")
    print("=========================================")
    print("1. Realizar nueva auditoría")
    print("2. Consultar histórico")
    print("3. Salir")
    
    entrada = input("\nSeleccione una opción (1-3): ").strip()
    
   
    try:
        opcion = int(entrada)
    except ValueError:
        print("⚠️ Error: Debe introducir un número entero.")
        continue
    
    if opcion == 1:
        print("\n--- AUDITORÍA ENERGÉTICA ---")
        proceso = input("Nombre del equipo/proceso: ").strip()
        
        # Validación de la potencia
        try:
            potencia = float(input("Potencia consumida en Vatios (W): "))
            if potencia < 0:
                print("⚠️ Error: La potencia no puede ser negativa.")
                continue
        except ValueError:
            print("⚠️ Error: Debe introducir un número válido para la potencia.")
            continue
            
        # Validación de las horas
        try:
            horas = float(input("Horas de uso diario: "))
            if horas < 0:
                print("⚠️ Error: Las horas no pueden ser negativas.")
                continue
        except ValueError:
            print("⚠️ Error: Debe introducir un número válido para las horas.")
            continue
            
        iter_str = input("Introduce iteraciones: ").strip()
       
        # Validación de las iteraciones
        try:
            iteraciones = int(iter_str)
            if iteraciones <= 0:
                print("⚠️ El valor debe ser mayor que 0.")
                continue
        except ValueError:
            print("⚠️ Error de formato: debe introducir un número entero.")
            continue

        # Realizar cálculos con las variables convertidas de forma segura
        consumo = estimar_consumo_wh(potencia, horas, iteraciones)
        huella = calcular_huella_co2(consumo)

        print(f"\n✅ Resultados calculados para '{proceso}':")
        print(f"   • Consumo total: {consumo:.2f} Wh")
        print(f"   • Huella de carbono estimada: {huella:.4f} g CO2")
        print("\n[OPCIÓN 1] Iniciando proceso de auditoría...")
        print(f"Configurado con éxito para {iteraciones} iteraciones")
        
    elif opcion == 2:
        print("\n[OPCIÓN 2] Consultando registros históricos...")
    
    elif opcion == 3:
        print("\nSaliendo de EcoAudit CLI. ¡Hasta pronto!")
        break
    
    else:
        print("⚠️ Opción no válida. Elija un número entre 1 y 3.")