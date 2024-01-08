import math

def desviacion_estandar(listanumreales):
    promedio = sum(listanumreales) / len(listanumreales)
    cuadrados = [(valor - promedio) ** 2 for valor in listanumreales]
    todosvalores = sum(cuadrados)
    step4 = todosvalores / len(listanumreales)
    step5 = step4 ** 0.5
    return step5

listasx = []
largo = int(input("¿Cuántos datos va a ingresar?: "))

for i in range(largo):
    datosuser = float(input("Ingrese el número real: "))
    listasx.append(datosuser)

resultado = desviacion_estandar(listasx)

print("Lista de números:", listasx)
print("Desviación estándar:", resultado)
