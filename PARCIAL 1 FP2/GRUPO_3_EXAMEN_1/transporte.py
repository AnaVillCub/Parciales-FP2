# ESCRIBA AQUÍ LA CLASE
class TarjetaTransporte:
    # descomente la siguiente línea si quiere usarla
    # __viajes_titular: dict[str, int] = {}  # titular: número de viajes

    __contador_tarjetas = 1000000  # Empezamos en 1000001
    __viajes_por_titular = {}  # Diccionario para llevar el conteo de viajes por titular
    
    def __init__(self, titular: str):
        self.__titular = titular
        self.__saldo = 0.0
        self.__viajes_realizados = 0
        
        # Generar número de tarjeta único
        TarjetaTransporte.__contador_tarjetas += 1
        self.__numero_tarjeta = f"TT-{TarjetaTransporte.__contador_tarjetas}"
        
        # Inicializar conteo de viajes para el titular si no existe
        if titular not in TarjetaTransporte.__viajes_por_titular:
            TarjetaTransporte.__viajes_por_titular[titular] = 0
    
    @property
    def numero_tarjeta(self) -> str:
        return self.__numero_tarjeta
    
    @property
    def titular(self) -> str:
        return self.__titular
    
    @property
    def saldo(self) -> float:
        return self.__saldo
    
    @property
    def viajes_realizados(self) -> int:
        return self.__viajes_realizados
    
    def recargar(self, cantidad: float):
        if cantidad < 0:
            raise ValueError("La cantidad a recargar no puede ser negativa")
        self.__saldo += cantidad
    
    def viajar(self, costo_viaje: float):
        if costo_viaje < 0:
            raise ValueError("El costo del viaje no puede ser negativo")
        if self.__saldo < costo_viaje:
            raise ValueError("Saldo insuficiente para realizar el viaje")
        
        self.__saldo -= costo_viaje
        self.__viajes_realizados += 1
        TarjetaTransporte.__viajes_por_titular[self.__titular] += 1
    
    @classmethod
    def total_tarjetas_emitidas(cls) -> int:
        return cls.__contador_tarjetas - 1000000  # Restamos el valor inicial
    
    @classmethod
    def viajes_titular(cls, nombre_titular: str) -> int:
        return cls.__viajes_por_titular.get(nombre_titular, 0)
    
    def __str__(self) -> str:
        return f"{self.__numero_tarjeta} - Titular: {self.__titular}, Saldo: {self.__saldo}, Viajes: {self.__viajes_realizados}"