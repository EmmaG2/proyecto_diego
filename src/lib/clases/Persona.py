class Persona:
    def __init__(
        self, nombre, estado_civil, apellido, edad, escolaridad, promedio, salario
    ):
        self.nombre = nombre
        self.estado_civil = estado_civil
        self.apellido = apellido
        self.edad = edad
        self.escolaridad = escolaridad
        self.promedio = promedio
        self.salario = salario
        
    def get_nombre(self):
        return self.nombre

    def get_estado_civil(self):
        return self.estado_civil

    def get_apellido(self):
        return self.apellido

    def get_edad(self):
        return self.edad

    def get_escolaridad(self):
        return self.escolaridad

    def get_promedio(self):
        return self.promedio

    def get_salario(self):
        return self.salario
    
    def __str__(self):
        return (
            f"Persona(nombre={self.nombre}, estado_civil={self.estado_civil}, apellido={self.apellido}, "
            f"edad={self.edad}, escolaridad={self.escolaridad}, promedio={self.promedio}, salario={self.salario})"
        )
