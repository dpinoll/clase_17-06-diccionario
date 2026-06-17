# este tipo de datos sirve para almacenar informacion de tipo de teto, puede ser texto simple o texto extenso.
# para almacenar un dato de tipo texto la informacion debera estar encerrada entre comillas ("",'',"""""")
## - comillas dobles ("")
## - comillas simples ('')
## - docstring ("""""")
nombre_instituto:str="IESTP-JMA"
nombre_curso:str='lenguaje de pro.'
descripcion_curso:str="""
el curso de "lenfuaje de programacion", 
tiene una duracion de un semestre educativo con 6 horas semanales y
 aprendera a programar en el lenguaje
 "python"
 """

## los string tienes funciones basicas para poder interactuar con los datos que estamos almacenando 
## la estructura de una funcion 
## nombre_funcion(parametros)
## *argumento - es un valor que se le pasa a una funcion que en base a su programacion retornara otro valor distinto al pasado por el argumento 
# funcion para mostrar informacion por terminal
print("hola mundo") # salida: hola mundo
print("hola","mundo") # salida: hola mundo
 
 # funcion para mostrar la cantidad de caracteres que tiene un string-texto
texto:str = "soy deduardo"
cantidad_caracteres:int = len (texto)
print("cantidad de caracteres:",cantidad_caracteres)

# forma de acceder a un caracter en especial 
## para esto hacemos uso de la notaciones de corchetes[]
## para esto tenemos que entender que python asigna a cada caracter con un indice de base cero

# ejemplo: celia
# indices  01234
nombre_celia:str = "celia"
print(nombre_celia)
print(nombre_celia[2])

# troceado de texto
## para esto se utiliza la notacion de corchetes con la diferencia que se debe indicar un indicar inicial y un indice final del texto a extraer
## texto[i_indice:i_final]
vocales:str = "aeiou"
print(vocales[1:3])
print(vocales[3:])
print(vocales[0:3]) 