# Arreglo alumnos, inicializado
alumnos = []
# Arreglo nombres con los siguientes valores
nombres = ["Mario", "José", "Laura", "Carmen", "Pedro"]
# Arreglo promedios con los siguientes valores
promedios = [9, 5, 7, 3, 10]
# Arreglo pagos con los siguientes valores
pagos = [True, True, False, True, False]
# Recorriendo los arreglos con un for, usando la variable index y la funsión range
for index in range(5):
	# Validando si el promedio actual es mayor a 5 y que el pago sea verdadero
	if promedios[index] > 5 and pagos[index]:
        # Validando si la condición se cumple, guardando el nombre actual en el arreglo alumnos
         alumnos.append(nombres[index])
# Imprimiendo el arreglo alumnos
print(alumnos)
