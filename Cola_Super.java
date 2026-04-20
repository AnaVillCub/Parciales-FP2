public class Client{
    public final String name;
    public final int totalCost;
    public Client(String name, int total){
        this.name = name;
        this.totalCost=total;
    }
}

public class ContainerBase{
    protected Node first;
    protected Node last;
    public String toString(){
        return "";
    }
}

public class Node{
    public Client value;
    public Node next;
    public Node(Client value){
        this.value = value;
    }
}

public class Cola_Super {
    private int daily_sales;
    // Constructor: inicializamos el atributo para añadir luego el metodo
    public Cola_Super(){
        this.daily_sales=0;
    }

    public void enqueue(String cliente){
        // Se supone que la lista está vacía, creamos el nodo con el valor del cliente
        Node new_node = new Node(cliente);
        if (first == null){
            first = new_node;
            last = new_node;
        } else { // Si hay un algo, se añade al finals
            last.next = new_node;
            last = new_node;
        }
    }
    // Metodo de Tipo Client ya que queremos sacar los clientes
    public Client dequeue(){
        if (first == null) return false; // No hay clientes

        Client cliente = first.value;
        daily_sales+= cliente.totalCost;
        first = first.next // El primero -> siguiente

        // Si la lista se vacío, el ultimo quedara vacio
        if (first==null){last=null;}

        return cliente;
    }

    public int getDaily_Sales(){
        return daily_sales;
    }

    public Cola_Super split(){
        Cola_Super nueva = new Cola_Super();
        Node actual = first;
        Node previo = null;
        int contador = 0;

        while (actual != null){
            if (contador % 2 == 1){ // Impares
                nueva.enqueue(actual.value);
                // Si el anterior tiene algún valor, el siguiente será actual siguiente
                if (previo != null){
                    previo.next = actual.next;
                }
                if (actual == last){
                    last = previo;
                }
            } else {
                previo = actual;
            }
            actual = actual.next;
            contador++;
        }

        return nueva;
    }

}
