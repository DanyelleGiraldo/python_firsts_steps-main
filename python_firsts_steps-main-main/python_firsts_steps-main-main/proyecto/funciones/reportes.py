import json

def cargar_base_datos_campers():
    try:
        with open("campersInscritos.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {"campers": []}
    return data

def cargar_base_datos_profesores():
    try:
        with open("profesores.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {"profesores": []}
    return data

def contar_aprobados_perdidos(ruta, entrenador):
    try:
        with open("campersInscritos.json", "r") as file:
            campers = json.load(file)
    except FileNotFoundError:
        print("Error: No se encontró la base de datos.")
        return None

    aprobados = 0
    perdidos = 0

    for camper in campers:
        if camper["ruta_elegida"] == ruta and camper["profesor"] == entrenador:
            if camper["filtro"] == "aprobado":
                aprobados += 1
            else:
                perdidos += 1

    return aprobados, perdidos

def listar_campers_entrenador_por_ruta(ruta):
    datacamper = cargar_base_datos_campers()
    dataprofe = cargar_base_datos_profesores()

    if datacamper["campers"] and dataprofe["profesores"]:
        print("Listado de campers inscritos:")
        for camper in datacamper["campers"]:
            if camper['estado'] == 'Aprobado':
                ruta_camper = camper['ruta_elegida']
                profesor_ruta = next((profesor['ruta'] for profesor in dataprofe["profesores"] if profesor['nombre'] in camper['profesor']), None)

                if ruta_camper == ruta and profesor_ruta == ruta:
                    print(f"ID: {camper['id']}, Nombre: {camper['nombre']} {camper['apellidos']}, Estado: {camper['estado']}")
    else:
        print("No hay campers inscritos.")




