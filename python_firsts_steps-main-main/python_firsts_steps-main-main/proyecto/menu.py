import sys
from funciones.registroCampers import cargar_base_datos, inscribir_camper, enlistar_campers, modificar_camper, eliminar_camper
from funciones.registrarprofesor import  crear_asignar_rutas_profesores, enlistar_profesores, modificar_profesor, eliminar_profesor, enlistar_salones_con_datos

# Agrega el directorio principal de tu proyecto al path
sys.path.append('..')

# Ahora puedes importar los módulos relativos
from funciones.registroCampers import cargar_base_datos, inscribir_camper, enlistar_campers, modificar_camper, eliminar_camper
from funciones.registropuerba import listar_campers_aprobados
from funciones.filtrocamper import enlistar_campers_en_riesgo
from funciones.matriculas import matricula_camper
from funciones.reportes import *
from funciones.crearyenlistarrutas import crear_rutas
from funciones.registropuerba import registrar_notas
from funciones.rutasAprobados import *
from funciones.filtrocamper import *

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
            submenu_trainer() # Llamada correcta a submenu_trainer()
            pass
        elif op == "3":
            submenu_matriculas() # Lógica para Matriculas
            pass
        elif op == "4":
            submenu_aulas() # Lógica para Aulas
            pass
        elif op == "5":
            submenu_reportes() # Lógica para Reportes
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
        print("5. Prueba admision")
        print("6. Asignarle ruta")
        print("7. Modificarle ruta")
        print("8. Filtro camper")
        print("9. Volver al menú principal")
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
            registrar_notas()
        elif opcamper == "6":
            inscribir_candidato()
        elif opcamper == "7":
            modificar_ruta_camper()
        elif opcamper == "8":
            evaluar_camper()
        elif opcamper == "9":
            print("Volviendo al menú principal.")
            break
        else:
            print("Opción no válida")
            
def submenu_trainer():
    while True:  # Agregado para que el submenú se repita
        print("1. Inscribir trainer")
        print("2. Enlistar trainer")
        print("3. Modificar trainer")
        print("4. Eliminar trainer")
        print("5. Volver al menú principal")
        optrainer = input("Seleccione su opcion: ").strip()

        if optrainer == "1":
           crear_asignar_rutas_profesores()
        elif optrainer == "2":
            enlistar_profesores()
        elif optrainer == "3":
            enlistar_profesores()
            rutaprofe= input("cual es el nombre del profesor?: ")
            modificar_profesor(rutaprofe)
        elif optrainer == "4":
             enlistar_profesores()
             nombreprofe= input("cual es el nombre del profesor?: ")
             eliminar_profesor(nombreprofe)            
        elif optrainer == "5":
            print("Volviendo al menú principal.")
            break
        else:
            print("Opción no válida")     

def submenu_matriculas():
    while True:  # Agregado para que el submenú se repita
        print("1. Modificar camper")
        print("2. Volver al menú principal")
        optrainer = input("Seleccione su opcion: ").strip()

        if optrainer == "1":
            matricula_camper()            
        elif optrainer == "2":
            print("Volviendo al menú principal.")
            break
        else:
            print("Opción no válida")
            
def submenu_aulas():
    while True:  # Agregado para que el submenú se repita
        print("1. Enlistar Aula")
        print("2. Crear rutas")
        print("3. Volver al menú principal")
        optrainer = input("Seleccione su opcion: ").strip()

        if optrainer == "1":
            enlistar_salones_con_datos()
        elif optrainer == "2":
            crear_rutas()            
        elif optrainer == "3":
            print("Volviendo al menú principal.")
            break
        else:
            print("Opción no válida")


def submenu_reportes():
    while True:  # Agregado para que el submenú se repita
        print("1. Listar los campers que se encuentren en estado de inscrito.")
        print("2. Listar los campers que aprobaron el examen inicial.")
        print("3. Listar los entrenadores que se encuentran trabajando con campuslands.")
        print("4. Listar los estudiantes que cuentan con bajo rendimiento.")
        print("5. Listar los campers y entrenador que se encuentren asociados a una ruta de entrenamiento.")
        print("""6. Mostrar cuantos campers perdieron y aprobaron cada uno de los modulos teniendo en cuenta
              la ruta de entrenamiento y el entrenador encargado""")
        print("7. Volver al menú principal")
        opreporte = input("Seleccione su opcion: ").strip()

        if opreporte == "1":
            enlistar_campers()
        elif opreporte == "2":
            listar_campers_aprobados()
        elif opreporte == "3":
            enlistar_profesores()
        elif opreporte == "4":
            enlistar_campers_en_riesgo()
        elif opreporte == "5":
            ruta= input("elija la ruta: ")
            listar_campers_entrenador_por_ruta(ruta)
        elif opreporte == "6":
            ruta= input("ingrese la ruta: ")
            profesor= input("ingrese el profesor: ")
            contar_aprobados_perdidos(ruta, profesor)
        elif opreporte == "7":
            print("Volviendo al menú principal.")
            break
        else:
            print("Opción no válida")      

# Ejecutar el programa
mostrar_menu()
