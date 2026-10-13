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
    
    # Validación robusta de la opción introducida
    try:
        opcion = int(entrada)
    except ValueError:
        print("⚠️ Error: Debe introducir un número entero.")
        continue
    
    if opcion == 1:
        print("\n[OPCIÓN 1] Iniciando proceso de auditoría...")
        iter_str = input("Introduce iteraciones: ").strip()
        try:
            iteraciones = int(iter_str)
            if iteraciones > 0:
                print(f"Configurado con éxito para {iter_str} iteraciones")
            else: 
                print("El valor tiene que ser mayor que 0")
        except ValueError:
            print("Error de formato: debe introducir un número entero")
    
    elif opcion == 2:
        print("\n[OPCIÓN 2] Consultando registros históricos...")
    
    elif opcion == 3:
        print("\nSaliendo de EcoAudit CLI. ¡Hasta pronto!")
        break
    
    else:
        print("⚠️ Opción no válida. Elija un número entre 1 y 3.")