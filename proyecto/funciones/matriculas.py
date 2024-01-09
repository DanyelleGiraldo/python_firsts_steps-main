import json

def cargar_base_datos():
    try:
        with open("campersInscritos.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {"campers": []}
    return data

def matricula_camper():
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
            nuevo_ruta= input("ingrese la nueva ruta: ")
            nuevo_profesor= input("ingrese el nuevo profesor: ")
            fecha_de_inicio= input("ingrese la fecha de inicio: ")
            fecha_de_finalizacion= input("ingrese la fecha de finalizacion")
            

            # Aplicar las modificaciones
            camper["nombre"] = nuevo_nombre
            camper["apellidos"] = nuevo_apellido
            camper["direccion"] = nueva_direccion
            camper["acudiente"] = nuevo_acudiente
            camper["telefonos"]["celular"] = nuevo_celular
            camper["telefonos"]["fijo"] = nuevo_fijo
            camper["ruta_elegida"]= nuevo_ruta
            camper["profesor"]= nuevo_profesor
            camper["fechadeinicio"]= fecha_de_inicio
            camper["fechafinal"]= fecha_de_finalizacion

            # Guardar la base de datos actualizada
            with open("campersInscritos.json", "w") as file:
                json.dump(data, file, indent=2)

            print(f"Camper ID {id_modificar} modificado exitosamente.")
            return

    print(f"No se encontró ningún camper con el ID {id_modificar}.")