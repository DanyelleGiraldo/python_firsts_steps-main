# def maxalza(x,nd,alza):
#     alza_maxima=0
#     for i in range(nd):
#         r=0
#         doltmp= int(input("valor del dolar dia:"))
        
#         if doltmp >= r or doltmp<= r :
#             r=doltmp
#         alzatmp=x-r
#         if alzatmp>alza_maxima:
#             alza_maxima=alzatmp
#     return alza_maxima
# nd= int(input("ingrese el numero de dias: "))
# print("la mayor alza fue: ", maxalza(nd))

def maxalza(nd):
    alza_maxima = 0
    r = 0
    for i in range(nd):
        
        doltmp = int(input("Valor del dólar del día: "))

        if doltmp >= r or doltmp <= r:
            r = doltmp

        alzatmp = doltmp - r

        if alzatmp > alza_maxima:
            alza_maxima = alzatmp

    return alza_maxima

nd = int(input("Ingrese el número de días: "))
print("La mayor alza fue:", maxalza(nd))