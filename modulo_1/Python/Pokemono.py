def elegir_pokemon_inicial():
    #Permite al jugador elegir su Pokémon inicial.
    print("\n¡Bienvenido al mundo Pokémon! Tu aventura comienza ahora.")
    print("El Entrenador del gimnasio pulgarcita te ofrece tres Pokémon para empezar:")
    print("1. Bulbasaur (Tipo Planta)")
    print("2. Charmander (Tipo Fuego)")
    print("3. Squirtle (Tipo Agua)")

    while True:
        seleccion = input("Elige a tu compañero Pokémon: ")
        if seleccion == '1':
            return "Bulbasaur"
        elif seleccion == '2':
            return "Charmander"
        elif seleccion == '3':
            return "Squirtle"
        else:
            print("¡Opción inválida! Por favor, elige 1, 2 o 3.")

def realizar_pregunta(ronda):
    #Genera una pregunta aleatoria para cada ronda.
    import random
    preguntas_disponibles = [
        {"pregunta": "¿Cual es la región más grande en el universo Pokémon?", "respuesta": "Galar"},
        {"pregunta": "¿Cual es el pokémon legendario más poderoso?", "respuesta": "Arceus"},
        {"pregunta": "¿Quién es el protagonistya de la serie de TV?", "respuesta": "Ash Ketchum"},
        {"pregunta": "¿Que tipo de pokémon es Pikachu?", "respuesta": "Tipo Electrico"},
        {"pregunta": "¿Cual es el nombre del Pokémon de tipo Fuego que aparece en una de las cartas del base set de JCC pokémon", "respuesta": "Charizard"},
        {"pregunta": "¿Que ataque especial tiene charizard en la carta del Base set?", "respuesta": "Giro Fuego"},
        {"pregunta": "¿Cuál es el día después del lunes?", "respuesta": "martes"}
    ]

    pregunta_elegida = random.choice(preguntas_disponibles)
    return pregunta_elegida['pregunta'], pregunta_elegida['respuesta']

def main_sencillo():
    nombre_jugador = input("¡Hola, futuro entrenador! ¿Cuál es tu nombre?: ")
    print(f"¡Genial, {nombre_jugador}!")

    pokemon_inicial = elegir_pokemon_inicial()
    print(f"\n¡Excelente elección! Tu primer Pokémon es {pokemon_inicial}. ¡Empieza tu aventura!")

    ronda = 1
    puntos = 0

    while True:
        print(f"\nRonda {ronda} ")
        print(f"Tu Pokémon {pokemon_inicial} te acompaña en esta etapa.")
        print("Para avanzar, responde la siguiente pregunta:")

        pregunta, respuesta_correcta = realizar_pregunta(ronda)
        print(pregunta)
        respuesta_jugador = input("Tu respuesta: ").strip().lower() # .strip() quita espacios extra

        if respuesta_jugador == respuesta_correcta.lower():
            print("¡Correcto! Has avanzado con tu Pokémon. ¡Sigue así!")
            puntos += 10
            ronda += 1
        else:
            print(f"Incorrecto. La respuesta correcta era '{respuesta_correcta}'.")
            print("Tu Pokémon necesita más entrenamiento en esta área. ¡Inténtalo de nuevo!")
            # Puedes optar por reiniciar la ronda o perder el juego si quieres un desafío
            # Por ahora, simplemente no suma puntos y permite seguir intentando.

        decision = input("\n¿Quieres continuar tu aventura? (si/no): ").lower()
        if decision != 'si' and decision != 'si':
            print(f"\n¡Aventura terminada! Lograste {puntos} puntos.")
            print("¡Gracias por jugar! ¡Vuelve pronto para más desafíos con tus Pokémon!")
            break

if __name__ == "__main__":
    main_sencillo()
