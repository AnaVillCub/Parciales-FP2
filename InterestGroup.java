public class ContainerBase{
    protected Node first;
    public String toString(){
        return "";
    }
}

public class Node{
    public String value;
    public Node next;
    public Node(String value){
        this.value = value;
    }
}

public class InterestGroup extends ContainerBase{
    
    public boolean isMember(String miembro){
        // if (first == null) return false;
        // first es el heredado
        Node actual = first;
        while (first != null){
            if (actual.value.equals(miembro)){
                return true;
            }
            // Avanzamos
            actual = actual.next;
        }
        return false;
    }

    public boolean addMember(String miembro){
        if (isMember(miembro)) return false;
        // Añadimos al principio pq es la referencia que tenemos
        Node nuevo_miembro = new Node(miembro);
        // Nuevo nodo con el valor miembro
        nuevo_miembro.next = nuevo_miembro;
        // El primero pasará a ser el nuevo miembro
        first = nuevo_miembro;
        return true;
    }

    public int getSize(){
        int tamaño = 0;
        Node actual = first;

        while (actual != null){
            tamaño++;
            actual = actual.next;
        }
        return tamaño;
    }

    public InterestGroup union(InterestGroup otro_grupo){
        InterestGroup union = new InterestGroup();

        Node actual = first;
        while (actual != null){
            union.addMember(actual.value);
            actual = actual.next;
        }

        Node actual_otro = otro_grupo.first;
        while (actual_otro != null){
            union.addMember(actual_otro.value);
            actual = actual.next;
        }
        return union;
    }

    public boolean removeMember(String miembro){
        if (first == null) return false;

        if (first.value.equals(miembro)){
            first = first.next;
            return true;
        }
        Node previo = first;
        Node actual = first.next;

        while (actual != null){
            if (actual.value.equals(miembro)){
                // previo.next = actual, pero como ese es
                // el que eliminamos, tenemos que apuntar al siguiente
                previo.next = actual.next;
                return true;
            }
            // Si no se cumple; el previo será el siguiente, y el actual igual
            previo = actual;
            actual = actual.next;
        }
        return false;
    }
}