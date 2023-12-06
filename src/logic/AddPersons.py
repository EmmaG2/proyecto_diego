from src.lib.builders.PersonaBuilder import PersonaBuilder
from src.lib.clases.Persona import Persona
from typing import List

def add_person(personas: List[Persona]):
    n = 0
    
    while n < 3:
        name = input("Nombre: ")
        persona_builder = PersonaBuilder(name)
        apellido = input("Apellido: ")
        edad = int(input("Edad: "))
        estado_civil = input("Estado civil: ")
        escolaridad = input("Escolaridad: ")
        promedio = float(input("Promedio: "))
        salario = float(input("Salario: "))
        
        persona = (
            persona_builder.set_apellido(apellido)
            .set_edad(edad)
            .set_escolaridad(escolaridad)
            .set_estado_civil(estado_civil)
            .set_promedio(promedio)
            .set_salario(salario)
            .build()
        )
        
        
        
        n = n + 1;
        personas.append(persona)
