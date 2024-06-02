from colaDoble import ColaDoble
#Cola con entrada restringida
class ColaER(ColaDoble):
    def __init__(self):
        super().__init__()
        
    def encolar_inicio(self, valor):
        return super().encolar_inicio(valor)
    
    def consultar(self):
        if self.cabeza is not None:
            return self.cabeza.valor
        return None
    
    def consultar_final(self):
        if self.cabeza is not None:
            return self.cola.valor
        return None    

    def desencolar_final(self):
        return super().desencolar_final()
    
    def desencolar_inicio(self):
        return super().desencolar_inicio()
    
    def recorrer_inicio(self):
        return super().recorrer_inicio()
    
    def recorrer_fin(self):
        return super().recorrer_fin()
    
    def size(self):
        return self.tamanio
        
    def esta_vacia(self):
       return self.cabeza is None
