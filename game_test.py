from unittest.mock import patch

from game import get_computer_choice, determine_winner, is_game_over, show_result, play


def test_get_computer_choice():
    choice = get_computer_choice()
    assert choice in ["piedra", "papel", "tijera"]


def test_determine_winner():
    assert determine_winner("piedra", "tijera") == ("jugador", "piedra")
    assert determine_winner("piedra", "papel") == ("computadora", "papel")
    assert determine_winner("papel", "papel") == ("empate", "papel")


def test_is_game_over():
    assert not is_game_over(2, 1, 3)
    assert is_game_over(3, 1, 3)
    assert is_game_over(2, 3, 0)


def test_show_result(capsys):
    show_result("jugador", "papel")
    captured = capsys.readouterr()
    assert "El ganador es jugador con papel." in captured.out

    show_result("computadora", "tijera")
    captured = capsys.readouterr()
    assert "El ganador es computadora con tijera." in captured.out

    show_result("empate", "papel")
    captured = capsys.readouterr()
    assert "Ambos jugadores eligieron papel. Es un empate." in captured.out


@patch('builtins.input', side_effect=["Juan", "papel", "piedra", "tijera"])
@patch('random.choice', side_effect=["piedra", "tijera", "papel"])
def test_player_is_best_of_three(mock_input, mock_random, capsys):
    play()
    captured = capsys.readouterr()
    assert "Bienvenido, Juan! Vamos a jugar Piedra, Papel o Tijera." in captured.out
    assert "Turnos restantes: 5." in captured.out
    assert "El ganador es Juan con papel." in captured.out
    assert "Turnos restantes: 4." in captured.out
    assert "El ganador es Juan con piedra." in captured.out
    assert "Turnos restantes: 3." in captured.out
    assert "El ganador es Juan con tijera." in captured.out
    assert "¡Felicidades, Juan! Has ganado la partida." in captured.out


@patch('builtins.input', side_effect=["Juan", "papel", "papel", "papel", "papel", "papel"])
@patch('random.choice', side_effect=["papel", "papel", "papel", "papel", "papel"])
def test_player_and_computer_draw(mock_input, mock_random, capsys):
    play()
    captured = capsys.readouterr()
    assert captured.out.count("Ambos jugadores eligieron papel. Es un empate.") == 5
    assert "Se han agotado los turnos. El juego ha terminado en empate." in captured.out
