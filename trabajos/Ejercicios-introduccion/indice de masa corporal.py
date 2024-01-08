edad= int(input("ingrese su edad: "))
peso= int(input("ingrese su peso expresado en kilogramos: "))
altura= float(input("ingrese su altura expresada en metros: "))

imc= peso/altura**2

if imc<22.0 and edad <45 :
    print("su indice de masa corporal es bajo")
elif imc < 22.0 and edad >= 45 : 
    print("su indice de masa corporal es medio")
elif imc >= 22.0 and edad < 45: 
    print("su indice de masa corporal es medio")
elif imc >= 22.0 and edad >= 45: 
    print("su indice de masa corporal es alto")