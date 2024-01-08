def obtener_digito_verificador(rol_sin_dv):
    rol_invertido = int(str(rol_sin_dv)[::-1])

    secuencia = [2, 3, 4, 5, 6, 7]
    suma = 0
    
    for i, digito in enumerate(str(rol_invertido)):
        multiplicador = secuencia[i % len(secuencia)]
        suma += int(digito) * multiplicador

    digito_verificador = 11 - (suma % 11)
    digito_verificador = digito_verificador if digito_verificador != 11 else 0

    return digito_verificador

rol_sin_dv = int(input("Ingrese su número: "))
digito_verificador_calculado = obtener_digito_verificador(rol_sin_dv)
print(f"El dígito verificador calculado es: {digito_verificador_calculado}")