# Crea el juego de piedra, papel o tijeras con las siguientes condiciones:
# - la piedra le gana a las tijeras, la tijera le gana al papel y el papel le gana a la piedra.
# - El juego debe ser para dos jugadores donde un jugador es el usuario y el otro es la computadora.
# - El juego debe ejecutarse por consola y al abrirse le debe preguntar al jugador si elige piedra, papel o tijeras. En caso de que el jugador elija una opción inválida, el juego debe mostrar un mensaje de error y debe volver a preguntarle al jugador qué elige. Las opciones el jugador las debe ingresar en minúsculas.
# - La computadora debe elegir su opción de forma aleatoria.
# - Al final se debe mostrar en consola el resultado, es decir, si el jugador ganó, perdió o fue un empate.
# - El juego debe llevar el número de veces que jugó el jugador, cuántas veces ganó, cuántas veces perdió y cuántas veces empató.
# - El juego debe preguntar al jugador si desea volver a jugar. En caso de que el jugador elija que sí, el juego debe volver a ejecutarse. En caso de que el jugador elija que no, el juego debe mostrar la puntuación final y el número de veces que jugó el jugador.

import random

def game():

    player = 0
    computer = 0
    draw = 0
    times = 0

    while True:
        times += 1
        print(f'Game {times}')
        print('Choose: rock, paper or scissors')
        player_choice = input().lower()
        computer_choice = random.choice(['rock', 'paper', 'scissors'])

        if player_choice == 'rock' or player_choice == 'paper' or player_choice == 'scissors':
            print(f'Computer choice: {computer_choice}')
            if player_choice == computer_choice:
                print('Draw')
                draw += 1
            elif player_choice == 'rock' and computer_choice == 'scissors':
                print('Player wins')
                player += 1
            elif player_choice == 'scissors' and computer_choice == 'paper':
                print('Player wins')
                player += 1
            elif player_choice == 'paper' and computer_choice == 'rock':
                print('Player wins')
                player += 1
            else:
                print('Computer wins')
                computer += 1
        else:
            print('Invalid option')
            continue

        print(f'Player: {player} - Computer: {computer} - Draw: {draw}')
        print('Do you want to play again? (yes/no)')
        play_again = input().lower()
        if play_again == 'no':
            print(f'Player: {player} - Computer: {computer} - Draw: {draw}')
            print(f'You played {times} times')
            break

game()