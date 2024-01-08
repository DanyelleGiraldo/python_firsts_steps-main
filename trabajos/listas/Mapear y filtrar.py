def mapear(f, valores):
    return [f(x) for x in valores]

def cuadrado(x):
    return x ** 2

contador=int(input("cuantos datos va a ingresar?: "))
datos=[]
for i in range(contador):
    l=int(input("ingrese datos: "))
    dato= datos.append(l)


resultado = mapear(cuadrado, datos)
print(resultado)
