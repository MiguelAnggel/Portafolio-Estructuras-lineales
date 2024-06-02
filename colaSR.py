from colaDoble import ColaDoble

#Cola con salida restringida
class ColaSR(ColaDoble):
    def __init__(self):
        super().__init__()
        
    def encolar_final(self, valor):
        return super().encolar_final(valor)
    
    def encolar_inicio(self, valor):
        return super().encolar_inicio(valor)
    
    def desencolar_inicio(self):
        pass
    
    def desencolar_final(self):
        return super().desencolar_final()
    
    def size(self):
        return super().size()
    
    def recorrer_inicio(self):
        return super().recorrer_inicio()
    
    def recorrer_fin(self):
        return super().recorrer_fin()
    
    def esta_vacia(self):
        return super().esta_vacia()
    
    def consultar_frente(self):
        if self.cabeza is not None:
            return self.cabeza.valor
        return None
    
    def consultar_final(self):
        if self.cabeza is not None:
            return self.cola.valor
        return None 