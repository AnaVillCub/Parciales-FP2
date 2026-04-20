from containerbase import ContainerBase 

class InterestGroup(ContainerBase):

    class Node:
        def __init__(self, value, next=None):
            self.value = value
            self.next = next

    def __init__(self):
        self.first = None
        
    def is_member(self, name):
        current = self.first
        while current is not None:
            if current.value == name:
                return True
            current = current.next
        return False
    
    def add_member(self, name):
        if self.is_member(name):
            return False
        new_node = self.Node(name, self.first)
        self.first = new_node
        # self._size += 1
        return True
    
    @property
    def size(self):
        tamaño = 0
        actual = self.first
        while actual:
            tamaño += 1
            actual = actual.next
        return tamaño
    
    def union(self, other_group):
        new_group = InterestGroup()
        current = self.first
        while current is not None:
            new_group.add_member(current.value)
            current = current.next
        current = other_group.first
        while current is not None:
            new_group.add_member(current.value)
            current = current.next
        return new_group
    
    def remove_member(self, name):
        if self.first is None:
            return False
        
        if self.first.value == name:
            self.first = self.first.next
            # self._size -= 1
            return True
        
        current = self.first
        while current.next is not None:
            if current.next.value == name:
                current.next = current.next.next
                # self._size -= 1
                return True
            current = current.next
        return False
    