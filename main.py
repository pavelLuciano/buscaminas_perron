from turtle import pos
import os
from board import Board
from game_handler import Game_Master
import display


def main_game():

    tablero = Board(5, 5, 1)
    for i in tablero.board_matrix:
        for j in i:
            print(j.get_item(), end = " ")
        print("\n")

    my_game = Game_Master(10, 15, 20)
    my_game.run()

    
    #display.show_board(tablero)

        



main_game()



