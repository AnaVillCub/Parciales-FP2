class Empleado:
    __total_empleados = 0
    __por_departamento: dict[str, int] = {}

    def __init__(self, nombre: str, departamento: str, salario: float):
        self.__nombre = nombre
        self.__departamento = departamento

        if salario <= 0:
            raise ValueError("El salario debe ser mayor que 0")
        self.__salario = salario

        Empleado.__total_empleados += 1
        Empleado.__por_departamento[departamento] = Empleado.__por_departamento.get(departamento, 0) + 1 # Reformular

    @property
    def nombre(self):
        return self.__nombre

    @property
    def departamento(self):
        return self.__departamento

    @property
    def salario(self):
        return self.__salario

    @salario.setter
    def salario(self, nuevo_salario: float):
        if not isinstance(nuevo_salario, (int, float)) or nuevo_salario <= 0:
            raise ValueError("El salario debe ser un número positivo")
        self.__salario = nuevo_salario

    def subir_salario(self, porcentaje: float):
        if porcentaje <= 0:
            raise ValueError("El porcentaje debe ser mayor que 0")
        self.__salario += self.__salario * (porcentaje / 100)

    @classmethod
    def total_empleados(cls):
        return cls.__total_empleados

    @classmethod
    def empleados_departamento(cls, depto: str):
        return cls.__por_departamento.get(depto, 0)

    def __str__(self):
        return f"{self.__nombre} - {self.__departamento} - {self.__salario} €"
