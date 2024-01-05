def enfrentamientos(tenistas):
    ganadores = []
    for i in range(0, len(tenistas), 2):
        jugador1 = tenistas[i]
        jugador2 = tenistas[i + 1]
        resultado = input(f"Ronda {len(ganadores) + 1}\n{jugador1} vs {jugador2}: ").lower()
        if resultado == "a":
            ganadores.append(jugador1)
        elif resultado == "b":
            ganadores.append(jugador2)
    return ganadores

tenistas = []
contador = 0
for i in range(8):
    contador += 1
    x = input(f"Ingrese nombres del tenista {contador}: ")
    tenistas.append(x)

while len(tenistas) > 1:
    tenistas = enfrentamientos(tenistas)

print(f"\n¡El campeón del torneo es {tenistas[0]}!")
