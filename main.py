from calculadora import estimar_consumo_wh, calcular_huella_co2

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
        # SIMULACIÓN ITERATIVA PASO A PASO (PARA INSPECCIÓN EN DEPURADOR)
        print("\nIniciando simulación ciclo a ciclo...")
        consumo_ciclo = estimar_consumo_wh(potencia, horas, 1) # Consumo de un solo ciclo
        consumo_acumulado = 0.0
        ciclo = 1

        while ciclo <= iteraciones:
          consumo_acumulado = consumo_acumulado + consumo_ciclo # <--- PONDRÉIS AQUÍ EL PUNTO ROJO
          print(f" [Ciclo {ciclo}] Consumo acumulado parcial: {consumo_acumulado:.2f} Wh")
          ciclo = ciclo + 1

        print(f"\n✅ Resultados calculados para '{proceso}':")
        print(f"   • Consumo total: {consumo:.2f} Wh")
        print(f"   • Huella de carbono estimada: {huella:.4f} g CO2")
        print("\n[OPCIÓN 1] Iniciando proceso de auditoría...")
        print(f"Configurado con éxito para {iteraciones} iteraciones")
                # Guardado persistente en el archivo CSV
        with open("auditorias.csv", mode="a", encoding="utf-8") as archivo:
            # Escribimos los datos separados por comas y terminamos con salto de línea (\n)
            archivo.write(f"{proceso},{potencia},{horas},{iteraciones},{consumo:.2f},{huella:.4f}\n")
        print("💾 Registro guardado con éxito en 'auditorias.csv'.")
        
    elif opcion == 2:
        print("\n[OPCIÓN 2] Consultando registros históricos...")
        print("\n================ HISTORIAL DE AUDITORÍAS ================")
        try:
            with open("auditorias.csv", mode="r", encoding="utf-8") as archivo:
                contenido = archivo.read()
                print(contenido)
        except FileNotFoundError:
            print("ℹ️ Aún no existen registros. Realiza una auditoría primero.")
    
    elif opcion == 3:
        print("\nSaliendo de EcoAudit CLI. ¡Hasta pronto!")
        break
    else:
        print("⚠️ Opción no válida. Elija un número entre 1 y 3.")