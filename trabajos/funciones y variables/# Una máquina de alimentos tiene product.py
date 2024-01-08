# Una máquina de alimentos tiene productos de tres tipos, ***A, B y C,*** 
# que valen respectivamente $**270**, $**340** y $**390**. 
# La máquina acepta y da de vuelto monedas de $**10**, $**50** y $**100**.
# Escriba un programa que pida al usuario elegir el producto y luego le pida ingresar las monedas hasta alcanzar 
# el monto a pagar. Si el monto ingresado es mayor que el precio del producto, 
# el programa debe entregar las monedas de vuelto, una por una.
            
def solicitar_producto():
    return input("Seleccione su producto: \n A: $270 \n B: $340 \n C: $390\n").upper()

def procesar_pago(producto, precio):
    print(f"Ha seleccionado el producto {producto}.")
    monedas = 0
    while monedas < precio:
        dinero = int(input(f"Ingrese su dinero\nEl producto vale ${precio}:\nRecibimos monedas de\n10$\n50$\n100$\n"))
        monedas += dinero

    if monedas > precio:
        print("Su cambio es:", monedas - precio)

ingrese_alimento = solicitar_producto()

if ingrese_alimento == "A":
    procesar_pago("A", 270)
elif ingrese_alimento == "B":
    procesar_pago("B", 340)
elif ingrese_alimento == "C":
    procesar_pago("C", 390)
else:
    print("Opción no válida. Por favor, seleccione A, B o C.")
