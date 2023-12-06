from lib.builders.PersonaBuilder import PersonaBuilder

from lib.menus.MenuUno import menu_uno
from lib.menus.MenuDos import menu_dos

from logic.AddPersons import add_person

from logic.imprimarDatosPersonas import imprimir_datos_personas, imprimir_datos_escolares, imprimir_salarios

opcion = -1
personas = []

while opcion != 3:
    menu_uno()
    opcion = int(input())
    
    if opcion == 1:
        add_person(personas)
        
    elif opcion == 2:
        opcion2 = -1
        
        while opcion2 != 7:
            menu_dos()
            opcion2 = int(input())
            
            if opcion2 == 4:
                imprimir_datos_personas(personas)
            elif opcion2 == 5:
                imprimir_datos_escolares(personas)
            elif opcion2 == 6:
                imprimir_salarios(personas)
        