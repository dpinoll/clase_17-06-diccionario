# DICCIONARIOS📒
Los diccionarios son la forma mas comun de almacenar datos estructurados de objetos que nos rodea en el mundo al igual que las listas que guardan informacion en `elementos`, de igual manera los diccionarios almacenan sus datos en `elementos`,separados por comas.
La diferencia es que las listas almacenan los elementos por `indice` y `valor`.
Y los diccionarios almacenan los elemntos por `clave valor`.
**ejemplo:**
```python
vocales:list[str]=['a','e','i','o','u']#valores
# indice            0   1   2   3   4
# un elemento en una lista esta conformado por dos cositas el indice y su  valor
# para acceder a un valor en una lista
vocales[2]# 1
alumno:dict={'nombre':'eduardo','edad':40}
# elemento en un diccionario esta conformado por clave valor
# para acceder a un diccionario
alumno["nombre"]# eduardo
```
## ACCEDE A ELEMENTOS👀
- **por clave(forma directo)**
```python 
persona;dict={
    "nombre":"celia",
    "edad":16,
    "ciudad":"cabo verde",
    "email":"celi@email.com"
}
print(persona["edad"])# 16
print(persona["email"])#celi@email.com
```
- **por su metodo (forma mas segura)**
```python
persona;dict={
    "nombre":"celia",
    "edad":16,
    "ciudad":"cabo verde",
    "email":"celi@email.com"
}
print(persona.get("nombre"))# celia
# la diferencia de este metodo es que nos permite manejar errores.
print(persona.get("telefono"))# nome
print(persona.get("telefono","no disponible"))# si la clave telefono  no existe no mostrara nome sino el segundo parametro que le pasemos al metodo get.
```
## MODIFICAR ELEMENTOS🛠️
**cambiar un valor existente**
```python
persona;dict={
    "nombre":"celia",
    "edad":16,  
}
persona["edad"]=19
#agregar una nueva clave valor.
persona["carrera"]="agro"
# si la clave no existe se crea automaticamente. si existe se actualiza.
```
## AGREGAR/ACTUALIZAR MULTIPLES ELEMENTOS🔄️
para esto tenemos que hacer uso de el metodo `.update`
se puede agregar si lo partes de `clave valor`no existe y actualizar si el `clave valor`existe.
```python
tienda:dict[str:str|int]={
    "razon_social":"bigote"
    "ruc":20465783674
}
#actializar usando el metodo .update tengo dos maneras
# 1. diccionarios
tienda.update({"ruc":20465783674,"telefono":987654321})
# 2. pares clave=valor
tienda.update(h_atencion="g-12",gerencia="kevin")
```
## ELIMINAR ELEMENTOS🧹
```PYTHON
tienda:dict[str:str|int]={
    "razon_social":"bigote"
    "ruc":20465783674
}
el_eliminado=tienda.pop("ruc")
tienda.popitem()# eliminar el ultimo elemento
# para limpiar todo el diccionario
tienda.clear()
```