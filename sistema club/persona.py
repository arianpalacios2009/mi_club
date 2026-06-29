#c) Crear el archivo persona.py con la clase Persona:
#Atributos:

#● nombre_completo
#● edad
#● __tipo_identificacion (DNI, Pasaporte, Cédula de identidad)
#● __identificacion
#● __nacionalidad

#Métodos:

#● mostrar_datos()
#● getters y setters

class Persona():
    def __init__(self,nombre_completo,edad,tipo_identificacion,identificacion,nacionalidad):
        self.nombre=nombre_completo
        self.edad=edad
        
        #atributos privado
        self.__tipo_identificacion=tipo_identificacion
        self.__identificacion=identificacion
        self.__nacionalidad=nacionalidad
        
        

    #getters    
    def get_tipo_identificacion(self):
        return self.__tipo_identificacion
    
    def get_identificacion(self):
        return self.__identificacion
    
    def get_nacionalidad(self):
        return self.__nacionalidad
    
    #setters
    
    def set_tipo_identificacion(self,tipo_identificacion):
        self._tipo_identificacion=tipo_identificacion
        
    def set_identificacion(self,identificacion):
        self.__identificacion=identificacion
        
    def set_nacionalidad(self,nacionalidad):
        self.__nacionalidad=nacionalidad
        
        
    def mostrar_datos(self):
        print("nombre_completo: ",self.nombre)
        print("edad: ",self.edad)
        print("tipo_identificacion: ",self.get_identificacion())
        print("identificacion: ",self.get_identificacion())
        print("nacionalidad: ",self.get_nacionalidad())
        
        
persona=Persona("juan","30","Dni ","32.400.127","Argentina")
persona.mostrar_datos()