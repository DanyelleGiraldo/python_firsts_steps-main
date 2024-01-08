def imc(peso, altura):
    return peso / altura**2

def obesidad(imc):
    estados = {
        (float('-inf'), 18.5): "Bajo peso",
        (18.5, 25): "Normal",
        (25, 30): "Sobrepeso",
        (30, 35): "Obesidad I",
        (35, 40): "Obesidad II",
        (40, float('inf')): "Obesidad III"
    }

    for rango, estado in estados.items():
        if rango[0] <= imc < rango[1]:
            return estado

estudiantes = []

numero_estudiantes = int(input("¿Cuántos estudiantes son?: "))

for _ in range(numero_estudiantes):
    peso = float(input(f"Ingrese el peso del estudiante {_ + 1} en kg: "))
    altura = float(input(f"Ingrese la altura del estudiante {_ + 1} en metros: "))
    
    indice = imc(peso, altura)
    estado = obesidad(indice)
    
    estudiantes.append((peso, altura, indice, estado))

# Mostrar información de los estudiantes
for i, estudiante in enumerate(estudiantes, start=1):
    print(f"\nEstudiante {i}:")
    print(f"Peso: {estudiante[0]} kg")
    print(f"Altura: {estudiante[1]} m")
    print(f"IMC: {estudiante[2]:.2f}")
    print(f"Estado de obesidad: {estudiante[3]}")
