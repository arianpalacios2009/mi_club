#b) Crear el archivo clubCategoria.py con la subclase ClubCategoria (la categoría que ustedes
#quieran, por ejemplo: ClubRecreativo) que hereda de Club:
#Atributos:

#● __socios (lista de socios)
#● actividades (lista de actividades)

#Métodos:

#● getters y setters


from club import Club

class ClubDeportivo(Club):
    def __init__(self, nombre, descripcion, ubicacion, presidente, fecha_fundacion,socios,actividades):
        #llama al constructor del Club
        super().__init__(nombre, descripcion, ubicacion, presidente, fecha_fundacion)
        self.__socios=socios
        self.actividades=actividades


    def get_socios(self):
        return self.__socios
    def get_actividades(self):
        return self.actividades
    
    def set_socios(self,socios):
        self.__socios= socios
    def set_actividades(self,actividades):
        self.actividades=actividades

    def mostrar(self):
        print("Nombre:", self.nombre)
        print("Descripcion:", self.descripcion)
        print("Ubicacion:", self.ubicacion)
        print("Presidente:", self.get_presidente())
        print("Fundacion:", self.get_fecha_fundacion())
        print("socios:",self.__socios)
        print("actividades:",self.actividades)


    #Incorporar la funcionalidad para registrar nuevos socios dentro de la categoría correspondiente.

    def registrar_socios(self,socio):
        self.__socios.append(socio)
        print("se agrego socio")

    #Obtener la cantidad total de socios registrados en la categoría.

    def cantidad_socio(self):
        return len(self.__socios)      


    #Permitir agregar nuevas actividades deportivas, recreativas o culturales ofrecidas por el club.
    
    def actividad_nueva(self,actividad):
        self.actividades.append(actividad)
        print("agregando actividad nueva")
        
    #Mostrar un listado completo de las actividades que se realizan en la categoría.

    def mostrar_actividades(self):
        for i in self.actividades:
            print(i)
        

   

club_boca = ClubDeportivo("Boca juniors","Gigante del fútbol mundial, apodado Xeneize. Famoso por su estadio La Bombonera y su enorme identidad popular.","Barrio de La Boca, Buenos Aires, Argentina ","Juan Román Riquelme","3 de abril de 1905",264,000)
club_boca.mostrar()
