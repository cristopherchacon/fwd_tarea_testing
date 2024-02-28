def get_computer_choice() -> str:
    """
    Esta function elige aleatoriamente entre piedra, papel o tijera.
    """
    pass


def determine_winner(player_choice: str, computer_choice: str) -> tuple[str, str]:
    """
    Esta function determina el ganador de una partida de piedra, papel o tijera.
    Y devuelve el nombre del ganador y su elección.
    """
    pass


def is_game_over(player_wins: int, computer_wins: int, turns_left: int) -> bool:
    """
    Esta function determina si el juego terminó o no.
    Y devuelve True si el juego terminó, de lo contrario False.
    """
    pass


def show_result(winner_name: str, winner_choice: str) -> None:
    """
    Esta function muestra el resultado de una partida.
    E imprime el nombre del ganador y su elección.
    """
    pass


def play():
    player_wins = 0
    computer_wins = 0
    turns_left = 5
    player_name = input("Ingresa el nombre del jugador: ")
    print(f"Bienvenido, {player_name}! Vamos a jugar Piedra, Papel o Tijera.")

    # Aquí va el resto del código

    if player_wins >= 3:
        print(f"\n¡Felicidades, {player_name}! Has ganado la partida.")
    elif computer_wins >= 3:
        print("\nLa computadora ha ganado la partida. Mejor suerte la próxima vez.")
    else:
        print("\nSe han agotado los turnos. El juego ha terminado en empate.")
