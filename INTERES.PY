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

class InterestGroup(ContainerBase):
    class Node:
        def __init__(self, value, next=None):
            self.value=value
            self.next=next
        
    def __init__(self):
        self.first=None
        
    def isMember(self, miembro):
        # Para no modificar la lista, debemos de crear una variable auxiliar
        actual = self.first
        while actual:
            if actual.value == miembro:
                return True
            # Avanzamos
            actual = actual.next
        return False
    
    def add_member(self, miembro):
        # Si el miembro ya existe, devolvemos false. Utilizamos la funcion isMember
        if self.isMember(miembro):
            return False
        nuevo_miembro_nodo = self.Node(miembro, self.first)
        self.first = nuevo_miembro_nodo
        return True
    
    @property
    def size(self):
        # Contador de la lista
        tamaño=0
        actual= self.first
        # Mientras en la lista haya valores, contamos y vamos al siguiente
        while actual:
            tamaño+=1
            actual = actual.next
        # Devolvemos el contador
        return tamaño
    
    def union(self, otro_grupo):
        # Creamos una lista nueva, y un valor actual para no modificar la lista original 
        nueva_union = InterestGroup()
        actual = self.first
        while actual is not None:
            # Añadimos el valor actual a la nueva lista 
            nueva_union.add_member(actual.value)
            actual = actual.next
        # Para la lista pasada por parámetro haremos lo mismo
        actual = otro_grupo.first 
        while actual is not None:
            # if not nueva_union.isMember(actual.value): -> cosa mia, no va
                nueva_union.add_member(actual.value) 
                actual = actual.next
        return nueva_union
    
    def remove_member(self, miembro):
        if self.first is None: return False
        
        # Si el primero es el que hay que borrar
        if self.first == miembro:
            self.first = self.first.next
            return True
        
        actual = self.first
        while actual.next is not None:
            if actual.next == miembro:
                actual.next = actual.next.next
                return True
            actual = actual.next
        return False
        """
        # Buscar el nodo a eliminar
        prev = self.first
        current = self.first.next
        while current is not None:
            if current.value == name:
                prev.next = current.next
                return True
            prev = current
            current = current.next
        return False
        """