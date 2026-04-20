from containerbase import ContainerBase 

class Task:

    def __init__(self, name, duration):
        self.name = name
        self.duration = duration

    def __str__(self):
        return f"{self.name}: {self.duration} min"


class TaskList(ContainerBase):

    class Node:
        def __init__(self, value, next=None):
            self.value = value
            self.next = next

    def __init__(self):
        self.first = None
        self.last = None
        self._size = 0
        self._time_spent = 0
        
    def add_task(self, task):
        new_node = self.Node(task)
        if self.first is None:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node # type: ignore
            self.last = new_node
        self._size += 1
    
    def get_task(self, position):
        if position < 0 or position >= self._size: # Verificamos los límites
            return None
        current = self.first
        for _ in range(position):
            if current is None: # Si la lista está mal construida
                return None
            current = current.next
        return current.value if current else None # Asegura que current no sea None
    
    def task_completed(self, position):
        if position < 0 or position >= self._size:
            return None
        
        if position == 0:
            if self.first is None: # Si la lista està vacía
                return None
            completed_task = self.first.value
            self._time_spent += completed_task.duration
            self.first = self.first.next
            if self.first is None:
                self.last = None
        else:
            current = self.first
            for _ in range(position - 1):
                if current is None or current.next is None: #  Si la posición no existe
                    return None
                current = current.next
                if current.next is None:  # Si el siguiente nodo no existe
                    return None
            completed_task = current.next.value # type: ignore
            self._time_spent += completed_task.duration
            current.next = current.next.next # type: ignore
            if current.next is None: # type: ignore
                self.last = current
        
        self._size -= 1
        return completed_task
    
    @property
    def time_left(self):
        total = 0
        current = self.first
        while current is not None:
            total += current.value.duration
            current = current.next
        return total
    
    @property
    def time_spent(self):
        return self._time_spent

