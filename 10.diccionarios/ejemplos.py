#modulos y librerias estadar 
# libreria estandar typing tipar datos a list y diccionarios para hacer mas optimo el codigo
#modulo es una porcion de codigo utilizable para poder usarlo nesecitamos importa la parte del codigo que deseamos utilizar
# union me permite tipar una coleccion de tipos, que si no sabes el tipo de dato con union le podemos pasar una lista de los posibles tipos de datos que puede tener mi valor
from typing import Union 
# sin libreria 
# alumno dict[str|int]
alumno:dict[str:Union[str,int,float,bool]]={
    "id_alumno":1,
    "dni":78483973,
    "nombre":"mio",
    "edad":20,
    "matricula":True
}
# acceder 
## clasica
print(alumno["dni"])
# codigo erroneo print(alumno["tricula"])
# metodos 
print(alumno.get("edad","valor no encontrado"))
# crear, modificar
print(alumno)
alumno["nombre"]="otro"# si existe la clave actualiza el valor
alumno["ruc"]=75216631463# si no existe la clave lo creamos
print(alumno)
# crear, modificar varios
alumno.update({"nombre":"celia","edad":15})
alumno.update({"carrera":"agro","semestre":"iii"})
print(alumno)
# eliminar
eliminado=alumno.pop("carrera")
print(f"el elemento eliminado es: (eliminado)")
print(f"mi nuevo diccionario: (alumno)")