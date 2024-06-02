import heapq
from colaPA import ColaPA
#Cola con prioridad Descendente
class ColaPD(ColaPA):
    def __init__(self):
        self.heap = []

    def encolar(self, prioridad, elemento):
        # Invertir la prioridad con - para simular un heap de máximos.
        heapq.heappush(self.heap, (-prioridad, elemento))

    def desencolar(self):
        if self.esta_vacia():
            print("La cola está vacía")
            return None
        # Extraer el elemento y restablecer su prioridad a positivo si es necesario.
        prioridad, valor = heapq.heappop(self.heap)
        return valor

    def esta_vacia(self):
        return len(self.heap) == 0

    def consultar_max(self):
        if self.esta_vacia():
            print("La cola está vacía")
            return None
        else:
            return self.heap[0][1]
            
    def size(self):
        return len(self.heap)
