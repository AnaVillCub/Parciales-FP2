class Coche:
    
    def __init__(self, marca: str, modelo: str, precio: float):
        self.__marca = marca
        self.__modelo = modelo
        if not isinstance(precio, (int, float)) or precio <= 0:
            raise ValueError("Precio incorrecto")
        self.__precio = precio
        self.__estado = "Disponible"
        
    @property
    def marca(self):
        return self.__marca
    @property
    def modelo(self):
        return self.__modelo
    @property
    def precio(self):
        return self.__precio
    @precio.setter
    def precio(self, valor):
        if not isinstance(valor, (int, float)) or valor <= 0:
            raise ValueError("Precio incorrecto")
        self.__precio = valor
    @property
    def estado(self):
        return self.__estado

    @estado.setter
    def estado(self, nuevo_estado):
        if nuevo_estado not in ("Disponible", "Reservado", "Vendido"):
            raise ValueError("Estado inválido. Debe ser 'Disponible', 'Reservado' o 'Vendido'")
        self.__estado = nuevo_estado

    def reservar(self):
        if self.__estado == "Disponible":
            self.__estado = "Reservado"
        else:
            raise ValueError("Solo reservar si coche disponible")

    def vender(self):
        if self.__estado in ("Disponible", "Reservado"):
            self.__estado = "Vendido"
        else:
            raise ValueError("Solo vender coche disponible o reservado")

    def liberar(self):
        if self.__estado == "Reservado":
            self.__estado = "Disponible"
        else:
            raise ValueError("Solo liberar coche reservado")
    
    def __str__(self):
        return f"{self.__marca}: {self.__modelo} - {self.__precio} $ - {self.__estado}"

if __name__ == "__main__":
    # Crear coche
    c = Coche("Toyota", "Yaris", 15000)
    print(c)  # Toyota Yaris - 15000 € - Disponible

    # Reservar el coche
    c.reservar()
    print(c)  # Toyota Yaris - 15000 € - Reservado

    # Liberar la reserva
    c.liberar()
    print(c)  # Toyota Yaris - 15000 € - Disponible

    # Vender directamente
    c.vender()
    print(c)  # Toyota Yaris - 15000 € - Vendido

    # Intentar reservar un coche vendido (debe fallar)
    try:
        c.reservar()
    except ValueError as e:
        print("Error:", e)

    # Intentar cambiar estado a algo inválido
    try:
        c.estado = "En reparación"
    except ValueError as e:
        print("Error:", e)

    # Cambiar el precio
    c.precio = 15500
    print(f"Nuevo precio: {c.precio} €")
