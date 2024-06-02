from listaSimple import ListaSimple

class Pila(ListaSimple):
    def __init__(self):
        super().__init__()

    def apilar(self, valor):
        self.agregar(valor)

    def desapilar(self):
        self.eliminar_final()

    def consultar(self):
        if self.cola is not None:
            return self.cola.valor

        return None

    def esta_vacia(self):
        return self.cabeza is None

    def size(self):
        return self.tamanio
