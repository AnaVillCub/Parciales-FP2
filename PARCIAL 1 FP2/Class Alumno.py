class Alumno:
    __total_alumnos = 0
    __suma_notas = 0
    
    def __init__(self, nombre: str, curso: str, nota: float):
        self.__nombre = nombre
        self.__curso = curso
        if nota < 0 or nota > 10:
            raise ValueError("Nota invalida")
        self.__nota = nota
        
        # CONTAMOS ALUMNOS
        Alumno.__total_alumnos += 1
        Alumno.__suma_notas += nota
    
    @property
    def nombre(self):
        return self.__nombre
    @property
    def curso(self):
        return self.__curso
    @property
    def nota(self):
        return self.__nota
    @nota.setter
    def nota(self, valor):
        if valor < 0 or valor > 10:
            raise ValueError("Valor invalido")
        # Actualiza la suma total restando la antigua y sumando la nueva
        Alumno.__suma_notas += valor - self.__nota
        self.__nota = valor
    
    @classmethod
    def total_alumnos(cls):
        return cls.__total_alumnos
    @classmethod
    def media_notas(cls):
        if cls.__suma_notas == 0:
            return 0.0
        return round(cls.__suma_notas / cls.__total_alumnos, 2)
    
    def __str__(self):
        return f"<{self.__nombre}> - <{self.__curso}> - Nota: <{self.__nota}>"

    
if __name__ == "__main__":
    # Crear alumnos
    a1 = Alumno("Sofía", "1º ESO", 8.5)
    a2 = Alumno("Lucas", "1º ESO", 6.0)
    a3 = Alumno("Valeria", "2º ESO", 9.2)

    # Mostrar alumnos
    print(a1)
    print(a2)
    print(a3)

    # Cambiar nota (válido)
    a2.nota = 7.5
    print(f"Nueva nota de {a2.nombre}: {a2.nota}")

    # Probar nota inválida
    try:
        a3.nota = 11.0
    except ValueError as e:
        print("Error:", e)

    # Estadísticas globales
    print("Total de alumnos:", Alumno.total_alumnos())
    print("Media de notas:", Alumno.media_notas())
