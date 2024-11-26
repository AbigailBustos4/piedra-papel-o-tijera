import random

def obtener_eleccion_computadora():
    return random.choice(["piedra", "papel", "tijera"])

def determinar_ganador(usuario, computadora):
    if usuario == computadora:
        return "empate"
    elif (usuario == "piedra" and computadora == "tijera") or \
         (usuario == "tijera" and computadora == "papel") or \
         (usuario == "papel" and computadora == "piedra"):
        return "usuario"  
    else:
        # Este caso nunca debería ocurrir con entradas validadas.
        return "computadora"

def mejor_de_tres():
    print("¡Juguemos a piedra, papel o tijera! 🎮")
    rondas_usuario = 0
    rondas_compu = 0

    for ronda in range(3):
        print(f"\n--- Nueva Ronda {ronda + 1} ---")
        usuario = input("Elige: piedra, papel o tijera: ").lower()

        # Validación de entrada
        if usuario not in ["piedra", "papel", "tijera"]:
            print("Entrada inválida. Por favor, elige piedra, papel o tijera.")
            continue

        computadora = obtener_eleccion_computadora()
        print(f"Tu elección fue: {usuario}")
        print(f"Elección de la computadora: {computadora}")

        # Determinación del ganador
        resultado = determinar_ganador(usuario, computadora)
        if resultado == "usuario":
            print("¡Ganaste esta ronda! 🎉")
            rondas_usuario += 1
        elif resultado == "computadora":
            print("La computadora ganó esta ronda. 🤖")
            rondas_compu += 1
        elif resultado == "empate":
            print("¡Es un empate! 😐")

        # Mostrar puntuación
        print(f"Puntuación: Tú {rondas_usuario} - {rondas_compu} Computadora")
        if rondas_compu == 2 or rondas_usuario == 2:
            break

    # Resultado final del mejor de 3
    if rondas_usuario > rondas_compu:
        print("\n🎉 ¡Felicidades! Ganaste el mejor de 3. 🎉")
    elif rondas_compu > rondas_usuario:
        print("\n😢 La computadora ganó el mejor de 3. Mejor suerte la próxima vez.")
    else:
        print("\n🙌 ¡Es un empate en el mejor de 3! 🙌")
       
    # Preguntar si quiere volver a jugar
    volver_a_jugar = input("\n¿Quieres jugar otra vez? (sí/no): ").lower()
    if volver_a_jugar in ["sí", "si", "s"]:
        mejor_de_tres()
    else:
        print("\nGracias por jugar. ¡Hasta pronto! 👋")

# Iniciar el juego
mejor_de_tres()
