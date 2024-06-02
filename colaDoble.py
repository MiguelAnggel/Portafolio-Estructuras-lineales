from listaDoble import ListaDoble

class ColaDoble(ListaDoble):
    def __init__(self):
        super().__init__()

    def encolar_inicio(self, valor):
        super().agregar_inicio(valor)

    def encolar_final(self, valor):
        super().agregar_final(valor)

    def desencolar_inicio(self):
        if not self.esta_vacia():
            valor = self.cabeza.valor
            self.eliminar_inicio()
            return valor
        else:
            raise Exception("La cola está vacía")

    def desencolar_final(self):
        if not self.esta_vacia():
            valor = self.cola.valor
            self.eliminar_final()
            return valor
        else:
            raise Exception("La cola está vacía")

    def esta_vacia(self):
        return self.cabeza is None
    
    def recorrer_fin(self):
        return super().recorrer_fin()
    
    def recorrer_inicio(self):
        return super().recorrer_inicio()
    
    def size(self):
        return self.tamanio

