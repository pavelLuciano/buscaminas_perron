from turtle import pos
from menu import Menu
import os
from board import Board
from game_handler import Game_Master
import pygame


def main_game():


    running = True

    
    while running:
        my_menu = Menu()
        my_menu.get_user()
        my_menu.run_main_menu()
        ancho, alto, num_bom = my_menu.get_params_from_dificulty()

        my_game = Game_Master(ancho, alto, num_bom)
        victory = my_game.run()

        running = my_menu.run_victory_screen(victory)


        



    
    #display.show_board(tablero)


main_game()



