# para declarar una variable en python usaremos la convencion snake_case 
## REGLAS
### 1. el nombre de la variable debe indicar que dato se esta almacenando
### 2. las variables no deben contener numeros ni caracteres especiales (@,/,!,?)
nombre_curso="lenguaje de programacion"
creditos_curso=3
horas_semnales_curso=6
# ADVERTENCIA - las variables son multables
print(creditos_curso) #salida:
creditos_curso=10
print(creditos_curso) #salida:
# NOTA IMPORTANTE PARA TODO EL CURSO - cada vez que declaramos variables usaremos anotaciones para indicar que tipo de dato se va a almacenar 
nombre_alumno:str = "deduardo"
edad_alumno: int =28
estatura_alumno:float = 1.59
asistencia_alumno:bool = True
amigos_alumno:list = []
direccion_alumno: dict = {
    "n_calle":"psj belen",
    "numero:casa":230,
    "barrio":"ccayao"
    }

#asignacion de una variable a otra variable
edad_alumno:int=20
edad_docente:int=edad_alumno


## impotartante no olvudarse 
### un decorador en python nos indica que tipo de dato va a almacenar nuestra variable
### los decoradores que python trae por defecto son:
######## datos primitivos ########
# decoradores para datos primitivos
### :int - enteros
### :float - decimales,coma flotante
### :str - string texto
### :bool - datos boleano true o false 

######## datos estructurados ########
# decoradores para datos estructurados
### :list - listas
### :dict - diccionarios

## como hacemos uso de las variables
## para hacer uso del dato almacenado en una variable basta hacer el llamado del nombre de la variable 
primer_numero:int = 30
segundo_numero:int = 20
suma:int = primer_numero+segundo_numero

