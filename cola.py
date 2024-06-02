from listaDoble import ListaDoble

class Cola(ListaDoble):
    def __init__(self):
        super().__init__()
    
    def encolar(self,valor):
        super().agregar_final(valor)
        
    def desencolar(self):
        super().eliminar_inicio()
        
    def consultar(self):
        if self.cabeza is not None:
            return self.cabeza.valor
        return None
    
    def esta_vacia(self):
        return self.cabeza is None
    
    def size(self):
        return self.tamanio