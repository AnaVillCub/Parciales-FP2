class ContainerBase:
    def __init__(self):
        self._size = 0

    def __str__(self):
        if not hasattr(self, 'first'):
            return "None"

        actual = self.first # type: ignore
        if actual is None:
            return "None"

        resultado = ""
        while actual:
            resultado += f"[{actual.value}]->"
            actual = actual.next
        return resultado + "None"

class Client:
    def __init__(self, name, total_cost):
        self.name = name
        self.total_cost = total_cost
        
    def __str__(self):
        return  f"{self.name}: {self.total_cost}"

class CheckOutQueue(ContainerBase):
    class Node:
        def __init__(self, value, next=None):
            self.value = value # Un valor de la clase Node (name, cost)
            self.next = next # Es el siguiente Nodo
    
    def __init__(self):
        self.first=None
        self.last=None
        self.caja=0
        
    def enqueue(self, cliente):
        # Creamos un cliente de tipo de Node dado que es una lista de nodos
        nuevo_cliente = self.Node(cliente)
        # Si el primer elemento está vacio
        if (self.first == None):
            self.first = nuevo_cliente
            self.last = nuevo_cliente
        else:
            self.first.next = nuevo_cliente
            self.last = nuevo_cliente
            
    def dequeue(self):
        if (self.first == None): return None # "No hay clientes"
        
        actual = self.first # Primero
        self.first = self.first.next # El primero pasará a ser el siguiente
        
        if self.first == None: # if el "primero" (que será tecnicamente el siguiente)
            self.last = None # Será None pq se vació la cola
        
        self.caja+=actual.value.total_Cost # value puede acceder al nombre y al coste
        return actual.value # Representa al cliente: Devolver cliente 
    @property
    def daily_sales(self):
        return self.caja

    def split(self):
        nueva_cola = CheckOutQueue()
        contador = 0 # Posicion
        
        actual = self.first
        anterior = None
        
        while actual:
            if (contador % 2 == 1): # Impares
                nueva_cola.enqueue(actual.value) # Valor del actual, es decir, del cliente con nombre y coste
                # si hay un valor anterior, este siguiente será el actual siguiente
                if anterior:
                    anterior.next = actual.next
                # Reducimos el valor de la lista
                actual = actual.next  # Avanzamos a siguiente nodo
            else:
                # si es par, el anterior será ese par, y el actual será el siguiente. Contamos++
                anterior = actual
                actual = actual.next
            contador+=1
        # Cuando acabe, el ultimo sea none, pues tendrá el valor del anterior
        self.last = anterior
        return nueva_cola   



