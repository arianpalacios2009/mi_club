
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
    def __init__(self,nombre,descripcion,ubicacion,existencia,presidente,fecha_fundacion):

        self.nombre = nombre
        self.descripcion = descripcion
        self.ubicacion = ubicacion
        self.existencia=existencia
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
        
        
    #Determinar si el club puede considerarse una institución histórica, entendiendo como tal a aquellas que tengan más de 50 años de existencia.

    def determinar_club(self):
        if self.existencia>=50:
            print("es una institucion historica")
        else:
            print("no es una institucion historica")
        
        

club1 = Club("boca juniors","xeneize"," Ciudad Autónoma de Buenos Aires",121,"juan roman riquelme"," 3 de abril de 1905.")
club1.mostrar_info()
club1.determinar_club()
