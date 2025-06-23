from containerbase import ContainerBase


class Client:

    def __init__(self, name, total_cost):
        self.name = name
        self.total_cost = total_cost

    def __str__(self):
        return f"{self.name}: {self.total_cost}"


class CheckoutQueue(ContainerBase):
    class Node:
        def __init__(self, value, next=None):
            self.value = value  # El valor en el nodo.
            self.next = next    # El enlace al siguiente nodo.

    def __init__(self):
        self.first = None   # El enlace al primer nodo de la lista.
        self.last = None   # El enlace al último nodo de la lista.
        self.caja = 0       # Donde guardamos el coste total
        self._size = 0

        
    def enqueue(self, value):
        nuevo_nodo = self.Node(value)
        if self.first is None:
            self.first = nuevo_nodo
            self.last = nuevo_nodo
        else:
            self.last.next = nuevo_nodo # type: ignore
            self.last = nuevo_nodo
        self._size += 1
    
    def dequeue(self):
        if self.first is None:
            return None # No hay clientes
        
        actual = self.first
        self.first = self.first.next
        # ¿No sera actual? No
        if self.first is None:
            self.last = None # La cola se vacío
    
        self.caja += actual.value.total_cost # Suma coste cliente
        self._size -= 1
        return actual.value # Devolver cliente

    @property
    def daily_sales(self):
        return self.caja

    def split(self):
        nueva_cola = CheckoutQueue()
        contador = 0

        actual = self.first # Primer elemento
        anterior = None     # Elemento antes del primero, vacío

        while actual:
            if contador % 2 == 1: # Impares
                nueva_cola.enqueue(actual.value)
                
                # Borra el nodo actual de la cola original
                if anterior:
                    anterior.next = actual.next
                #else:
                    #self.first = actual.next
                # Si actual es ultimo, actualizamos
                #if actual == self.last:
                #    self.last = anterior
                
                self._size -= 1
                actual = actual.next  # Avanzamos a siguiente nodo
            else:
                anterior = actual
                actual = actual.next
            contador += 1
        self.last = anterior 
        return nueva_cola
