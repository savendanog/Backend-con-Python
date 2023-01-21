'''
Python tiene reglas claras definidas para los numeros.
Para declarar un número en una variable, estos deben ir sin
comillas para que el sistema no los tome como un string.
Nota: es muy buena practica dar nombres a las variables que
sean dicientes sobre lo que se está almacenando dentro de estas.
'''
#
# Existen varias clases de numeros:
# 1) Enteros:
lives = 3
age = 30
budget = 100

# 2) Flotantes:
temperature = 12.12
PI = 3.14

'''También es permitido declarar variables realizando operaciones
dentro de esta, de la siguiente manera:'''
lives = 3 + 1

#Se puede usar la misma variable para realizar operaciones:
lives = lives - 1
#Una forma más abreviada para realizar la operación anterior es:
lives -=1 #Para operaciones de decremento
lives +=2 ##Para operaciones de incremento en la cantidad deseada

#Cuando se tienen numeros muy grandes, al imprimirlos, Python
#mostrara el valor en notación cientifica
number = 45000000000000000000000000000000.1
print(number) #Imprime el numero 4.5e+31

#Lo mismo sucede con numeros muy pequeños
number = 0.00000000000000000000000000005
print(number) #Imprime el numero 5e-29

###################
'''
Ejercicio propuesto:
Programa para calcular el promedio de gastos de varios
meses. Se deben declarar las variables con los gastos
de cada mes y una ultima, que sume los gastos de los
meses y promedie dicho valor.
'''
gastos_enero = 1200
gastos_febrero = 1800
gastos_marzo = 1450
promedio_gastos = (gastos_enero + gastos_febrero + gastos_marzo)/3
print(promedio_gastos)
#Como resultado muestra el numero 1483.3333333333333



