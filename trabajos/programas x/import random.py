import random

def inicializar_palabra_oculta(palabra):
    """Inicializa la palabra oculta con guiones bajos."""
    return ['_' for _ in palabra]

def mostrar_ahorcado(intentos_maximos, intentos_restantes):
    """Muestra el estado actual del ahorcado."""
    partes_ahorcado = ["pierna derecha", "pierna izquierda", "brazo derecho", "brazo izquierdo", "tronco", "cabeza"]
    partes_mostradas = partes_ahorcado[:intentos_maximos - intentos_restantes]
    print("Ahorcado:", partes_mostradas)

def mostrar_palabra_oculta(palabra_oculta):
    """Muestra la palabra oculta actualizada."""
    print("Palabra:", " ".join(palabra_oculta))

def letra_en_palabra(letra, palabra):
    """Verifica si la letra está en la palabra."""
    return letra in palabra

def actualizar_palabra_oculta(letra, palabra, palabra_oculta):
    """Actualiza la palabra oculta con la letra ingresada."""
    for i in range(len(palabra)):
        if palabra[i] == letra:
            palabra_oculta[i] = letra

def no_ha_ganado(palabra_oculta, palabra):
    """Verifica si se ha ganado el juego."""
    return "".join(palabra_oculta) != palabra

def jugar_ahorcado():
    # Lista de palabras para el juego (puedes agregar más palabras si lo deseas)
    palabras = ["PYTHON", "PROGRAMACION", "DEVELOPER", "COMPUTADORA", "ALGORITMO", "AHORCADO"]

    # Seleccionar una palabra al azar
    palabra = random.choice(palabras).upper()
    
    # Inicializar variables
    palabra_oculta = inicializar_palabra_oculta(palabra)
    intentos_maximos = 6
    intentos_restantes = intentos_maximos

    print("Bienvenido al juego del Ahorcado")

    while intentos_restantes > 0 and no_ha_ganado(palabra_oculta, palabra):
        # Mostrar estado actual del juego
        mostrar_ahorcado(intentos_maximos, intentos_restantes)
        mostrar_palabra_oculta(palabra_oculta)

        # Obtener letra del jugador
        letra_ingresada = input("Ingresa una letra: ").upper()

        # Verificar si la letra está en la palabra
        if letra_en_palabra(letra_ingresada, palabra):
            print("¡Correcto!")
            actualizar_palabra_oculta(letra_ingresada, palabra, palabra_oculta)
        else:
            print("Incorrecto. Pierdes una vida.")
            intentos_restantes -= 1

    # Mostrar resultado final
    if not no_ha_ganado(palabra_oculta, palabra):
        mostrar_ahorcado(intentos_maximos, 0)  # Mostrar ahorcado completo
        print(f"Lo siento, has perdido. La palabra era {palabra}")
    else:
        mostrar_palabra_oculta(palabra_oculta)
        print("¡Felicidades! Has ganado.")

if __name__ == "__main__":
    jugar_ahorcado()
