#f) Crear el archivo cuota.py con la clase Cuota:
#Atributos:

#● __estado (pagada, pendiente, vencida)
#● fecha_de_vencimiento
#● periodo (mes/año)

#Métodos:

#● getters y setters
from datetime import date



class Cuota:
    def __init__(self,estado,fecha_de_vencimiento,periodo):
        self.estado=estado
        self.fecha_de_vencimiento=fecha_de_vencimiento
        self.periodo=periodo
        
    def get_estado(self):
        return self.estado
    
    def set_estado(self,estado):
        self.estado=estado
    
    def mostrar(self):
        print("estado: ",self.estado)
        print("fecha de nacimiento: ",self.fecha_de_vencimiento)
        print("periodo: ",self.periodo)
        
    #Registrar una cuota como pagada.
    def pagar_cuota(self):
        self.estado="pagada"
        print("la cuota esta pagada")
    
    def determinar(self):
        hoy = date.today()
        if hoy > self.fecha_de_vencimiento:
            self.estado = "vencida"
            return True
        else:
            return False
    
#Actualizar automáticamente el estado de la cuota cuando corresponda.
    def actualizar_estado(self):
        if self.determinar():
            self.estado = "vencida"
    
    
#Informar cuántos días faltan para el vencimiento de una cuota.
    def informar_dias_faltantes(self):
        hoy = date.today()
        if hoy > self.fecha_de_vencimiento:
            self    
    
pagar=Cuota("pendiente", date(2026,8,1), "08/2026")
pagar.mostrar()
pagar.set_estado("pagada")
pagar.mostrar()
pagar.pagar_cuota()
pagar.determinar()
pagar.actualizar_estado()