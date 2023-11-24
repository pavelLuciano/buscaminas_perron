import pygame as pg
from pygame.locals import *
from board import *
import sys
import display

class Input_Receiver:
    
    
    def get_mouse_event():
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                pos=pg.mouse.get_pos()
                btn=pg.mouse
                return [pos[0],pos[1]] #¿pos es una lista tamaño 2?
        return [-1,-1]

    def wait_for_mouse_button_event(self):
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                if event.type == pg.MOUSEBUTTONDOWN:
                    pos=pg.mouse.get_pos()
                    btn=pg.mouse
                    return [pos[0],pos[1]], btn.get_pressed()
                



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