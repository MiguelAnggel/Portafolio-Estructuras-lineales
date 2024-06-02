from nodo import Nodo

class ListaSimple:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.tamanio = 0

    def agregar(self, valor):
        nuevo = Nodo(valor)

        # Verifica si la lista esta vacía
        if self.cola == None:
            self.cabeza = nuevo
            self.cola = nuevo
        else:
            self.cola.siguiente = nuevo
            self.cola = nuevo

        self.tamanio += 1

    def eliminar(self, valor):
        actual = self.cabeza
        anterior = None
        while actual:
            if actual.valor == valor:
                if anterior:  # No es el primer nodo
                    anterior.siguiente = actual.siguiente
                else:
                    self.cabeza = actual.siguiente
                self.tamanio -= 1
                return True  # Valor eliminado
            # Avanza al siguiente nodo
            anterior = actual  # El actual se vuelve el "anterior"
            actual = actual.siguiente  # El "nuevo actual" es el siguient
        return False  # Valor no encontrado

    def eliminar_final(self):
        if self.cola is None:
            return False

        actual = self.cabeza
        anterior = None
        while actual.siguiente:
            anterior = actual
            actual = actual.siguiente
        if anterior:
            anterior.siguiente = None
            self.cola = anterior
        else:
            self.cabeza = None
            self.cola = None
        self.tamanio -= 1
        return True

    def recorrer(self):
        actual = self.cabeza

        while actual:
            print(actual.valor, end=" -> " if actual.siguiente else "\n")
            actual = actual.siguiente

    def buscar(self, valor):
        actual = self.cabeza

        while actual:
            if actual.valor == valor:
                return True
            actual = actual.siguiente

        return False
