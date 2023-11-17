import random as rm

CERO = 0
UNO = 1
DOS = 2
TRES = 3
CUATRO = 4
CINCO = 5
SEIS = 6
SIETE = 7
OCHO = 8
BOMB = 9

class Cell:

    def __init__(self, item):
        self._hide = True
        self._flag = False
        self._item = item #almacena un numero o una bomba

    def set_item(self, item):
        self._item = item

    def set_num(self, numero):
        if (self._item == BOMBA):
            return False
        else:
            self._item = numero
            return True

    def get_item(self):
        return self._item

    def is_hide(self):
        return self._hide

    def add_num(self):
        if self._item > SIETE:
            return False
        else:
            self._item += 1
            return True

    def unhide(self):
        self._hide = False



class Board:

    def place_bomb(self, coords):
        x,y = coords
        self.board_matrix[x][y].set_item(BOMB)
        for i in [-1, 0,1]:
            for j in [-1,0,1]:
                if x+i >= 0 and x+i < self._size_x and y+j >= 0 and y+j < self._size_y :
                    self.board_matrix[x+i][y+j].add_num()

    def create_matriz(self):
        self.board_matrix = [[Cell( CERO ) for _ in range (self._size_y)] for _ in range (self._size_x)]
        for coords in self._list_bombs:
            self.place_bomb(coords)

    def __init__(self, size_x, size_y, num_bombs, forbidden = [-1,0]):
        self._size_x = size_x
        self._size_y = size_y
        self._list_bombs = []
        self.board_matrix = []
        while len(self._list_bombs) < num_bombs:
            x = rm.randint(0,size_x-1)
            y = rm.randint(0,size_y-1)
            #Faltan condiciones mas especificas (crear funciones aparte)
            if [x,y] not in self._list_bombs and [x,y] != forbidden:
                self._list_bombs.append([x,y])
        print(self._list_bombs)
        self.create_matriz()
    
    def left_click_on(self,coords):
        x,y = coords
        if x < 0 :
            return False
        else:
            self.board_matrix[x][y].unhide()
            return True
    
    def get_size(self):
        return [self._size_x, self._size_y]