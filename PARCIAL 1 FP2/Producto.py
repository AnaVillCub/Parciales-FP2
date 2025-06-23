class Producto:
    
    __total_productos = 0
    __productos_categ: dict[str, int] = {} # categoria: stock
    
    def __init__(self, nombre, categoria, precio, stock):
        self.__nombre = nombre
        self.__categoria = categoria
        
        if precio <= 0:
            raise ValueError("Precio negativo")
        self.__precio = precio
        if stock < 0:
            raise ValueError("Stock negativo")
        self.__stock = stock
        
        #Contador de __total_productos
        Producto.__total_productos += 1
        if categoria in Producto.__productos_categ:
            Producto.__productos_categ[categoria] += 1
        else:
            Producto.__productos_categ[categoria] = 1
        
    #////////    
    @property
    def nombre(self):
        return self.__nombre
    #//////// 
    @property
    def categoria(self):
        return self.__categoria
    #//////// 
    @property
    def precio(self):
        return self.__precio
    @precio.setter
    def precio(self, valor):
        if valor <= 0:
            raise ValueError("Precio negativo")
        self.__precio = valor
    #////////
    @property
    def stock(self):
        return self.__stock
    @stock.setter
    def stock(self, valor):
        if valor < 0:
            raise ValueError("Stock negativo")
        self.__stock = valor
        
    def vender(self, cantidad: int):
        if cantidad < 0 or not isinstance(cantidad, int):
            raise ValueError("Cantidad negativa")
        if cantidad > self.__stock:
            raise ValueError("Stock insuficiente")
        self.__stock -= cantidad
    
    def reponer(self, cantidad: int):
        if cantidad < 0 or not isinstance(cantidad, int):
            raise ValueError("Cantidad a reponer negativa")
        #if cantidad > self.__stock:
        #    raise ValueError("Stock supera el espacio")
        self.__stock += cantidad
    
    @classmethod
    def total_productos(cls):
        return cls.__total_productos
    @classmethod
    def productos_por_categoria(cls, categoria):
        return cls.__productos_categ.get(categoria, 0)
        
        
    def __str__(self):
        return f"{self.__nombre} - {self.__categoria} - {self.__precio} - {self.__stock} uds"


if __name__ == "__main__":
    # Crear productos
    p1 = Producto("Teclado", "Electrónica", 25.99, 10)
    p2 = Producto("Ratón", "Electrónica", 15.50, 5)
    p3 = Producto("Camiseta", "Ropa", 12.00, 20)

    # Mostrar productos
    print(p1)
    print(p2)
    print(p3)

    # Probar venta
    p1.vender(3)
    print(f"Stock de {p1.nombre} tras vender 3 unidades: {p1.stock}")  # 7

    # Probar reposición
    p2.reponer(10)
    print(f"Stock de {p2.nombre} tras reponer 10 unidades: {p2.stock}")  # 15

    # Probar errores
    try:
        p3.vender(25)  # stock insuficiente
    except ValueError as e:
        print("Error:", e)

    try:
        p1.precio = -10  # precio inválido
    except ValueError as e:
        print("Error:", e)

    # Totales
    print("Total productos creados:", Producto.total_productos())
    print("Productos en categoría 'Electrónica':", Producto.productos_por_categoria("Electrónica"))
    print("Productos en categoría 'Ropa':", Producto.productos_por_categoria("Ropa"))

