#dice combinations 

puntaje= int(input("ingrese puntaje: "))
comb=0
for n1 in range(1,7):
    for n2 in range(1,7):
        if n1+n2== puntaje:
            comb+=1
    
print ("hay", comb, "combinaciones para obtener", puntaje)