# ESCRIBA AQUÍ LA CLASE
class Libro:
    # descomente la siguiente línea si quiere usarla
    
    # Atributos de clase para contadores
    __autor_número: dict[str, int] = {}  # diccionario autor: nº libros
    __total_libros = 0
    
    def __init__(self, titulo: str, autor: str, fecha: int):
        # Atributos de instancia privados
        self.__titulo = titulo
        self.__autor = autor
        self.__fecha = fecha
        self.__prestado = False # Por defecto
        
        # Actualizar diccionario
        Libro.__total_libros += 1 # Contamos el libro de la clase
        if autor in Libro.__autor_número: # Si el autor está en el atributo, sumamos 1 al numero de libros
            Libro.__autor_número[autor] += 1
        else:
            Libro.__autor_número[autor] = 1 # Si el autor no existe, se añade
    
    # Propiedades: titulo, autor, fecha (solo lectura)
    @property
    def titulo(self):
        return self.titulo
    @property
    def autor(self):
        return self.__autor
    @property
    def fecha(self) -> int: # devuelve un int, aunque no es extricamente necesario la flecha
        return self.__fecha
    # Propiedad: prestado (lectura/escritura + validación)
    @property
    def prestado(self):
        return self.__prestado
    @prestado.setter
    def prestado(self, valor: bool):
        if self.__prestado:
            raise ValueError("El libro ya está prestado")
        self.__prestado = valor # Aquí es donde damos valor al presto o no del libro
    # Es lo mismo que el setter de prestar, pq estamos habilitando la propiedad de prestar
    def prestar(self):
        if self.__prestado:
            raise ValueError("Ya prestado")
        self.__prestado = True
        
    def devolver(self):
        if not self.prestado:
            raise ValueError("Devuelto el libro")
        self.__prestado = False
    
    @classmethod
    def total_libros(cls):
        return cls.__total_libros
    
    @classmethod
    def publicados_autor(cls, autor):
        if autor in cls.__autor_número:
            return cls.__autor_número[autor]
    
    def __str__(self):
        estado = None
        if self.__prestado:
            estado = "Prestado"
        else:
            estado = "Disponible"
        return f'"{self.__titulo}" por {self.__autor} ({self.__fecha}) - {estado}'
    