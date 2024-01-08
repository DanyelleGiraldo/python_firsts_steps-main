total_suma=0
suma=0 
tabla=0
total=0 

while True:
    suma+=1
    total_suma=1/(2**suma)
    total+=total_suma
    if tabla==0:
        print("potencia   fraccion   suma")
        tabla=1
    print(suma,"        ",total_suma,"       ",total)
    
    if total_suma <= 0.000001:
        break






