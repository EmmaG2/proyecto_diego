class Persona:
    def __init__(
        self, nombre, estado_civil, apellido, edad, escolaridad, promedio, salario
    ):
        self.__nombre = nombre
        self.__estado_civil = estado_civil
        self.__apellido = apellido
        self.__edad = edad
        self.__escolaridad = escolaridad
        self.__promedio = promedio
        self.__salario = salario
        
    def get_nombre(self):
        return self.__nombre

    def get_estado_civil(self):
        return self.__estado_civil

    def get_apellido(self):
        return self.__apellido

    def get_edad(self):
        return self.__edad

    def get_escolaridad(self):
        return self.__escolaridad

    def get_promedio(self):
        return self.__promedio

    def get_salario(self):
        return self.__salario
    
    def __str__(self):
        return (
            f"Persona(nombre={self.__nombre}, estado_civil={self.__estado_civil}, apellido={self.__apellido}, "
            f"edad={self.__edad}, escolaridad={self.__escolaridad}, promedio={self.__promedio}, salario={self.__salario})"
        )
