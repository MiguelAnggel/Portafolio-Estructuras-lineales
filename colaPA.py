import heapq
#Cola con prioridad Ascendente
class ColaPA:
    def __init__(self):
        self.heap = []

    def encolar(self, elemento, prioridad):
        heapq.heappush(self.heap, (prioridad, elemento))

    def menos_p(self):
        if not self.esta_vacia():
            return heapq.heappop(self.heap)[1]
        else: 
            print("La cola está vacía")
            return None

    def consultar_min(self):
        if not self.esta_vacia():
            return self.heap[0][1]
        else:
            print("La cola está vacía")

    def esta_vacia(self):
        return not self.heap
    
    def recorrer(self):
        return [elemento for prioridad, elemento in sorted(self.heap)]

    def size(self):
        return len(self.heap)