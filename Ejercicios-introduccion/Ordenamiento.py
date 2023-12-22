lista_numeros = []

x = int(input("Ingrese cuántos números quiere ordenar: "))

for i in range(x):
    numero = int(input("Ingrese un número: "))
    lista_numeros.append(numero)

lista_numeros.sort()
print(lista_numeros)
     