# ESCRIBA AQUÍ LA CLASE
class Libro:
    # descomente la siguiente línea si quiere usarla
    # __autor_número: dict[str, int] = {}  # diccionario autor: nº libros

    __total_libros = 0
    __autor_numero = {}  # diccionario autor: nº libros
    
    def __init__(self, titulo: str, autor: str, fecha: int):
        self.__titulo = titulo
        self.__autor = autor
        self.__fecha = fecha
        self.__prestado = False
        
        # Actualizar contadores
        Libro.__total_libros += 1
        if autor in Libro.__autor_numero:
            Libro.__autor_numero[autor] += 1
        else:
            Libro.__autor_numero[autor] = 1
    
    @property
    def titulo(self) -> str:
        return self.__titulo
    
    @property
    def autor(self) -> str:
        return self.__autor
    
    @property
    def fecha(self) -> int:
        return self.__fecha
    
    @property
    def prestado(self) -> bool:
        return self.__prestado
    
    @prestado.setter
    def prestado(self, valor: bool):
        if not isinstance(valor, bool):
            raise ValueError("El valor de prestado debe ser booleano")
        self.__prestado = valor
    
    def prestar(self):
        if self.__prestado:
            raise ValueError("El libro ya está prestado")
        self.__prestado = True
    
    def devolver(self):
        if not self.__prestado:
            raise ValueError("El libro no está prestado")
        self.__prestado = False
    
    @classmethod
    def total_libros(cls) -> int:
        return cls.__total_libros
    
    @classmethod
    def publicados_autor(cls, autor: str) -> int:
        return cls.__autor_numero.get(autor, 0)
    
    def __str__(self) -> str:
        estado = "Prestado" if self.__prestado else "Disponible"
        return f'"{self.__titulo}" por {self.__autor} ({self.__fecha}) - {estado}'