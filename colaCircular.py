from listaDoble import ListaDoble

class ColaCircular(ListaDoble):
    def __init__(self):
        super().__init__()
        
    def encolar(self,valor):
        super().agregar_final(valor)
        
    def desencolar(self):
        super().eliminar_inicio()
        
    def recorrer(self):
        super().recorrer_inicio()

    def consultar(self):
        if not self.esta_vacia():
            return self.cola.valor
    
    def esta_vacia(self):
        return self.cabeza is None
    
    def recorrer_final(self):
        super().recorrer_fin()
    
    def size(self):
        return self.tamanio
        
