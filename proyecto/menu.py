import sys
sys.path.append(r'C:\Users\danie\Documents\python_firsts_steps-main\proyecto')

from funciones.registroCampers import cargar_base_datos, inscribir_camper, enlistar_campers, modificar_camper, eliminar_camper

# Ahora puedes utilizar las funciones importadas

def mostrar_menu():
    while True:
        print("1. Campers")
        print("2. Trainers")
        print("3. Matriculas")
        print("4. Aulas")
        print("5. Reportes")
        print("6. Salir")
        op = input("Seleccione su opcion: ").strip()

        if op == "1":
            cargar_base_datos()
            submenu_camper()  # Llamada correcta a submenu_camper
        elif op == "2":
            # Lógica para Trainers
            pass
        elif op == "3":
            # Lógica para Matriculas
            pass
        elif op == "4":
            # Lógica para Aulas
            pass
        elif op == "5":
            # Lógica para Reportes
            pass
        elif op == "6":
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Inténtelo de nuevo.")

def submenu_camper():
    while True:  # Agregado para que el submenú se repita
        print("1. Inscribir camper")
        print("2. Enlistar campers")
        print("3. Modificar camper")
        print("4. Eliminar camper")
        print("5. Volver al menú principal")
        opcamper = input("Seleccione su opcion: ").strip()

        if opcamper == "1":
            inscribir_camper()
        elif opcamper == "2":
            enlistar_campers()
        elif opcamper == "3":
            modificar_camper()
        elif opcamper == "4":
            eliminar_camper()
        elif opcamper == "5":
            print("Volviendo al menú principal.")
            break
        else:
            print("Opción no válida")

# Ejecutar el programa
mostrar_menu()
