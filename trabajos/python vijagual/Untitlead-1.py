def suma(digitos):
    l= sum(digitos)
    return l 
datos=[]

x= int(input("cuantos datos va a ingresar: "))

for i in range(x):
    numeros=int(input("ingrese sus datos: "))
    datos.append(numeros)

print("el resultado es: ", suma(datos))