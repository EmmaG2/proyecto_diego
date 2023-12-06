from src.lib.clases.Persona import Persona

class PersonaBuilder:
    def __init__(self, nombre):
        self.nombre = nombre
        self.estado_civil = None
        self.apellido = None
        self.edad = None
        self.escolaridad = None
        self.promedio = None
        self.salario = None

    def set_estado_civil(self, estado_civil):
        self.estado_civil = estado_civil
        return self

    def set_apellido(self, apellido):
        self.apellido = apellido
        return self

    def set_edad(self, edad):
        self.edad = edad
        return self

    def set_escolaridad(self, escolaridad):
        self.escolaridad = escolaridad
        return self

    def set_promedio(self, promedio):
        self.promedio = promedio
        return self

    def set_salario(self, salario):
        self.salario = salario
        return self

    def build(self):
        return Persona(
            self.nombre,
            self.estado_civil,
            self.apellido,
            self.edad,
            self.escolaridad,
            self.promedio,
            self.salario,
        )
