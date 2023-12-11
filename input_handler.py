from abc import ABC, abstractmethod
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



# Definir una interfaz (clase abstracta)
class Input_Handler(ABC):

    def __init__(self):
        self.input_getter = Input_Receiver()

    #esta funcion está en fase beta y debe ser modficada cuanda añadamos banderas
    def wait_for_click(self):
        coords, button_pressed =  self.input_getter.wait_for_mouse_button_event()
        if button_pressed[0]:
            return self.on_left_click(coords)
        if button_pressed[2]:
            return self.on_right_click(coords)
    
    @abstractmethod
    def on_left_click(self, coords):
        pass

    @abstractmethod
    def on_right_click(self,coords):
        pass
