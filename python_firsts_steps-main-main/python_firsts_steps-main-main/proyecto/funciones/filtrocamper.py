import json


class Camper:
    def __init__(self, nombre, nota_teorica, nota_practica):
        self.nombre = nombre
        self.nota_teorica = nota_teorica
        self.nota_practica = nota_practica


def cargarbasenotas():
    try:
        with open("notas.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {"notas": []}
    return data


def cargarbasecampers():
    try:
        with open("campersInscritos.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {"campers": []}
    return data


def guardarbasecampers(datacampers):
    with open("campersInscritos.json", "w") as file:
        json.dump(datacampers, file, indent=2)


def evaluar_camper(camper_id, nota_teorica, nota_practica, nota_trabajo):
    datacampers = cargarbasecampers()
    datanotas = cargarbasenotas()

    print("Lista de Campers Inscritos:")
    for camper in datacampers["campers"]:
        if camper.get("ruta_elegida", ""):  # Check if "ruta_elegida" is not empty
            print(f"{camper['nombre']} {camper['apellidos']} (ID: {camper['id']})")

    for camper in datacampers["campers"]:
        if camper["id"] == camper_id:
            promedio = ((0.3 *nota_teorica) + (0.6 *nota_practica) + (0.1 * nota_trabajo))  / 2
            print(f"Promedio de {camper['nombre']}: {promedio:.2f}")

            if promedio >= 60:
                print(f"{camper['nombre']} ha aprobado.")
                camper["filtro"] = "aprobado"
            else:
                print(f"{camper['nombre']} ha reprobado.")
                camper["filtro"] = "reprobado"
                if promedio < 60:
                    print(f"{camper['nombre']} está en riesgo. ¡Atención necesaria!")
                    camper["estadomatricula"] = "Enriesgo"

            # Update the notas data
            datanotas["notas"].append({
                "id": camper_id,
                "nombre_ruta": camper.get("ruta_elegida", ""),
                "nota_practica": nota_practica,
                "nota_teorica": nota_teorica,
                "nombre_camper": camper['nombre']
            })

            guardarbasecampers(datacampers)
            with open("notas.json", "w") as file:
                json.dump(datanotas, file, indent=2)

            return

    print(f"Camper con ID {camper_id} no encontrado.")

def enlistar_campers_en_riesgo():
    datacampers = cargarbasecampers()

    print("Lista de Campers en Riesgo:")
    for camper in datacampers["campers"]:
        if camper.get("estadomatricula", "") == "Enriesgo":
            print(f"{camper['nombre']} {camper['apellidos']} (ID: {camper['id']})")

def main():
    # Ejemplo de uso
    camper_id = input("Ingrese la ID del camper: ")
    nota_teorica = float(input("Ingrese la nota teórica del camper: "))
    nota_practica = float(input("Ingrese la nota práctica del camper: "))
    nota_trabajo= float(input("ingrese nota del trabajo: "))
    evaluar_camper(camper_id, nota_teorica, nota_practica, nota_trabajo)

    main()
