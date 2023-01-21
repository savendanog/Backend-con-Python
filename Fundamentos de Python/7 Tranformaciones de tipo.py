'''Se puede hacer la conversión de un tipo de dato a otro tipo
de dato: un entero a un string, un string a un booleano,
un flotante a un entero, etc.
'''
name = "Sebastian" #Es de tipo string
name = 12 #Se transforma de manera dinámica el tipo de dato a entero
name = True #Ahora la variable es de tipo booleana

print("Sebastian" + " Avendaño") #En este caso concatena las cadenas de texto
print(10 + 20) #Acá, el sistema, al tener datos numericos, realiza la suma
print("Sebastian" + 20) #El sistema arroja error al querer realizar una
                        #operación con tipos de datos diferentes
print("Sebastian" + "20") #"20" se considera un string, por lo que en esta
                          #ocasión, concatena las dos cadenas de texto

#Una manera más práctica, es transformar el tipo de dato:

#La notación 'str' permite convertir el valor dentro del parentesis a una
#cadena de texto:
age = 30 #Es de tipo entero(int)
print("Mi edad es " + str(age))
#La función format hace la tranformación automaticamente:
print(f"Mi edad es {age}")

#La función input captura todos los datos de tipo string:
age = input("Ingresa tu edad => ") #El valor ingresado se guarda como string
#Para convertirlo, sólo se debe usar la notación 'int()', así:
age = int(age) #De esta manera, el dato ya será de tipo entero
#La conversión tambien se puede hacer directamente desde el input:
age = int(input("Ingresa tu edad => "))

#NOTA: si el valor ingresado es texto, al tratar de hacer la conversión
#el sistema arrojará un error al no poder transformar el tipo de dato