def totalnum(numeros):
    largo= len(numeros)
    return largo

def numpares(numeros):
    contadorpares=0
    for num in numeros:
        if num % 2 == 0:
            contadorpares+=1
    return contadorpares
def numimpares(numeros):
    contadorimpares=0
    for num in numeros:
        if num % 2 != 0:
            contadorimpares+=1
    return contadorimpares
def menores10 (numeros):
    contadormenor=0
    for num in numeros:
        if num < 10: 
            contadormenor+=1
    return contadormenor
def entre2050 (numeros):
    contadorentre=0
    for num in numeros:
        if  num >= 20 and num <=50:
            contadorentre+=1
    return contadorentre
def mayorque (numeros):
    contador100= 0
    for num in numeros:
        if num > 100:
            contador100+=1
    return contador100

datos=[]

x= int(input("cuantos datos va a ingresar?: "))

for i in range(x):
    numeros= int(input("ingrese sus numeros: "))
    datos.append(numeros)
    
print(totalnum(datos))
print(numpares(datos))
print(numimpares(datos))
print(menores10(datos))
print(entre2050(datos))
print(mayorque(datos))