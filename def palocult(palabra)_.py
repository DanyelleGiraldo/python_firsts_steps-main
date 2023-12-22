def palocult(palabra):
    return ["_" for _ in palabra]

def mostahor(intmax, intrest):
    partes = ["pierna derecha", "pierna izquierda", "brazo derecho", "brazo izquierdo", "torso", "cabeza"]
    mostpart = partes[:intmax - intrest]
    print("ahorcado", mostpart)

def palocult1(palabraoc):
    print("palabra: ", "".join(palabraoc))

def letra_en_pal(letra, palabra):
    return letra in palabra

def actpaloct(letra, palabra, palocult):
    for i in range(len(palabra)):
        if palabra[i] == letra:
            palocult[i] = letra

def equivocado(palocult, palabra):
    return "".join(palocult) != palabra

def jugaho():
    palabra = input("Ingresa la palabra para el juego del Ahorcado: ").upper()
    palabra_oculta = palocult(palabra)
    intentos_maximos = 6
    intentos_restantes = intentos_maximos
    print("Bienvenido al juego del Ahorcado")

    while intentos_restantes > 0 and equivocado(palabra_oculta, palabra):
        mostahor(intentos_maximos, intentos_restantes)
        palocult1(palabra_oculta)
        letra_ingresada = input("Ingresa una letra: ").upper()

        if letra_en_pal(letra_ingresada, palabra):
            print("¡Correcto!")
            actpaloct(letra_ingresada, palabra, palabra_oculta)
        else:
            print("Incorrecto. Pierdes una vida.")
            intentos_restantes -= 1

    if equivocado(palabra_oculta, palabra):  # Corregido: Se invierte la condición
        mostahor(intentos_maximos, 0)
        print(f"Lo siento, has perdido. La palabra era {palabra}")
    else:
        palocult1(palabra_oculta)
        print("¡Felicidades! Has ganado.")

if __name__ == "__main__":
    jugaho()
