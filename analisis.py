import statistics

datos = [10, 20, 30, 40, 50]

print("--- Analisis de datos ---")
print("Promedio:", statistics.mean(datos))
print("Mediana:", statistics.median(datos))
print("Desv. estandar:", round(statistics.stdev(datos), 2))

def limpiar_datos(lista):
    """Elimina valores negativos y nulos de la lista."""
    return [x for x in lista if x is not None and x > 0]

datos_sucios = [10, -5, None, 30, 0, 50, None, 20]
datos_limpios = limpiar_datos(datos_sucios)

print("\n--- Limpieza de datos ---")
print("Datos originales:", datos_sucios)
print("Datos limpios:   ", datos_limpios)

def calcular_rango(lista):
    """Devuelve el rango (max - min) de la lista."""
    return max(lista) - min(lista)

print("\n--- Rango ---")
print("Rango de datos limpios:", calcular_rango(datos_limpios))