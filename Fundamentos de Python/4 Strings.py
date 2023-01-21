#Se hace un analisis más profundo del tipo de dato String

name = "Sebastian" #Se puede usar comillas dobles
last_name = 'Avendaño' #Como también se puede usar comillas simples
#NOTA: se abre y cierra con el mismo tipo de comillas:(" ") o (' ')

#Concatenación de cadenas de texto uniendo varias variables
full_name = name + last_name 
'''Si se quisiera imprimir la variable 'full_name', se mostraría
algo como SebastianAvendaño, para solucionar el espacio que falta
entre la dos variables, se recomienda concatenar un espacio entre
las variables, de la siguiente manera:
'''
full_name = name + " " + last_name

#--------------------------#
'''
Para los casos en que se utiliza comillas dobles o simples dentro
de una cadena de texto, se debe tener en cuenta que en ocasiones se
pueden generar errores, ejemplo:
quote = 'I'm Sebastian' => En este caso el sistema considera que se
están cerrando las comillas justo después de la I y no al final del
nombre, lo que genera un error de sintasis. Para evitar esto, se debe
combinar las comillas dobles con las simples, así:
quote = "I'm Sebastian"
quote2 = "She said "Hello"" => genera error
quote2 = 'She said "Hello"'=> no geera error
'''
#--------------------------#
'''
Format: existen varias maneras de concatener cadenas de texto llegando
a obtener el mismo resultado, de la siguiente manera:
'''
# Forma 1: usando el operador +
template = "hola, mi nombre es " + name + " y mi apellido es " + last_name
print(template)

# Forma 2: usando {} para las variables y asignando un valor a cada llave con .format
template = "Hola, mi nombre es {} y mi apellido es {}".format(name, last_name)
#Reemplaza los valores en el orden en que estos se colocan

# Forma 3: usando una f al inicio y {nombre variable} para la concatenación
template = f"Hola, mi nombre es {name} y mi apellido es {last_name}"


