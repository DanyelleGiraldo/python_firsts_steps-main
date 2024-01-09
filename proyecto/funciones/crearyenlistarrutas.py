import json
import os

def crear_rutas():
    print("Directorio actual:", os.getcwd())

    try:
        # Cargar la base de datos de campers desde el archivo existente
        with open("rutaentrenamiento.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        print("Error: No se encontró la base de datos.")
        return
    
    print("Lista de rutas: ")
    
    nombreruta = input("Ingrese el nombre de la nueva ruta: ")
    opcionesvalidas = ["Fundamentos de programación", "Programación Web", "Programación formal", "Bases de datos Backend"]
    temaprincipalruta = input(f"Ingrese el tema principal de la ruta {nombreruta}:\n{opcionesvalidas}\n")
    salon = input("Ingrese el salón en el que desea asignar la ruta (sputnik, artemis, apolo): ")
    
    if temaprincipalruta not in opcionesvalidas:
        print("Tema principal no válido.")
        return
    
    temasecundarioruta = input(f"Ingrese el tema secundario de la ruta {nombreruta}:\n{opcionesvalidas}\n")
    
    if temasecundarioruta not in opcionesvalidas:
        print("Tema secundario no válido.")
        return
    elif temasecundarioruta == temaprincipalruta:
        print("¡El tema secundario no puede ser igual al tema principal!")
        return
    
    nuevaruta = {
        "nombreruta": nombreruta,
        "temaprincipalruta": temaprincipalruta,
        "temasecundarioruta": temasecundarioruta,
        "salonuevaruta": salon
    }
    
    try:
        with open("rutaentrenamiento.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {"rutas": []}

    # Agregar la nueva ruta a la base de datos
    data["rutas"].append(nuevaruta)

    # Guardar la base de datos actualizada
    with open("rutas.json", "w") as file:
        json.dump(data, file, indent=2)

    print("La ruta ha sido creada exitosamente.")

crear_rutas()
