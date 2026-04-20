# ESCRIBA AQUÍ LA CLASE
class CuentaBancaria:
    # descomente la siguiente línea si quiere usarla
    # __titular_suma: dict[str, float] = {}  # diccionario titular: suma saldos
    
    __contador_cuentas = 0
    __titular_suma = {}  # diccionario titular: suma saldos
    
    def __init__(self, titular: str):
        self.__titular = titular
        self.__saldo = 0.0
        
        # Generar código de cuenta automático
        CuentaBancaria.__contador_cuentas += 1
        self.__codigo_cuenta = f"CB-{CuentaBancaria.__contador_cuentas:03d}"
        
        # Actualizar el diccionario de titulares
        if titular in CuentaBancaria.__titular_suma:
            CuentaBancaria.__titular_suma[titular] += self.__saldo
        else:
            CuentaBancaria.__titular_suma[titular] = self.__saldo
    
    @property
    def codigo_cuenta(self) -> str:
        return self.__codigo_cuenta
    
    @property
    def titular(self) -> str:
        return self.__titular
    
    @property
    def saldo(self) -> float:
        return self.__saldo
    
    def depositar(self, cantidad: float):
        if cantidad < 0:
            raise ValueError("La cantidad a depositar no puede ser negativa")
        self.__saldo += cantidad
        CuentaBancaria.__titular_suma[self.__titular] += cantidad
    
    def retirar(self, cantidad: float):
        if cantidad < 0:
            raise ValueError("La cantidad a retirar no puede ser negativa")
        if cantidad > self.__saldo:
            raise ValueError("Saldo insuficiente para realizar la retirada")
        self.__saldo -= cantidad
        CuentaBancaria.__titular_suma[self.__titular] -= cantidad
    
    @classmethod
    def obtener_total_cuentas(cls) -> int:
        return cls.__contador_cuentas
    
    @classmethod
    def total_saldo_titular(cls, titular: str) -> float:
        return cls.__titular_suma.get(titular, 0.0)
    
    def __str__(self) -> str:
        return f"{self.__codigo_cuenta} - Titular: {self.__titular}, Saldo: {self.__saldo}"