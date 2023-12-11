import pygame as pg
from pygame.locals import *
from board import *
import sys

ANCHO_TILE = 32
ALTO_TILE  = 32

zero_tile  = pg.image.load('./assets/0.png')
one_tile   = pg.image.load('./assets/1.png')
two_tile   = pg.image.load('./assets/2.png')
three_tile = pg.image.load('./assets/3.png')
four_tile  = pg.image.load('./assets/4.png')
five_tile  = pg.image.load('./assets/5.png')
six_tile   = pg.image.load('./assets/6.png')
seven_tile = pg.image.load('./assets/7.png')
eight_tile = pg.image.load('./assets/8.png')
bomb_tile  = pg.image.load('./assets/bomb.png')
hide_tile  = pg.image.load('./assets/hide.png')
flag_tile  = pg.image.load('./assets/flag.png')

zero_tile  = pg.transform.scale(zero_tile, (ANCHO_TILE,ALTO_TILE))
one_tile   = pg.transform.scale(one_tile, (ANCHO_TILE,ALTO_TILE))
two_tile   = pg.transform.scale(two_tile, (ANCHO_TILE,ALTO_TILE))
three_tile = pg.transform.scale(three_tile, (ANCHO_TILE,ALTO_TILE))
four_tile  = pg.transform.scale(four_tile, (ANCHO_TILE,ALTO_TILE))
five_tile  = pg.transform.scale(five_tile, (ANCHO_TILE,ALTO_TILE))
six_tile   = pg.transform.scale(six_tile, (ANCHO_TILE,ALTO_TILE))
seven_tile = pg.transform.scale(seven_tile, (ANCHO_TILE,ALTO_TILE))
eight_tile = pg.transform.scale(eight_tile, (ANCHO_TILE,ALTO_TILE))
bomb_tile  = pg.transform.scale(bomb_tile, (ANCHO_TILE,ALTO_TILE))
hide_tile  = pg.transform.scale(hide_tile, (ANCHO_TILE,ALTO_TILE))
flag_tile  = pg.transform.scale(flag_tile, (ANCHO_TILE,ALTO_TILE))

class Displayer:

    def __init__(self, size_x, size_y):
        pg.init()
        pg.display.set_caption("Juego")
        pg.key.set_repeat(500, 50)
        self._window = pg.display.set_mode((ANCHO_TILE * size_x, ALTO_TILE * size_y))

    def fake_matrix(self, size_x, size_y):
        y_tile = 0
        for y in range(size_y):
            x_tile = 0
            for x in range(size_x):
                self._window.blit(hide_tile, (x_tile, y_tile))
                x_tile += ANCHO_TILE
            y_tile += ALTO_TILE
        pg.display.update()

    def show_board(self, matrix):
        self._window.fill("black")
        y = 0  # we start at the top of the screen
        for row in matrix:
            x = 0 # for every row we start at the left of the screen again
            for cell in row:
                if cell.is_hide():
                    if cell.is_flagged():
                        self._window.blit(flag_tile, (x, y))
                    else:
                        self._window.blit(hide_tile, (x, y))

                elif cell.get_item() == CERO:
                    self._window.blit(zero_tile, (x, y))
                    
                elif cell.get_item() == UNO:
                    self._window.blit(one_tile, (x, y))
                    
                elif cell.get_item() == DOS:
                    self._window.blit(two_tile, (x, y))
                    
                elif cell.get_item() == TRES:
                    self._window.blit(three_tile, (x, y))
                    
                elif cell.get_item() == CUATRO:
                    self._window.blit(four_tile, (x, y))
                    
                elif cell.get_item() == CINCO:
                    self._window.blit(five_tile, (x, y))

                elif cell.get_item() == SEIS:
                    self._window.blit(six_tile, (x, y))

                elif cell.get_item() == SIETE:
                    self._window.blit(seven_tile, (x, y))

                elif cell.get_item() == OCHO:
                    self._window.blit(eight_tile, (x, y))

                elif cell.get_item() == BOMB:
                    self._window.blit(bomb_tile, (x, y))

                x += ALTO_TILE# for ever item/number in that row we move one "step" to the right
            y += ANCHO_TILE   # for every new row we move one "step" downwards

        pg.display.update()


