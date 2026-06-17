## en poo todo es un objeto y en programacion un objeto es una clase
class mensaje:
    def __init__(self,txt):
        self.texto=txt
    
    def saludar(self):
        print("holaaa")
saludo1=mensaje("hola mundo")
print(saludo1.saludar())