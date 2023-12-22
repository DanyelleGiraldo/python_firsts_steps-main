#Escriba un programa que pida al usuario que ingrese varios valores enteros, que pueden ser positivos o negativos. 
# Cuando se ingrese un cero, el programa debe terminar y mostrar un gráfico de cuántos valores positivos y negativos 
# fueron ingresados:
#Ingrese varios valores, termine con cero:
lista=[] 
positivos=0
negativos=0
while True: 
      
    V1= int(input("Ingrese varios valores, termine con cero: "))
    lista.append(V1) 
    if V1== 0: 
        break
    if V1 >0 :
        positivos+=1
    if V1 < 0:
        negativos+=1

print("positivos: ", ("*")*positivos)
print("negativos: ", ("*")*negativos)

