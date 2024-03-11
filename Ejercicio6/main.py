import random

def jugar():
    opciones = ["piedra", "papel", "tijera"]

    print("Elige: piedra, papel o tijera")
    jugador = input().lower()

    # Validar la elección del jugador
    if jugador not in opciones:
        print("Elección no válida. Elige entre piedra, papel o tijera.")
        return

    computadora = random.choice(opciones)

    print("Jugador elige:", jugador)
    print("Computadora elige:", computadora)

    if jugador == computadora:
        print("¡Empate!")
    elif (jugador == "piedra" and computadora == "tijera") or \
         (jugador == "papel" and computadora == "piedra") or \
         (jugador == "tijera" and computadora == "papel"):
        print("¡Ganaste!")
    else:
        print("¡Perdiste!")

jugar()
