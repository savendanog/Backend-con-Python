'''Tipo de dato Booleano:
Viene de la estructura binaria de ceros y unos.
Tiene solo dos estados: verdadero (True) o falso (False).
'''
is_single = False #Siempre debe iniciar con mayuscula.

#Se puede invertir el valor de una variable booleana con la
#notación not, así:
print(not True) #Imprime el valor False
print(not False) #Imprime el valor True

#Se puede aplicar a variables:
is_single = not is_single #El valor de la variable será True
is_married = not is_single #Se le puede asignar a otra variable