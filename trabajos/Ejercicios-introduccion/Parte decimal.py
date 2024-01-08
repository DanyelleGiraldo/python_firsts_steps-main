import math

dec= float(input("ingrese su numero real: "))
if dec<0 :
    dec= math.modf(dec*-1.)
else :
    dec= math.modf(dec) 


print("la parte decimal es ", dec)