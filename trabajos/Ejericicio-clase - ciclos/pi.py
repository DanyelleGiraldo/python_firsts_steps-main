def espi(n):
    suma=0
    signo= 1
    
    for i in range(n) :
        termino = 1/(2*i+1)
        suma=suma+ signo* termino
        signo*=-1        
    estimacion_pi=4*suma
    return estimacion_pi

n= int(input("ingrese el numero del termino para estimar pi "))

print(espi(n))