registros = {}

def registrarciudad():
    ciudad = input("Ingrese el nombre de la ciudad: ")
    n = int(input("Ingrese la cantidad de sismos a registrar: "))
    registros[ciudad] = [None] * n

def registrarsismo():
    ciudad = input("Ingrese el nombre de la ciudad: ")
    if ciudad in registros:
        for i in range(len(registros[ciudad])):
            if registros[ciudad][i] is None:
                try:
                    magnitud = float(input("Ingrese la magnitud del sismo: "))
                    registros[ciudad][i] = magnitud
                    break
                except ValueError:
                    print("Error: Ingrese un número válido.")
    else:
        print("Ciudad no registrada.")

def buscarSismosporCiudad():
    ciudad = input("Ingrese el nombre de la ciudad: ")
    if ciudad in registros:
        print(f"Sismos registrados en la ciudad {ciudad}: {registros[ciudad]}")
    else:
        print("Ciudad no registrada.")

def informederiesgo():
    for ciudad, sismos in registros.items():
        promedio = sum(sismos) / len(sismos)
        print(f"Ciudad: {ciudad}")
        if promedio < 2.5:
            print("Amarillo, sin riesgo")
        elif 2.6 <= promedio <= 4.5:
            print("Naranja, riesgo medio")
        elif promedio > 4.5:
            print("Rojo, riesgo alto")
        print("-" * 30)

while True:
    print("\nMenú:")
    print("1. Registrar Ciudad")
    print("2. Registrar Sismo")
    print("3. Buscar sismos por ciudad")
    print("4. Informe de riesgo")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        registrarciudad()
    elif opcion == "2":
        registrarsismo()
    elif opcion == "3":
        buscarSismosporCiudad()
    elif opcion == "4":
        informederiesgo()
    elif opcion == "5":
        print("Saliendo del programa.")
        break
    else:
        print("Opción no válida.")
