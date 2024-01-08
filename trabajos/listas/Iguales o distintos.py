def todos_iguales(lista):
    return all(elemento == lista[0] for elemento in lista)

listass = []

l = int(input("¿Cuántos datos va a ingresar?: "))

for i in range(l):
    x = int(input("Ingrese sus datos: "))
    listass.append(x)

resultado = todos_iguales(listass)

if resultado:
    print("Todos los elementos son iguales.", listass)
else:
    print("No todos los elementos son iguales.", listass)
