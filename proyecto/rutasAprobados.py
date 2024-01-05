import json

# Obtener información del candidato
def inscribir_candidato():
    nombre = input("Ingrese el nombre del candidato: ")
    apellido = input("Ingrese el apellido del candidato: ")
    ruta_elegida = input("Seleccione la ruta de entrenamiento (NodeJS, Java, NetCore): ")

    # Verificar si la ruta seleccionada es válida
    rutas_validas = ["NodeJS", "Java", "NetCore"]
    if ruta_elegida not in rutas_validas:
        print("Ruta no válida. Por favor, seleccione entre NodeJS, Java o NetCore.")
        return

    # Realizar prueba inicial
    resultado_prueba = input("¿El candidato ha superado la prueba inicial? (Si/No): ")
    if resultado_prueba.lower() != "si":
        print("El candidato no cumple con los requisitos para la ruta seleccionada.")
        return

    # Crear diccionario con la información del candidato
    candidato = {
        "nombre": nombre,
        "apellido": apellido,
        "ruta_elegida": ruta_elegida
    }

    # Cargar la base de datos existente (si existe)
    try:
        with open("base_de_datos_rutas.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {"candidatos": []}

    # Agregar el nuevo candidato a la base de datos
    data["candidatos"].append(candidato)

    # Guardar la base de datos actualizada
    with open("base_de_datos_rutas.json", "w") as file:
        json.dump(data, file, indent=2)

    print(f"Candidato inscrito en la ruta {ruta_elegida} exitosamente.")

# Ejecutar el programa
inscribir_candidato()