from turtle import pos
import os
from board import Board
import game_handler
import display


def main_game():

    tablero = Board(15, 25, 40)
    for i in tablero.board_matrix:
        for j in i:
            print(j.get_item(), end = " ")
        print("\n")
    
    display.show_board(tablero)

        



main_game()



