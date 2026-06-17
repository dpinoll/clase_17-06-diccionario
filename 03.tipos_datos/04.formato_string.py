# utilizar tecnicas para unir string en un solo 
## concatenacion 
## para usar el operador de concatenacion +
# cuando este operador se encuentra entre dos textos se convierte en el operador de concatenacion y cuando esta entre dos numeros en el operador de adicion (suma)
nombre:str ="noemi"
apellido:str ="noseprofesor"
nombre_apellido:str = nombre+" "+apellido #correcto con espacio en el medio
print(nombre_apellido) # salida: noemi noseprofesor

## opcion mas optima de concatenar
print(nombre,apellido) #forma de separar un nombre y apellido

## f-string (tarea)

# formato de string esto sirve para formatear string con variables de python y para esto se requiere de una f antes de escribir un string, si se desea incluir codigo python en el string se debe encerrar entre llaves{}
nombre:str = "Gianfranca"
edad:int = 14
# mensaje de salida me diga hola mi nombre es {} y tengo{}
print(f"hola mi nombres es {nombre} y tengo {edad}")

## plantillas de string
nombre_cliente:str=input("ingresa tu nombre: ")
ruc_cliente:int=input("ingresa ruc: ")
direccion_cliente:str=input("digite direccion: ")
codigo_producto:str=input("ingrese codigo: ")
nombre_producto:str=input("ingrese nombreproducto: ")
precio_producto:float=input("el precio del producto: ")
cantidad_producto:float=float(input("cantidad a comprar: "))
precio_total:float=precio_unidad*cantidad_producto 

plantilla:str=f"""
cliente: {nombre_cliente}........ruc: {ruc_cliente}
direccion: {dieccion_cliente}
codigo producto      |  nombre producto    |  p_unidad      |  cantidad
............................................................................
{codigo_producto}   {nombre_producto}   {precio_unidad}  {cantidad_producto}
.............................................................................
el precio total de su compra es de: {precio_total}
"""
print(plantilla)