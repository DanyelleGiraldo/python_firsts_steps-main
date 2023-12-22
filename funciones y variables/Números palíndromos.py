def invertir_digitos(n):
    
    num_invertido=int(str(n)[::-1])
    return num_invertido

n= int(input("ingrese su numero para verificar si es palindromo: "))

num_invertidos= invertir_digitos(n)

if num_invertidos == n:
    print(n, "es palindromo")
else:
    print(n,"no es palindromo")

