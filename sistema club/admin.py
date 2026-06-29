#e) Crear el archivo admin.py con la clase Administrador:

#Atributos:

#● nombre
#■ __usuario
#● __contraseña

#Métodos:

#● getters y setters

class Administrador:
    def __init__(self,nombre,usuario,contrasena):
        self.nombre=nombre
        
        #atributos privados
        self.__usuario=usuario
        self.__contrasena=contrasena
        
    def get__usuario(self):
        return self.__usuario
    
    def get__contrasena(self):
        return self.__contrasena
    
    def set_usuario(self,usuario):
        self.__usuario=usuario
        
    def set_contrasena(self,contrasena):
        self.__contrasena=contrasena
        
admin=Administrador("tiziano","tizi123","87654321")
