
import json

# Obtener información del candidato
def inscribir_candidato():
    try:
        # Cargar la base de datos de campers desde el archivo existente
        with open("campersInscritos.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        print("Error: No se encontró la base de datos.")
        return

    print("Lista de Campers a asignar ruta:")
    
    camper_encontrado = None

    for camper in data["campers"]:
        if camper["estado"] == "Aprobado":
            print(f"{camper['nombre']} {camper['apellidos']} (ID: {camper['id']})")

    id_camper = input("Ingrese el ID del camper al que desea registrar la ruta: ")
    
    for camper in data["campers"]:
        if camper["id"] == id_camper and camper["estado"] == "Aprobado":
            camper_encontrado = camper
            break

    if camper_encontrado is None:
        print("Camper no encontrado o no está matriculado.")
        return

    # Verificar si la ruta seleccionada es válida
    rutas_validas = ["nodejs", "java", "netcore"]
    ruta_elegida = input("Seleccione la ruta de entrenamiento (nodejs, java, netcore): ")

    if ruta_elegida not in rutas_validas:
        print("Ruta no válida. Por favor, seleccione entre NodeJS, Java o NetCore.")
        return

    # Agregar la ruta al diccionario del camper encontrado
    camper_encontrado["ruta_elegida"] = ruta_elegida

    # Guardar la base de datos actualizada
    with open("campersInscritos.json", "w") as file:
        json.dump(data, file, indent=2)

    print(f"Ruta {ruta_elegida} asignada al camper {camper_encontrado['nombre']} {camper_encontrado['apellidos']} (ID: {camper_encontrado['id']}).")

# Ejecutar el programa
inscribir_candidato()
