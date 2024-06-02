from listaDoble import ListaDoble
from nodoDoble import NodoDoble
class ListaCircular(ListaDoble):
    def __init__(self):
        super().__init__()
        
    def recorrer_adelante(self):
        if self.cabeza is None:
            print("La lista está vacía.")
        else:
            actual = self.cabeza
            while True:
                print(actual.valor, end=" -> ")
                actual = actual.siguiente
                if actual == self.cabeza:
                    print("Vuelta completa a la lista.")
                    break

            
    def recorrer_atras(self):
        if self.cabeza is None:
            print("La lista está vacía.")
        else:
            actual = self.cabeza.anterior
            while True:
                print(actual.valor, end=" <- ")
                actual = actual.anterior
                if actual == self.cabeza.anterior:
                    print("Vuelta completa a la lista.")
                    break


            
    def agregar_final(self, valor):
        nuevo = NodoDoble(valor)
        if self.cabeza is None:
        # Estableciendo el primer nodo, debe apuntar a sí mismo en ambos.
            nuevo.siguiente = nuevo
            nuevo.anterior = nuevo
            self.cabeza = nuevo
            self.cola = nuevo
        else:
        # Enlazando el nuevo nodo al final de la lista circular.
            nuevo.anterior = self.cola
            nuevo.siguiente = self.cabeza
            self.cola.siguiente = nuevo
            self.cabeza.anterior = nuevo
            self.cola = nuevo
        self.tamanio += 1
        return True

    def agregar_inicio(self, valor):
        nuevo = NodoDoble(valor)
        if self.cabeza is None:
        # Estableciendo el primer nodo, debe apuntar a sí mismo en ambos.
            nuevo.siguiente = nuevo
            nuevo.anterior = nuevo
            self.cabeza = nuevo
            self.cola = nuevo
        else:
        # Enlazando el nuevo nodo al inicio de la lista circular.
            nuevo.siguiente = self.cabeza
            nuevo.anterior = self.cola
            self.cabeza.anterior = nuevo
            self.cola.siguiente = nuevo
            self.cabeza = nuevo
        self.tamanio += 1
        return True

        
        
    def eliminar_inicio(self):
        if self.cabeza is None:  # Lista vacía
            return None
        if self.cabeza == self.cola:  # Lista con un solo elemento
            self.cabeza = None
            self.cola = None
        else:
            self.cabeza = self.cabeza.siguiente
            self.cabeza.anterior = self.cola
            self.cola.siguiente = self.cabeza
        self.tamanio -= 1
        return True
    
    def eliminar_final(self):
        if self.cabeza is None:  # Lista vacía
            return None
        if self.cabeza == self.cola:  # Lista con un solo elemento
            self.cabeza = None
            self.cola = None
        else:
            self.cola = self.cola.anterior
            self.cola.siguiente = self.cabeza
            self.cabeza.anterior = self.cola
        self.tamanio -= 1
        return True
    
    def agregar(self, valor, posicion):
        if posicion < 0 or posicion > self.tamanio:
            return False
        if posicion==0:
            self.agregar_inicio(valor)
        elif posicion == self.tamanio:
            self.agregar_final(valor)
        else:
            nuevo=NodoDoble(valor)
            actual = self.cabeza
            for _ in range (posicion):
                actual= self.siguiente
            nuevo.anterior = actual.anterior
            nuevo.siguiente = actual
            actual.anterior.siguiente = nuevo
            actual.anterior = nuevo
            self.tamanio+=1
            return True
    
    def buscar(self, valor):
        if self.cabeza is None:
            return False
        
        actual = self.cabeza
        while True:  # Se utiliza un bucle infinito aquí porque la lista es circular
            if actual.valor == valor:
                return True
            actual = actual.siguiente
            if actual == self.cabeza:# Has dado la vuelta completa a la lista
                return False
    
                
    def eliminar(self, posicion):
        if posicion < 0 or posicion >= self.tamanio:
            return False
        if posicion == 0:
            return self.eliminar_inicio()
        elif posicion== self.tamanio-1:
            return self.eliminar_final()
        else: 
            actual = self.cabeza
            for _ in range (posicion):
                actual = actual.siguiente
            actual.anterior.siguiente = actual.siguiente
            actual.siguiente.anterior = actual.anterior
            self.tamanio-=1
        return True