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
            nombre = profesor.get("nombre", "Nombre no disponible")
            apellido = profesor.get("apellido", "Apellido no disponible")
            ruta = profesor.get("ruta", "Ruta no disponible")
            horario = profesor.get("horario", "Horario no disponible")
            salon = profesor.get("salon", "Salón no disponible")
            print(f"Nombre: {nombre} {apellido}, Ruta: {ruta}, Horario: {horario}, Salón: {salon}")
    else:
        print("No hay profesores registrados.")

def crear_asignar_rutas_profesores():
    data = cargar_base_datos_profesores()

    print("Lista de profesores:")
    for profesor in data["profesores"]:
        nombre = profesor.get("nombre", "Nombre no disponible")
        apellido = profesor.get("apellido", "Apellido no disponible")
        ruta = profesor.get("ruta", "Ruta no disponible")
        horario = profesor.get("horario", "Horario no disponible")
        salon = profesor.get("salon", "Salón no disponible")
        print(f"Nombre: {nombre} {apellido}, Ruta: {ruta}, Horario: {horario}, Salón: {salon}")

    nombreprofe = input("Agregue nombre del nuevo profesor: ")
    apellidoprofe = input("Agregue apellido del nuevo profesor: ")
    rutaprofe = input("Agregue ruta del nuevo profesor: ")
    horarioprofe = input("Ingrese el horario del profesor: ")
    salonprofe = input("Ingrese el salon del profesor: ")

    new_profesor = {
        "nombre": nombreprofe,
        "apellido": apellidoprofe,
        "ruta": rutaprofe,
        "horario": horarioprofe,
        "salon": salonprofe
    }

    # Agregar el nuevo profesor a la base de datos
    data["profesores"].append(new_profesor)

    # Guardar la base de datos actualizada
    with open("profesores.json", "w") as file:
        json.dump(data, file, indent=2)

    print("Profesor inscrito exitosamente.")

def eliminar_profesor(nombreprofe):
    data = cargar_base_datos_profesores()

    profesores = data["profesores"]
    profesor_encontrado = None

    for profesor in profesores:
        if profesor.get("nombre", "") == nombreprofe:
            profesor_encontrado = profesor
            break

    if profesor_encontrado:
        profesores.remove(profesor_encontrado)
        with open("profesores.json", "w") as file:
            json.dump(data, file, indent=2)
        print(f"Profesor {profesor_encontrado['nombre']} {profesor_encontrado['apellido']} eliminado correctamente.")
    else:
        print(f"No se encontró ningún profesor con el nombre {nombreprofe}.")

def modificar_profesor(nombre):
    data = cargar_base_datos_profesores()

    profesores = data["profesores"]
    profesor_encontrado = None

    for profesor in profesores:
        if profesor.get("ruta") == nombre:
            profesor_encontrado = profesor
            break

    if profesor_encontrado:
        print(f"Modificando profesor: {profesor_encontrado['nombre']} {profesor_encontrado['apellido']}")
        nombreprofe = input("Nuevo nombre (deje en blanco para mantener el actual): ") or profesor_encontrado['nombre']
        apellidoprofe = input("Nuevo apellido (deje en blanco para mantener el actual): ") or profesor_encontrado['apellido']
        horarioprofe = input("Nuevo horario (deje en blanco para mantener el actual): ") or profesor_encontrado['horario']
        salonprofe = input("Nuevo salón (deje en blanco para mantener el actual): ") or profesor_encontrado['salon']
        rutaprofe = input("Nueva ruta del profesor (deje en blanco para mantener el actual: )"or profesor_encontrado['ruta'])

        profesor_modificado = {
            "nombre": nombreprofe,
            "apellido": apellidoprofe,
            "ruta": rutaprofe,
            "horario": horarioprofe,
            "salon": salonprofe
        }

        profesores.remove(profesor_encontrado)
        profesores.append(profesor_modificado)

        with open("profesores.json", "w") as file:
            json.dump(data, file, indent=2)

        print("Profesor modificado exitosamente.")
    else:
        print(f"No se encontró ningún profesor el nombre {nombre}.")
        

def enlistar_salones_con_datos():
    try:
        # Cargar la base de datos de profesores desde el archivo existente
        with open("profesores.json", "r") as file:
            profesores_data = json.load(file)
    except FileNotFoundError:
        print("Error: No se encontró la base de datos de profesores.")
        return

    print("Lista de profesores con datos del salón:")
    for profesor in profesores_data["profesores"]:
        nombre = profesor.get("nombre", "Nombre no disponible")
        apellido = profesor.get("apellido", "Apellido no disponible")
        ruta = profesor.get("ruta", "Ruta no disponible")
        horario = profesor.get("horario", "Horario no disponible")
        salon = profesor.get("salon", "Salón no disponible")
        print(f"Nombre: {nombre} {apellido}, Ruta: {ruta}, Horario: {horario}, Salón: {salon}")