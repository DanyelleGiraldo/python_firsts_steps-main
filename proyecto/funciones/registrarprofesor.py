import json
import os

def cargar_base_datos_profesores():
    try:
        with open("profesores.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {"profesores": []}
    return data

def enlistar_profesores():
    data = cargar_base_datos_profesores()

    if data["profesores"]:
        print("Lista de profesores:")
        for profesor in data["profesores"]:
            print(f"Nombre: {profesor['nombre']} {profesor['apellido']}, Ruta: {profesor['rutaprofesor']}, Horario: {profesor['horarioprofe']}, Salón: {profesor['salonprofe']}")
    else:
        print("No hay profesores registrados.")

def crear_asignar_rutas_profesores():
    data = cargar_base_datos_profesores()

    print("Lista de profesores:")
    for profesor in data["profesores"]:
        print(f"Nombre: {profesor['nombre']} {profesor['apellido']}, Ruta: {profesor['rutaprofesor']}, Horario: {profesor['horarioprofe']}, Salón: {profesor['salonprofe']}")

    nombreprofe = input("Agregue nombre del nuevo profesor: ")
    apellidoprofe = input("Agregue apellido del nuevo profesor: ")
    rutaprofe = input("Agregue ruta del nuevo profesor: ")
    horarioprofe = input("Ingrese el horario del profesor: ")
    salonprofe = input("Ingrese el salon del profesor: ")

    new_profesor = {
        "nombre": nombreprofe,
        "apellido": apellidoprofe,
        "rutaprofesor": rutaprofe,
        "horarioprofe": horarioprofe,
        "salonprofe": salonprofe
    }

    # Agregar el nuevo profesor a la base de datos
    data["profesores"].append(new_profesor)

    # Guardar la base de datos actualizada
    with open("profesores.json", "w") as file:
        json.dump(data, file, indent=2)

    print("Profesor inscrito exitosamente.")

# Ejecutar el programa
enlistar_profesores()
crear_asignar_rutas_profesores()
