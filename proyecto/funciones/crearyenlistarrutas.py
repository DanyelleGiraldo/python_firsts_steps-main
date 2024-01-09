import json
import os

def crear_rutas():
    
    try:
        print("Directorio actual:", os.getcwd())

        # Cargar la base de datos de campers desde el archivo existente
        with open("rutas.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        print("Error: No se encontró la base de datos.")
        return
    
    print("lista de rutas: ")
    
    nombreruta= input("ingrese el nombre de la nueva ruta: ")
    opcionesvalidas=["Fundamentos de programación", "Programación Web", "Programación formal", "Bases de datos Backend"]
    temaprincipalruta= input(f"ingrese el tema principal de la ruta {nombreruta}: \n {opcionesvalidas} ")
    salon= input("ingrese el salon en el que desea asignar la ruta \n sputnik \n artemis \n apolo ")
    profesor= input("ingrese el profesor de esta ruta: ")
    if temasecundarioruta != temaprincipalruta:
        temasecundarioruta= input(f"ingre el tema secundario de la ruta {nombreruta}: \n {opcionesvalidas}")
    else: 
        print("ese tema ya esta seleccionado!")
        
    nuevaruta= {
        "nombreruta": nombreruta,
        "temaprincipalruta": temaprincipalruta,
        "temasecundarioruta": temasecundarioruta,
        "salonuevaruta": salon,
        "profesornuevaruta": profesor
    }
    
    try:
        with open("rutas.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {"rutas": []}

    # Agregar el nuevo camper a la base de datos
    data["rutas"].append(nuevaruta)

    # Guardar la base de datos actualizada
    with open("rutas.json", "w") as file:
        json.dump(data, file, indent=2)

    print("la ruta ha sido creada exitosamente.")
    
