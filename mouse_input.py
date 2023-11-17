import pygame as pg
from pygame.locals import *
from board import *
import sys
import display

def mouse_input_handler(tablero):
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        if event.type == pg.MOUSEBUTTONDOWN:
            pos=pg.mouse.get_pos()
            btn=pg.mouse
            
            x = pos[1]//display.ALTO_TILE
            y = pos[0]//display.ANCHO_TILE
            return [x,y]
    return [-1,-1]