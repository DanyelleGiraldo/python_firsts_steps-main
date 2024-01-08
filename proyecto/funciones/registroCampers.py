import json

def cargar_base_datos():
    try:
        with open("campersInscritos.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {"campers": []}
    return data

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

def enlistar_campers():
    data = cargar_base_datos()

    if data["campers"]:
        print("Listado de campers inscritos:")
        for camper in data["campers"]:
            print(f"ID: {camper['id']}, Nombre: {camper['nombre']} {camper['apellidos']}, Estado: {camper['estado']}")
    else:
        print("No hay campers inscritos.")

def modificar_camper():
    data = cargar_base_datos()

    id_modificar = input("Ingrese el ID del camper a modificar: ")

    for camper in data["campers"]:
        if camper["id"] == id_modificar:
            print(f"Datos actuales del camper ID {id_modificar}:")
            print(json.dumps(camper, indent=2))

            # Solicitar las modificaciones
            nuevo_nombre = input("Nuevo nombre del camper: ")
            nuevo_apellido = input("Nuevos apellidos del camper: ")
            nueva_direccion = input("Nueva dirección del camper: ")
            nuevo_acudiente = input("Nuevo nombre del acudiente del camper: ")
            nuevo_celular = input("Nuevo número de celular del camper: ")
            nuevo_fijo = input("Nuevo número fijo del camper: ")

            # Aplicar las modificaciones
            camper["nombre"] = nuevo_nombre
            camper["apellidos"] = nuevo_apellido
            camper["direccion"] = nueva_direccion
            camper["acudiente"] = nuevo_acudiente
            camper["telefonos"]["celular"] = nuevo_celular
            camper["telefonos"]["fijo"] = nuevo_fijo

            # Guardar la base de datos actualizada
            with open("campersInscritos.json", "w") as file:
                json.dump(data, file, indent=2)

            print(f"Camper ID {id_modificar} modificado exitosamente.")
            return

    print(f"No se encontró ningún camper con el ID {id_modificar}.")

def eliminar_camper():
    data = cargar_base_datos()

    id_eliminar = input("Ingrese el ID del camper a eliminar: ")

    for camper in data["campers"]:
        if camper["id"] == id_eliminar:
            data["campers"].remove(camper)

            # Guardar la base de datos actualizada
            with open("campersInscritos.json", "w") as file:
                json.dump(data, file, indent=2)

            print(f"Camper ID {id_eliminar} eliminado exitosamente.")
            return

    print(f"No se encontró ningún camper con el ID {id_eliminar}.")

# Ejecutar el programa
inscribir_camper()
