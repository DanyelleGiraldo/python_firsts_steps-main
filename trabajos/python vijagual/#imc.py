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

datos = []

for i in range(2):
    x = float(input("Ingrese su peso y luego su altura: "))
    datos.append(x)

peso, altura = datos
indice = imc(peso, altura)
estado = obesidad(indice)
print(estado)
