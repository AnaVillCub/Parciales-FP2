package A.GRUPO_1_EXAMEN_3;

public class InterestGroup extends ContainerBase {
    
    // Método para verificar si un miembro está en el grupo
    public boolean isMember(String name) {
        Node current = first;
        while (current != null) {
            if (current.value.equals(name)) {
                return true;
            }
            current = current.next;
        }
        return false;
    }
    
    // Método para añadir un nuevo miembro (sin duplicados)
    public boolean addMember(String name) {
        if (isMember(name)) {
            return false;
        }
        
        Node newNode = new Node(name);
        newNode.next = first;
        first = newNode;
        return true;
    }
    
    // Método para obtener el número de miembros
    public int getSize() {
        int count = 0;
        Node current = first;
        while (current != null) {
            count++;
            current = current.next;
        }
        return count;
    }
    
    // Método para crear la unión de dos grupos
    public InterestGroup union(InterestGroup other) {
        InterestGroup result = new InterestGroup();
        
        // Añadir miembros del grupo actual
        Node current = this.first;
        while (current != null) {
            result.addMember(current.value);
            current = current.next;
        }
        
        // Añadir miembros del otro grupo
        current = other.first;
        while (current != null) {
            result.addMember(current.value);
            current = current.next;
        }
        
        return result;
    }
    
    // Método para eliminar un miembro
    public boolean removeMember(String name) {
        if (first == null) {
            return false;
        }
        
        // Caso especial: el primer nodo
        if (first.value.equals(name)) {
            first = first.next;
            return true;
        }
        
        Node prev = first;
        Node current = first.next;
        
        while (current != null) {
            if (current.value.equals(name)) {
                prev.next = current.next;
                return true;
            }
            prev = current;
            current = current.next;
        }
        
        return false;
    }
    
    // Sobrescribir toString para mostrar la lista correctamente
    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        Node current = first;
        while (current != null) {
            sb.append("[").append(current.value).append("]->");
            current = current.next;
        }
        sb.append("null");
        return sb.toString();
    }
}