# metodo para convertir un texto en mayuscula
texto_minuscula:str="hola"
print(texto_minuscula.upper())
# metodo para convertir un texto en minusculas
texto_mayuscula:str="HOLASSS"
print(texto_mayuscula.lower())
# metodo para convertir solo la primer letra en mayuscula
texto:str="buenos dias"
print(texto.capitalize())
# metodo para convertir la primera letra de cada palabra en mayuscula como un titulo
print(texto.title())

# metodos para quitar espacios
texto_espacios:str="     oso      "
print(texto_espacios)
# este metodo quita los espacios que estan a la derecha e izquierda. si deseamos quitar solo los espacios de la izquierda usamos el metodo **lstrip()** y si deseamos solo quitar de la derecha usamos **rstrip()**
print(texto_espacios.lstrip())

# metodo para buscar un caracter o conjunto de caracteres
#find retorna al indice donde comieza el texto a buscar si el texto no se encuentra retornara -1
parrafo:str="mi mama me ama yo amo a mi mama de gianfranco"
print(parrafo.find("gianfranco"))
print(parrafo[35:])

# metodo para remplazar una parte del texto 
texto_incorrecto:str="gianfranco es malo"
print(texto_incorrecto.replace("malo","bueno"))

# (metodo) operador binario de existencia 
#este operador verifica si cierto texto existe o no dentro de otro retorno true si exixte y false si no
vocales:str="aeiouAEIOU"
print("c" in vocales)

#tarea( que son y cuales son los operadore unarios,binarios,ternarios)

#ternario 
print("es verdad"if 20>18 else"es falso")

##realizar un programa que nos pida la contraseña si la contraseña es correcta el usuario podra ingresar caso contrario le dara un mensaje de contraseña incorrecta

password_use:str=input("ingresa tu contraseña:")
