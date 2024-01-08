def genpi(n) :
    sum=0 
    signo=1
    
    for i in range(n):
        term=1/(2*i+1)
        sum=sum+signo*term
        signo*=-1
        
    estmPi= 4*sum
    return estmPi
n=int(input("ingrese el termino a estimar: "))

print(genpi(n))