from lib.clases.Persona import Persona
from typing import List

def imprimir_datos_personas(personas: List[Persona]):
    for person in personas:
        print(person)
        print()
        
def imprimir_datos_escolares(personas: List[Persona]):
    for person in personas:
        print("Escolaridad:", person.get_escolaridad())
        print("Promedio:", person.get_promedio())
        print()
        
def imprimir_salarios(personas: List[Persona]):
    for person in personas:
        print("Salario:", person.get_salario())
        print()