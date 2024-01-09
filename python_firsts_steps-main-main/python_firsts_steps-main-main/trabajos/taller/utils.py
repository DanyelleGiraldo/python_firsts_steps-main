def ingresardatonumero(enunciado):
    
    while (True):
        dato=input(enunciado)
        if dato.isdigit():
            print("entero")
            return int(dato)
            break
        else: 
            print("no es entero")
            
            
def ingresadatocadena(dato):
    while (True):
        cadena= input(dato)
        if cadena.isalpha():
            print("la cadena no tiene numeros")
            return str(cadena)
            break
        else:
            print("la cadena tiene digitos")
            
def ingresardatopositivo(dato):
    while True:
        input_str = input(dato)
        if input_str.isdigit():
            numero = int(input_str)
            if numero > 0:
                print("El número es positivo")
                return numero
            else:
                print("El número no es positivo")
        else:
            print("No ingresó un número entero")
        
def ingresardatonumeroentre(dato):
    while (True):
        numero=int(input(dato))
        if numero >= 0 and numero<= 10:
            print("el numero esta dentro del rango:D")
            return int(numero)
            break
        else:
            print("el numero esta fuera del rango")
            