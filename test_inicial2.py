pareja_autora = input("Introduce los nombres de los componentes de la pareja: ").strip()
portatil = input("Introduce el nombre del dispositivo auditado : ").strip()
vatios = input("Introduce la  potencia en vatios: ").strip()
potencia = float(vatios)
result = potencia * 24
print(f"--- INFORME PARA: {pareja_autora.upper()}---")
print(f"El consumo registrado es de {result}Wh.")