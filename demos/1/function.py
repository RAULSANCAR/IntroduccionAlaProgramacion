# VARIABLE SALUDAR
def saludar(nombreCompleto): # Definición de variable
    return "Hola {} {} Bienvenido al Juego de Cody".format(nombre,apellido) # Resultado de la variable
print("Ingresa sólo tu nombre") # Mensaje que pide nombre al usuario.
nombre = input() # Caja almacenadora de variable
print("ingresa tu apellido ó apellidos") # Mensaje que pide apellido o apellidos al usuario.
apellido = input() # Caja almacenadora de variable
nombreCompleto = nombre + " " + apellido # Concatenación de las variables
print(saludar(nombreCompleto)) # Rasultado de la variable
