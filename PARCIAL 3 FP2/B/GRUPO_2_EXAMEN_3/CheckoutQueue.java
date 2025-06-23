package B.GRUPO_2_EXAMEN_3;

public class CheckoutQueue extends ContainerBase {
    private int dailySales;

    public CheckoutQueue() {
        this.dailySales = 0;
    }

    // Método para añadir un cliente al final de la cola
    public void enqueue(Client client) {
        Node newNode = new Node(client);
        if (first == null) {
            first = newNode;
            last = newNode;
        } else {
            last.next = newNode;
            last = newNode;
        }
    }

    // Método para atender al primer cliente de la cola
    public Client dequeue() {
        if (first == null) {
            return null;
        }
        
        Client client = first.value;
        dailySales += client.totalCost;
        first = first.next;
        
        if (first == null) {
            last = null;
        }
        
        return client;
    }

    // Método para obtener el total de ventas diarias
    public int getDailySales() {
        return dailySales;
    }

    // Método para dividir la cola en dos
    public CheckoutQueue split() {
        CheckoutQueue newQueue = new CheckoutQueue();
        Node current = first;
        Node prev = null;
        int index = 0;

        while (current != null) {
            if (index % 2 == 1) { // Posiciones impares
                // Añadir a la nueva cola
                newQueue.enqueue(current.value);
                
                // Eliminar de la cola original
                if (prev != null) {
                    prev.next = current.next;
                }
                
                // Actualizar last si es necesario
                if (current == last) {
                    last = prev;
                }
            } else {
                prev = current;
            }
            
            current = current.next;
            index++;
        }

        return newQueue;
    }

}