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
    def __init__(self, name, duration):
        self.name = name
        self.duration = duration
        
    def __str__(self):
        return  f"{self.name}: {self.duration} min"

class TaskList(ContainerBase):
    class Node:
        def __init__(self, value, next=None):
            self.value = value # Un valor de la clase Node (name, cost)
            self.next = next # Es el siguiente Nodo
    
    def __init__(self):
        self.first=None
        self.last=None
        self._time_spent = 0
        self.size = 0 # Para verificar la longitud de la lista
    
    def add_task(self, tarea):
        nueva_tarea = self.Node(tarea)
        if self.first is None:
            # Si el primero está vacío, tanto el primero como el ultimo serán la nueva tarea    
            self.first=nueva_tarea
            self.last=nueva_tarea
        else:
            # Si no, como se inserta por el final. El siguiente será la nueva tarea,
            # y el ultimo apuntara al siguiente, por eso el mismo valor
            self.last.next=nueva_tarea # type: ignore
            self.last= nueva_tarea
        self.size+=1
            
    def get_task(self, pos):
        index = 0
        if pos < 0 or pos >= self.size:
            return None
        actual = self.first
        while actual is not None:
            if index==pos:
                return actual.value
            actual = actual.next
            index += 1
        return None
    
    def task_completed(self, pos):
        """
        Elimina y devuelve la tarea en la posición dada.
        Añade su duración a time_spent.
        Devuelve None si la posición no existe.
        """
        if self.first is None:
            return None
        # Caso especial: eliminar el primer nodo
        if pos == 0:
            task = self.first.value
            self._time_spent += task.duration
            self.first = self.first.next
            if self.first is None:
                self.last = None
            return task
        # Buscar el nodo en la posición dada
        prev = None
        current = self.first
        index = 0
        while current is not None and index < pos:
            prev = current
            current = current.next
            index += 1     
        if current is None:
            return None   
        # Eliminar el nodo encontrado
        task = current.value
        self._time_spent += task.duration
        prev.next = current.next # type: ignore
        # Actualizar last si eliminamos el último nodo
        if current.next is None:
            self.last = prev 
        return task
        
    @property
    def time_spent(self):
        return self._time_spent
    
    @property
    def time_left(self):
        """Devuelve el tiempo total de todas las tareas pendientes."""
        total = 0
        current = self.first
        while current is not None:
            total += current.value.duration
            current = current.next
        return total