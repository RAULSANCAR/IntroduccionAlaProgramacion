# Arreglo edades, asignando los valores
edades = [34, 15, 20, 9, 50, 32, 31, 12, 23, 18]
# Arreglo mayores, inicializado
mayores = []
# Arreglo menores, inicializado
menores = []
# Recorriendo el arreglo edades con un for, validando si la edad es mayor o igual a 18 y guardando el resultado en el arreglo correspondiente
for edad in edades:
    if edad >= 18:
        mayores.append(edad)
    else:
        menores.append(edad)
# Imprimiendo los arreglos resultantes
print("Mayores de edad: ", mayores)
print("Menores de edad: ", menores)

