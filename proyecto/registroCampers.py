import json

def inscribir_camper():
    # Obtener información del camper
    id_camper = input("Ingrese el número de identificación del camper: ")
    nombre = input("Ingrese el nombre del camper: ")
    apellidos = input("Ingrese los apellidos del camper: ")
    direccion = input("Ingrese la dirección del camper: ")
    acudiente = input("Ingrese el nombre del acudiente del camper: ")
    celular = input("Ingrese el número de celular del camper: ")
    fijo = input("Ingrese el número fijo del camper: ")
    estado = "Matriculado"  # Por defecto, se asume que el camper está matriculado

    # Crear diccionario con la información del camper
    camper = {
        "id": id_camper,
        "nombre": nombre,
        "apellidos": apellidos,
        "direccion": direccion,
        "acudiente": acudiente,
        "telefonos": {
            "celular": celular,
            "fijo": fijo
        },
        "estado": estado
    }

    # Cargar la base de datos 
    try:
        with open("campersInscritos.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {"campers": []}

    # Agregar el nuevo camper a la base de datos
    data["campers"].append(camper)

    # Guardar la base de datos actualizada
    with open("campersInscritos.json", "w") as file:
        json.dump(data, file, indent=2)

    print("Camper inscrito exitosamente.")

# Ejecutar el programa
inscribir_camper()
