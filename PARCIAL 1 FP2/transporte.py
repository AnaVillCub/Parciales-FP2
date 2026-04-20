# ESCRIBA AQUÍ LA CLASE
class TarjetaTransporte:
    # descomente la siguiente línea si quiere usarla
    __viajes_titular: dict[str, int] = {}  # titular: número de viajes
    __contador_tarjetas = 1000000

    def __init__(self, titular: str):
        self.__titular = titular
        self.__viajes_realizados = 0
        self.__saldo = 0.0
        
        # Contador de tarjetas
        self.__contador_tarjetas += 1
        self.__numero_tarjeta = f"TT-{self.__contador_tarjetas}"
        
        # Crear conteo viajes si titular no existe
        if titular not in TarjetaTransporte.__viajes_titular:
            TarjetaTransporte.__viajes_titular[titular] = 0
        
    @property
    def titular(self):
        return self.__titular
    @property
    def numero_tarjeta(self):
        return self.__numero_tarjeta
    @property
    def saldo(self):
        return self.__saldo
    @property
    def viajes_realizados(self):
        return self.__viajes_realizados


    def recargar(self, cantidad):
        if cantidad < 0:
            raise ValueError("Cantidad Inválida")
        self.__saldo += cantidad


    def viajar(self, costo_viaje: float):
        if self.__saldo < costo_viaje or costo_viaje < 0.0:
            raise ValueError("Insuficiente")
        self.__saldo -= costo_viaje
        self.__viajes_realizados += 1
        TarjetaTransporte.__viajes_titular[self.__titular] += 1
        
    @classmethod
    def total_tarjetas_emitidas(cls):
        return cls.__contador_tarjetas - 1000000
    
    @classmethod
    def viajes_titular(cls, nombre_titular: str):
        return cls.__viajes_titular.get(nombre_titular, 0)
    """if nombre_titular in cls.__viajes_titular:
            return cls.__viajes_titular[nombre_titular]"""
            
    def __str__(self):
        return f'{self.__numero_tarjeta} - Titular: {self.__titular}, Saldo: {self.__saldo}'
