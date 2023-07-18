# Ejercicio de comparación.
# ¿Eres mayor de edad?
print("¿Eres mayor de edad?") # Titulo del ejercicio.
print("Ingresa tu edad, por favor.") # Se le pide al usuario que ingrese su edad.
edad01 = int(input()) # Caja receptora de valor.
if edad01 > 18: # Comparación.
    print ("Eres mayor de edad, puedes continuar.") # Mensaje para continuar.
else: # De lo contrario.
    print ("Eres menor de edad, no puedes continuar.") # Mensaje de restricción.

# ¿Eres menor de edad?
print("¿Eres menor de edad?") # Titulo del ejercicio.
print("Ingresa tu edad, por favor.") # Se le pide al usuario que ingrese su edad.
edad02 = int(input()) # Caja receptora de valor.
if edad02 < 18:
    print ("Eres menor de edad, puedes continuar.") # Mensaje para continuar.
else: # De lo contrario.
    print ("Eres mayor de edad, no puedes continuar.") # Mensaje de restricción.
