import statistics

datos = [10, 20, 30, 40, 50]

print("--- Analisis de datos ---")
print("Promedio:", statistics.mean(datos))
print("Mediana:", statistics.median(datos))
print("Desv. estandar:", round(statistics.stdev(datos), 2))