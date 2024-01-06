import json
import os

def crear_asignar_rutas_profesores():
    try:
        # Imprimir el directorio actual
        print("Directorio actual:", os.getcwd())

        # Verificar si el archivo de profesores existe
        if os.path.isfile("profesores.json"):
            # Cargar la base de datos de profesores desde el archivo existente
            with open("profesores.json", "r") as file:
                data = json.load(file)
        else:
            data = {"profesores": []}
    except FileNotFoundError:
        print("Error: No se encontró la base de datos de profesores.")
        return
    
    print(f"Lista de profesores: {data['profesores']} ")
    for profesor in data["profesores"]:
        print(f"Nombre: {profesor['nombre']}, Ruta: {profesor['rutaprofesor']}")

    nombreprofe = input("Agregue nombre del nuevo profesor: ")
    apellidoprofe = input("Agregue apellido del nuevo profesor: ")
    rutaprofe = input("Agregue ruta del nuevo profesor: ")
    horarioprofe = int(input("Ingrese el horario del profesor: "))
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

crear_asignar_rutas_profesores()
