from board import Board
import board 
import display
import pygame as pg
from display import Displayer
from input_handler import Input_Handler

class Game_Master(Input_Handler):
    def __init__(self, size_x, size_y, n_bombs):
        super().__init__()
        self.game_over = None
        self._n_bombs = n_bombs
        self._size_x = size_x
        self._size_y = size_y
        self._displayer = Displayer(size_x, size_y)

    def run(self):
        
        
        self._displayer.fake_matrix(self._size_x, self._size_y)
        coords, _ = self.input_getter.wait_for_mouse_button_event()
        tile_coords = [coords[0]//display.ANCHO_TILE, coords[1]//display.ALTO_TILE]
        print("este esta prohibido: ", tile_coords)
        self._game_board = Board(self._size_x, self._size_y, self._n_bombs, forbidden = tile_coords)
        self.on_left_click(coords)

        self._playing = True
        self._displayer.show_board(self._game_board.board_matrix)
        while self._playing:
            tile_coords = self.wait_for_click()
            self._displayer.show_board(self._game_board.board_matrix)

        self.input_getter.wait_for_mouse_button_event()
        return self.game_over



    def on_left_click(self,coords):
        x = coords[0]//display.ANCHO_TILE
        y = coords[1]//display.ALTO_TILE
        if (self._game_board.unhide(x,y) == board.BOMB):
            self.lose()


    def on_right_click(self, coords):
        x = coords[0]//display.ANCHO_TILE
        y = coords[1]//display.ALTO_TILE
        self._game_board.put_flag(x,y)
        if self._game_board.is_clean():
            self.win()
        
        

    def lose(self):
        for x,y in self._game_board._list_bombs:
            self._game_board.unhide(x,y)
        self._playing = False
        self.game_over = False

    def win(self):
        print("Victoria")
        self._playing = False
        self.game_over = True

        

        

