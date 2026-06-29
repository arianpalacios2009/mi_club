
#a) Crear el archivo club.py con la clase Club:
#Atributos:

#● nombre
#● descripcion
#● ubicacion
#● __presidente
#● __fecha_fundacion

#Métodos:

#● mostrar_info()
#● getters y setters





class Club:
    def __init__(self,nombre,descripcion,ubicacion,presidente,fecha_fundacion):

        self.nombre = nombre
        self.descripcion = descripcion
        self.ubicacion = ubicacion

        #atributos privados
        self.__presidente = presidente
        self.__fecha_fundacion = fecha_fundacion

    
    #getters
    def get_presidente(self):
        return self.__presidente 

    def get_fecha_fundacion(self):
        return self.__fecha_fundacion

    #setters
    def set_presidente(self, presidente):
        self.__presidente = presidente

    def set_fecha_fundacion(self, fecha):
        self.__fecha_fundacion = fecha
        
    def mostrar_info(self):
        print("Nombre:", self.nombre)
        print("Descripcion:", self.descripcion)
        print("Ubicacion:", self.ubicacion)
        print("Presidente:", self.get_presidente())
        print("Fundacion:", self.get_fecha_fundacion())

club1 = Club("boca juniors","xeneize"," Ciudad Autónoma de Buenos Aires","juan roman riquelme"," 3 de abril de 1905.")
club1.mostrar_info()
