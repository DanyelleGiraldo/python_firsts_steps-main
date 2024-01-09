from datetime import datetime

print("ingrese su fecha de nacimiento")
d=int(input("dia: "))
m= int(input("mes: "))
año= int(input ("año: "))
dateFormatter = "%Y-%m-%d"

#el resultado entregado depende del día en que su programa será ejecutado.
#El programa debe tener en cuenta si el cumpleaños ingresado ya pasó durante este año, o si todavía no ocurre.
hoy = datetime.now()
fecha_nacimiento = datetime(hoy.year, m, d)

if hoy >= fecha_nacimiento:
    edad = hoy.year - año
else:
    edad = hoy.year - año - 1

print("Su edad es:", edad)