class CuentaBancaria:
    # descomente la siguiente línea si quiere usarla
    __titular_suma: dict[str, float] = {}  # diccionario titular: suma saldos
    __contador_cuentas = 0 # Saldo actual

    def __init__(self, titular: str):
        self.__titular = titular
        self.__saldo = 0.0
        
        # Creamos codigo de cuenta automatico
        CuentaBancaria.__contador_cuentas += 1
        self.__codigo_cuenta = f"CB-{CuentaBancaria.__contador_cuentas:03d}"
        
        # Actualizar el diccionario de titulares
        if titular in CuentaBancaria.__titular_suma:
            CuentaBancaria.__titular_suma[titular] += self.__saldo
        else:
            CuentaBancaria.__titular_suma[titular] = self.__saldo
        
    @property
    def codigo_cuenta(self):
        return self.__codigo_cuenta
    @property
    def titular(self):
        return self.__titular
    @property
    def saldo(self):
        return self.__saldo
    
    
    def depositar(self, cantidad: float):
        if cantidad < 0.0:
            raise ValueError("Ingreso Negativo")
        self.__saldo += cantidad # Modifica el saldo
        # Modificar el saldo en cuenta
        CuentaBancaria.__titular_suma[self.__titular] += cantidad
    
    def retirar(self, cantidad: float):
        if cantidad > self.__saldo or cantidad < 0:
            raise ValueError("Retiradas Inválidas")
        self.__saldo -= cantidad
        CuentaBancaria.__titular_suma[self.__titular] -= cantidad
        
    @classmethod
    def obtener_total_cuentas(cls):
        return cls.__contador_cuentas
    
    @classmethod
    def total_saldo_titular(cls, titular):
        # return cls.__por_autor[autor] tambien valdría pero podría dar un error
        return cls.__titular_suma.get(titular, 0.0) # Valor por defecto
        
    def __str__(self):
        return f'{self.__codigo_cuenta} - Titular {self.__titular}, Saldo: {self.__saldo}'




