class Pelicula:
    
    __listado_peliculas: dict[str, int] = {} # Director: peliculas
    __total_peliculas = 0
    
    def __init__(self, titulo: str, director: str, año: int):
        self.__titulo = titulo
        self.__director = director
        self.__año = año
    
        self.__alquilada = False # Al crearse, la película no está alquilada
        
        #Contador de peliculas
        Pelicula.__total_peliculas += 1
        
        if director in Pelicula.__listado_peliculas:
            Pelicula.__listado_peliculas[director] += 1
        else:
            Pelicula.__listado_peliculas[director] = 1
        
        
    @property
    def titulo(self):
        return self.__titulo
    @property
    def director(self):
        return self.__director
    @property
    def año(self):
        return self.__año
    @property
    def alquilada(self):
        return self.__alquilada
    @alquilada.setter
    def alquilada(self, valor: bool):
        if not isinstance(valor, bool):
            raise ValueError("El estado de alquiler debe ser booleano")
        self.__alquilada = valor
    
    def alquilar(self):
        if self.__alquilada:
            raise ValueError("La Película Está alquilada")
        self.__alquilada = True
    def devolver(self):
        if not self.__alquilada:
            raise ValueError("La Película Está Devuelta")
        self.__alquilada = False
    
    @classmethod
    def total_peliculas(cls):
        return cls.__total_peliculas
    @classmethod
    def peliculas_director(cls, director):
        return cls.__listado_peliculas.get(director, 0)
        
    # Representación informal
    def __str__(self):
        estado = None
        if self.__alquilada:
            estado = "Alquilada" 
        else:
            estado = "Disponible"
        return f'"{self.__titulo}" dirigida por {self.__director} ({self.__año}) - {estado}'

    
    
p = Pelicula("Inception", "Christopher Nolan", 2010)
print(p)  # "Inception" dirigida por Christopher Nolan (2010) - Disponible
p.alquilar()
print(p)  # "Inception" dirigida por Christopher Nolan (2010) - Alquilada
