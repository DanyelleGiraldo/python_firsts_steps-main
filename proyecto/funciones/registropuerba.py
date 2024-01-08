import json

def registrar_notas():
    try:
        # Cargar la base de datos de campers desde el archivo existente
        with open("campersInscritos.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        print("Error: No se encontró la base de datos.")
        return

    # Mostrar la lista de campers inscritos
    print("Lista de Campers Inscritos:")
    for camper in data["campers"]:
        if camper["estado"] == "Matriculado":
            print(f"{camper['nombre']} {camper['apellidos']} (ID: {camper['id']})")

    # Solicitar el ID del camper al que se le registrará la nota
    id_camper = input("Ingrese el ID del camper al que desea registrar la nota: ")

    # Buscar el camper en la base de datos
    camper_encontrado = None
    for camper in data["campers"]:
        if camper["id"] == id_camper and camper["estado"] == "Matriculado":
            camper_encontrado = camper
            break

    if camper_encontrado is None:
        print("Camper no encontrado o no está matriculado.")
        return

    # Registrar las notas del camper
    try:
        nota_teorica = float(input("Ingrese la nota teórica del camper: "))
        nota_practica = float(input("Ingrese la nota práctica del camper: "))
    except ValueError:
        print("Error: Las notas deben ser valores numéricos.")
        return

    # Calcular el promedio de las notas
    promedio = (nota_teorica + nota_practica) / 2
    

    # Determinar si el camper aprobó la prueba
    if promedio >= 60:
        print(f"El camper {camper_encontrado['nombre']} {camper_encontrado['apellidos']} ha aprobado la prueba con un promedio de {promedio}.")
        camper_encontrado["estado"] = "Aprobado"
        
    else:
        print(f"El camper {camper_encontrado['nombre']} {camper_encontrado['apellidos']} no ha aprobado la prueba con un promedio de {promedio}.")
        camper_encontrado["estado"] = "No Aprobado"

    # Actualizar la base de datos con las notas y el estado del camper
    with open("campersInscritos.json", "w") as file:
        json.dump(data, file, indent=2)

