dtm= 0

x= float(input("ingrese su tiempo en minutos de recorrido por tramo: "))

while x!= 0 : 
    dtm= dtm+ x
    x= float (input("ingrese otro valor, 0 para salir "))
    
dtm= dtm/60
print ("duracion de su recorrido es: ", dtm,("h") )



