from nodo import Nodo

class ListaSimpleCircular:
    def __init__(self):
        self.cabeza = None
        self.tamanio = 0

    def agregar(self, valor):
        nuevo = Nodo(valor)
        if self.cabeza is None:
            self.cabeza = nuevo
            nuevo.siguiente = self.cabeza
        else:
            actual = self.cabeza
            while actual.siguiente != self.cabeza:
                actual = actual.siguiente
            actual.siguiente = nuevo
            nuevo.siguiente = self.cabeza
        self.tamanio += 1

    def recorrer(self):
        if self.cabeza is None:
            print("La lista está vacía")
            return

        actual = self.cabeza
        while True:
            print(actual.valor, end=" -> ")
            actual = actual.siguiente
            if actual == self.cabeza:
                print()
                return

    def buscar(self, valor):
        if self.cabeza is None:
            return False

        actual = self.cabeza
        while True:
            if actual.valor == valor:
                return True
            actual = actual.siguiente
            if actual == self.cabeza:
                return False
            

    def tamanio_lista(self):
        return self.tamanio
    
    def buscar(self, valor):
        if self.cabeza is None:
            return False
        
        actual = self.cabeza
        while True:  # Se utiliza un bucle infinito aquí porque la lista es circular
            if actual.valor == valor:
                return True
            actual = actual.siguiente
            if actual == self.cabeza or actual !=self.cabeza:  # Has dado la vuelta completa a la lista
                return False
                    
    def eliminar(self, valor):
        
        if self.cabeza is None: #la lista esta vacía
            return False
        actual=self.cabeza
        anterior=None
        #si la lista tiene un solo nodo
        if self.cabeza.valor == valor and self.cabeza.siguiente==self.cabeza:   #hacemos dos comparaciones
            self.cabeza= None
            self.tamanio=0
            return True     
        #buscar el nodo a eliminar y mantener el nodo anterior
        while True:
            if  actual.valor == valor:
                break
            anterior=actual
            actual=actual.siguiente
            if actual== self.cabeza:
                return False #Valor no encontrado
            
        #Si el nodo a eliminar es la cabeza
        if actual== self.cabeza:
            #encontrar al ultimo nodo para actualizar su referencia 'siguiente'
            while actual.siguiente != self.cabeza:
                actual=actual.siguiente
            actual.siguiente = self.cabeza.siguiente
            self.cabeza= self.cabeza.siguiente
            
        #Eliminar al nodo que no es la cabeza
        else:
            anterior.siguiente= actual.siguiente
        self.tamanio=-1
        return True
    
    def eliminar_final(self):
        if self.cabeza is None: #la lista esta vacía
            return False
        #cuando solo hay un nodo
        if self.cabeza.siguiente == self.cabeza:
            self.cabeza= None
            self.tamanio=0
            return True
        #Iniciar con el primer nodo
        actual=self.cabeza
        #recorre hasta encontrar el nodo que esta a la cabeza
        while actual.siguiente.siguiente != self.cabeza:
            actual= actual.siguiente#el nodo actual ahora es el penultimo
        actual.siguiente= self.cabeza #hacemos que apunte a la cabeza(ultimo)
        self.tamanio-=1
        return True
        
    def eliminar_inicio(self):
        if self.cabeza== None: #si la lista esta vacia
            return False
        #si solo hay un nodo
        if self.cabeza.siguiente== self.cabeza:
            self.cabeza = None
            self.tamanio-=1
            return True
        else:
            #encontrar el ultimo nodo para actualizarlo a su referencia 'siguiente'
            actual=self.cabeza
            
            while actual.siguiente != self.cabeza:
                actual= actual.siguiente
            
            actual.siguiente = self.cabeza.siguiente
            self.cabeza = self.cabeza.siguiente
        self.tamanio -=1
        return True
        