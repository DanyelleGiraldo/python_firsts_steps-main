def promedio (promediar):
    return sum(promediar)/len(promediar)    
l=0
datos= []
contadordato=0

x= int(input("cuantos datos va a ingresar?: "))


for i in range(x):
    contadordato= contadordato+1
    h = int(input(f"Ingrese dato {contadordato}: "))
    datos.append(h)
    
    promedio_datos= promedio(datos)

mayores = [dato for dato in datos if dato > promedio_datos]
cantidad = sum(1 for dato in datos if dato > promedio_datos)

print (f"{cantidad} datos son mayores que el promedio")
print (f"los datos mayores que el promedio son: {mayores}")