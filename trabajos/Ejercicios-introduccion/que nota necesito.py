cm1= float(input("ingrese nota del certamen 1: "))
cm2= float(input("ingrese nota del certamen 2: "))
lab= float(input("ingrese nota del laboratorio: "))

ncm= float((lab*0.3))
ntc= float((60-ncm)/0.7)

enc= float((cm1+cm2)/3)
ntf= float((ntc-enc)*3)
cm3=ntf

print ("Necesita nota ", round(ntf, 2), " en el certamen 3")
