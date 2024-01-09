def maxalza(nd):
    alza_maxima = 0
    r = 0
    for i in range(nd):
        doltmp = int(input("Valor del dólar del día: "))

        alzatmp = doltmp - r  # Calculate the increase before updating the reference value

        if alzatmp > alza_maxima:
            alza_maxima = alzatmp

        if doltmp > r:
            r = doltmp  # Update the reference value if the current value is greater

    return alza_maxima

nd = int(input("Ingrese el número de días: "))
print("La mayor alza fue:", maxalza(nd))
