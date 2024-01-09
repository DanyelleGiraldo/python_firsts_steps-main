import json

def contar_aprobados_perdidos(ruta, entrenador):
    try:
        with open("matriculas.json", "r") as file:
            matriculas = json.load(file)
    except FileNotFoundError:
        print("Error: No se encontró la base de datos.")
        return None

    aprobados = 0
    perdidos = 0

    for matricula in matriculas:
        if matricula["ruta"] == ruta and matricula["entrenador"] == entrenador:
            if matricula["aprobado"]:
                aprobados += 1
            else:
                perdidos += 1

    return aprobados, perdidos

import json

def listar_campers_entrenador_por_ruta(ruta):
    try:
        with open("matriculas.json", "r") as file:
            matriculas = json.load(file)
    except FileNotFoundError:
        print("Error: No se encontró la base de datos.")
        return None

    campers_entrenadores = []

    for matricula in matriculas:
        if matricula["ruta"] == ruta:
            camper_entrenador = {
                "camper": matricula["camper"],
                "entrenador": matricula["entrenador"]
            }
            campers_entrenadores.append(camper_entrenador)

    return campers_entrenadores