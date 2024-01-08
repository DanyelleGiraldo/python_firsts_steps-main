# ⚙ Desarrolle un programa que tenga la siguiente entrada:
# - primero, el usuario ingresa un número entero *n*, que indica cuántas palabras ingresará a continuación;
# - después el usuario ingresa *n* palabras.
# La salida del programa debe mostrar la palabra más larga y la más corta que fueron ingresadas por el usuario.
lista= []
x= int(input("cuantos numeros va a ingresar?: "))
long= 0
cort=0
palabra_larga= ""
palabra_corta=""
for i in range(x):
     p= str(input("ingrese la palabra: "))
     lista.append(p)
     if len(p) > long:
          long= p
     if len(p) < cort:
       cort=p    
print (lista)
print(cort)
print(long)