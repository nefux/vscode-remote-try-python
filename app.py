#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------
import random

opciones = ["piedra", "papel", "tijeras"]

#def jugar():
#    jugador = input("Elige una opcion: piedra, papel o tijeras: ").lower()
#    computadora = random.choice(opciones)
#    print(f"\nTu eliges: {jugador}")
#    print(f"La computadora eligio: {computadora}\n")
#
#    if jugador == computadora:
#        print(f"Ambos jugadores eligieron {jugador}. Empate!")
#    elif jugador == "piedra":
#        if computadora == "tijeras":
#            print("La piedra aplasta las tijeras! Ganaste!")
#        else:
#            print("El papel cubre la piedra! Perdiste.")
#    elif jugador == "papel":
#        if computadora == "piedra":
#            print("El papel cubre la piedra! Ganaste!")
#        else:
#            print("Las tijeras cortan el papel! Perdiste.")
#    elif jugador == "tijeras":
#        if computadora == "papel":
#            print("Las tijeras cortan el papel! Ganaste!")
#        else:
#            print("La piedra aplasta las tijeras! Perdiste.")
#
#jugar()


opciones = ["piedra", "papel", "tijeras"]
puntuacion_jugador = 0
puntuacion_oponente = 0

while True:
    eleccion_jugador = input("Elige piedra, papel o tijeras: ").lower()
    if eleccion_jugador not in opciones:
        print("Opción no válida. Inténtalo de nuevo.")
        continue
    eleccion_oponente = random.choice(opciones)
    print("El oponente eligió " + eleccion_oponente)

    if eleccion_jugador == eleccion_oponente:
        print("Es un empate.")
    elif (eleccion_jugador == "piedra" and eleccion_oponente == "tijeras") or \
         (eleccion_jugador == "tijeras" and eleccion_oponente == "papel") or \
         (eleccion_jugador == "papel" and eleccion_oponente == "piedra"):
        print("¡Has ganado!")
        puntuacion_jugador += 1
    else:
        print("Has perdido.")
        puntuacion_oponente += 1

    jugar_de_nuevo = input("¿Quieres jugar de nuevo? (s/n): ").lower()
    if jugar_de_nuevo != "s":
        print("Tu puntuación: ", puntuacion_jugador)
        print("Puntuación del oponente: ", puntuacion_oponente)
        break

