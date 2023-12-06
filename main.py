from turtle import pos
from menu import Menu
import os
from board import Board
from game_handler import Game_Master
import display


def main_game():

    my_menu = Menu()
    ancho, alto, num_bom = my_menu.get_params_from_dificulty()

    my_game = Game_Master(ancho, alto, num_bom)
    my_game.run()

    

    
    #display.show_board(tablero)

        



main_game()



