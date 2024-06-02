class PilaEstatica:
    def __init__(self, capacidad=5):
        self.capacidad = capacidad
        self.arreglo = [None] * capacidad  # Almacenamiento estático
        self.tope = -1  # Índice del último elemento

    def esta_vacia(self):
        return self.tope == -1

    def esta_llena(self):
        return self.tope == self.capacidad - 1

    def apilar(self, item):
        if not self.esta_llena():
            self.tope += 1
            self.arreglo[self.tope] = item
        else:
            print("Pila está llena, no se puede añadir el elemento ingresado.")
            

    def desapilar(self):
        if not self.esta_vacia():
            item = self.arreglo[self.tope]
            self.arreglo[self.tope] = None  # Limpiar la referencia, opcional
            self.tope -= 1
            return item
        else:
            print("Pila está vacía")

    def consultar(self):
        if not self.esta_vacia():
            return self.arreglo[self.tope]
        
    def tamanio(self):
        return self.tope + 1
