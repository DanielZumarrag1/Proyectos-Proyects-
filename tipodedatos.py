# Strings

# No es lo mismo "Hola Mundo" que "hola mundo" (cuando escribamos codigo hay que prestar atencion  
# en la manera en que se escribe el codigo).
# (no hay que menospreciarlo) (esto hace que tu programa sea mejor o peor).
# Un string tambien puede ir en comillas simples. (podemos crear strings con comilla o dobles comillas).
# Tambien se puden usar triples comillas y triples dobles comillas (cada aspecto importa).
# Siempre hay que pasar a print cualquier info para que lo imprima en pantalla.
# Para unir dos strings se usa el simbolo (+).
# Todo esto que esta abajo son strings:

print ("Hola Mundo")
print ("hola mundo")
print ('Hola Mundo')
print ('''Hola Mundo''')
print ("""Hola Mundo""") 
print (type ("Hola Mundo"))

print ("hola" + "mundo y otras galaxias")


#Numeros

# 10, 20 o 30 son numeros enteros.
# 30 es tipo de dato entero y 30.5 un tipo de dato decimal.
# Los decimales en computacion se conocen como flotantes (floats).

#Enteros:

print (30)

#Flotantes (Floats):

print (30.5)

#Boolean (Booleanos):

#Sirve para definir tipos de estados.
#Son palabras reservadas (si las escribes en un programas python la va a entender como tipo de datos logicos).

True
False

# Listas (Lists):

# Es una lista de datos que se pueden agrupar unos a otros.
# Para hacer que python entienda que los datos son distintos se los separa por comas (,).
# Tambien se puede crear listas de textos.
# Se puede conbinar listas de strings entre numeros y letras.
# Tambien se pueden crear listas vacias.

[10, 20, 30, 40, 50]
[10, 20, 30, 40, 60] # [Ejemplo de cambio de numeros (el numero 50 se cambio por el 60)]. 
['Hola Mundo', 'Adios Mundo', 'Como va Mundo'] 
["Hola Mundo", True, 10, 10.5]
[] # (Esta es una lista que no tiene elementos, esta vacia en resumen)


# Tuplas (Tuples):
# Es muy similar a una lista porque tambien agrupa datos pero por lo general las usamos para datos que no cambian:
# (Cuando tenemos una lista podemos cambiar sus datos).
# No se puede cambiar la lista (si ya la definiste una vez, va a estar asi para siempre) (Tambien se lo conoce como inmutable).
# Tambien se puede crear una tupla vacia.

# IMPORTANTE: (Si una lista la definimos con corchetes una tupla la definimos con parentesis).

(10, 20, 30, 40)
() # (Esta es una tupla vacia).


# Diccionarios (Dictionaries):

# Los diccionarios te permiten agrupar datos pero que pertenecen a una misma entidad con un nombre clave.
# Aqui tenemos tres datos, pero pertenecen a la misma persona.
# Lo que esta antes de los dos puntos se lo conoce como clave (key) y lo que esta despues como valor (value).
# Escribir none es como decirle a python que lo que vemos a utilizar no esta definido aun por algun tipo de dato (y lo podemos ver por
# pantalla).


print(type({
    "Nombre_de_la_persona":"Walter",                                                                                                                                                                                                                                                                  
    "Appellido":"White",
    "Apodo":"Walt"
}))

None