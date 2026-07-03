#f) Crear el archivo cuota.py con la clase Cuota:
#Atributos:

#● __estado (pagada, pendiente, vencida)
#● fecha_de_vencimiento
#● periodo (mes/año)

#Métodos:

#● getters y setters


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
    
pagar=Cuota("pendiente","1 de agosto del 2026","cada 20 dias")
pagar.mostrar()
pagar.set_estado("pagado")
pagar.mostrar()
pagar.pagar_cuota()