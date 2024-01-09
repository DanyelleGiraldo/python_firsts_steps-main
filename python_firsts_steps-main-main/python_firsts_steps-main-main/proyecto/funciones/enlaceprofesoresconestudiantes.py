import json
import os

def enlazar_estudiantes_con_profesor():
    try:
        # Imprimir el directorio actual
        print("Directorio actual:", os.getcwd())

        # Cargar la base de datos de campers desde el archivo existente
        with open("campersInscritos.json", "r") as file:
            campers_data = json.load(file)
    except FileNotFoundError:
        print("Error: No se encontró la base de datos de campers.")
        return
    
    try:
        # Cargar la base de datos de profesores desde el archivo existente
        with open("profesores.json", "r") as file:
            profesores_data = json.load(file)
    except FileNotFoundError:
        print("Error: No se encontró la base de datos de profesores.")
        return
    
    for camper in campers_data["campers"]:
        if "ruta_elegida" in camper and camper["ruta_elegida"] is not None:
            # Buscar profesor con la misma ruta
            for profesor in profesores_data["profesores"]:
                if profesor.get("ruta") == camper.get("ruta_elegida"):
                    # Agregar información del profesor al estudiante si las rutas coinciden
                    if camper["ruta_elegida"] == profesor["ruta"]:
                        camper["profesor"] = f"{profesor['nombre']} ({profesor['ruta']})"
    
    # Guardar la base de datos de campers actualizada
    with open("campersInscritos.json", "w") as file:
        json.dump(campers_data, file, indent=2)

    print("Enlace de estudiantes con profesores completado.")

