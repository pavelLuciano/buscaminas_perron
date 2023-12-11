from turtle import pos
from menu import Menu
import os
from board import Board
from game_handler import Game_Master
import pygame


def main_game():


    running = True

    """
        El programa inicia selecionando un usuario con la funcion del menu 'get_user'
        (si el juegador sale el usuario será 'invitado')
        
        la dificultad se selecciona con la funcion run_main_menu()

        el game master crea el juego y lo ejecuta

        finalmente el menu muestra los datos de la db y da la opcion de salir o jugar otra vez
        (eligiendo usuario nuevamente)
    """
    while running:
        my_menu = Menu()
        my_menu.get_user()
        my_menu.run_main_menu()
        ancho, alto, num_bom = my_menu.get_params_from_dificulty()

        my_game = Game_Master(ancho, alto, num_bom)
        victory, tiempo = my_game.run()

        running = my_menu.run_victory_screen(victory, tiempo)


        



    
    #display.show_board(tablero)


main_game()



