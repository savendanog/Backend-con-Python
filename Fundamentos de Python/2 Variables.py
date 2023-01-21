'''
Las variables se pueden considerar como cajas en
las que almaceno elementos y a dichas cajas les 
asigno un nombre para identificar lo que almaceno
en estas.
'''
'''Para declarar una variable, se le asigna un nombre
y con un igual se le asigna un valor
'''
my_name = "Sebas"
print(my_name)

my_age = 30
print(my_age)

#Se puede modificiar el valor de una variable
my_name="Sebastian"

'''En la función print podemos concatener variables
con texto y con otras variables. También se pueden
realizar operaciones aritmeticas
'''
print("Mi nombre es", my_name)

'''Para guardar un valor solicitado dentro de una
variable, se usa la función input
'''
my_name = input("Cual es tu nombre? ")
print("El valor ingresado es:", my_name)

my_lastname = input("Cual es tu apellido? ")
print("El valor ingresado es:", my_lastname)

print("Tu nombre completo es:", my_name, my_lastname)
