from listaDoble import ListaDoble
from nodoDoble import NodoDoble


class ListaDobleCircular(ListaDoble):
    def __init__(self):
        super().__init__()

    def agregar_final(self, valor):
        super().agregar_final(valor)
        self.cola.siguiente = self.cabeza
        self.cabeza.anterior = self.cola

    def agregar_inicio(self, valor):
        super().agregar_inicio(valor)
        self.cabeza.anterior = self.cola
        self.cola.siguiente = self.cabeza

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


    def agregar(self, valor, posicion):
        if posicion < 0 or posicion > self.tamanio:
            return False

        if posicion == 0:
            self.agregar_inicio(valor)
        elif posicion == self.tamanio:
            self.agregar_final(valor)
        else:
            nuevo = NodoDoble(valor)
            actual = self.cabeza
            for _ in range(posicion):
                actual = actual.siguiente
            nuevo.anterior = actual.anterior
            nuevo.siguiente = actual
            actual.anterior.siguiente = nuevo
            actual.anterior = nuevo
            self.tamanio += 1
            return True

    def recorrer_inicio(self):
        actual = self.cabeza
        while actual:
            print(actual.valor, end=' -> ' if actual.siguiente else '\n')
            actual = actual.siguiente
            if actual == self.cabeza:
                print()
                break

    def recorrer_fin(self):
        actual = self.cola
        while actual:
            print(actual.valor, end=' -> ' if actual.anterior else '\n')
            actual = actual.anterior
            if actual == self.cola:
                print()
                break

    def recorrer(self, pasos=1):
        actual = self.cabeza
        for _ in range(pasos):
            print(actual.valor, end=" -> ")
            actual = actual.siguiente

    def eliminar_inicio(self):
        if self.cabeza is None:
            return False

        if self.cabeza.siguiente == self.cabeza:
            self.cabeza = None
            self.cola = None
        else:
            self.cabeza = self.cabeza.siguiente
            self.cabeza.anterior = self.cola
            self.cola.siguiente = self.cabeza

        self.tamanio -= 1
        return True

    def eliminar_final(self):
        if self.cola is None:
            return False

        if self.cola.anterior == self.cola:
            self.cabeza = None
            self.cola = None
        else:
            self.cola = self.cola.anterior  # Apuntamos al penúltimo
            self.cola.siguiente = self.cabeza  # Penúltimo a cabeza
            self.cabeza.anterior = self.cola  # Cabeza a penúltimo

        self.tamanio -= 1
        return True
    
    def eliminar_por_valor(self, valor):
        # Comenzamos con el primer nodo.
        actual = self.cabeza
    # Inicializamos anterior como None ya que empezamos con la cabeza de la lista.
        anterior = None

    # Mientras no lleguemos al final de la lista circular
        while actual:
        # Si encontramos el nodo con el valor deseado, procedemos a eliminarlo.
            if actual.valor == valor:
            # Si es el único nodo en la lista
                if actual.siguiente == actual:
                    self.cabeza = None
                    self.cola = None
            # Si es la cabeza de la lista
                elif actual == self.cabeza:
                    self.cabeza = actual.siguiente
                    self.cabeza.anterior = self.cola
                    self.cola.siguiente = self.cabeza
            # Si es la cola de la lista
                elif actual == self.cola:
                    self.cola = anterior
                    self.cola.siguiente = self.cabeza
                    self.cabeza.anterior = self.cola
            # Si está en el medio
                else:
                    anterior.siguiente = actual.siguiente
                    actual.siguiente.anterior = anterior
            # Decrementamos el tamaño de la lista
                self.tamanio -= 1
                return True  # Indicamos que el elemento ha sido eliminado
        # Si no hemos encontrado el valor, seguimos buscando
            anterior = actual
            actual = actual.siguiente
        # Si hemos dado la vuelta completa a la lista, paramos
            if actual == self.cabeza:
                break

        return False  # El valor no fue encontrado y por lo tanto no se eliminó nada

    
    #def eliminar(self, posicion):
     #   if posicion < 0 or posicion >= self.tamanio:
      #      return False

       # if posicion == 0:
        #    return self.eliminar_inicio()
        #elif posicion == self.tamanio - 1:
         #   return self.eliminar_final()
        #else:
         #   actual = self.cabeza
          #  for _ in range(posicion):
            #    actual = actual.siguiente
           # actual.anterior.siguiente = actual.siguiente
            #actual.siguiente.anterior = actual.anterior
            #self.tamanio -= 1
        #return True
