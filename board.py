import random as rm

ERROR = -1
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

    def set_flag(self):
        self._flag = not self._flag

    def set_num(self, numero):
        if (self._item == BOMB):
            return False
        else:
            self._item = numero
            return True

    def get_item(self):
        return self._item

    def is_hide(self):
        return self._hide
    
    def is_flagged(self):
        return self._flag

    def add_num(self):
        if self._item > SIETE:
            return False
        else:
            self._item += 1
            return True

    def unhide_cell(self):
        self._hide = False



class Board:
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

    def place_bomb(self, coords):
        x,y = coords
        self.board_matrix[y][x].set_item(BOMB)
        for i in [-1, 0,1]:
            for j in [-1,0,1]:
                if self.coords_are_in_matrix(x+j, y+i):
                    self.board_matrix[y+i][x+j].add_num()

    def create_matriz(self):
        self.board_matrix = [[Cell( CERO ) for _ in range (self._size_x)] for _ in range (self._size_y)]
        for coords in self._list_bombs:
            self.place_bomb(coords)
    
    def get_size(self):
        return [self._size_x, self._size_y]

    def unhide(self, x_coord, y_coord):
        if not self.coords_are_in_matrix(x_coord, y_coord):
            return ERROR
        if self.board_matrix[y_coord][x_coord].is_hide():
            self.board_matrix[y_coord][x_coord].unhide_cell()
            if self.board_matrix[y_coord][x_coord].get_item() != CERO:
                return self.board_matrix[y_coord][x_coord].get_item()
            else:
                self.unhide(x_coord, y_coord-1)
                self.unhide(x_coord, y_coord+1)
                self.unhide(x_coord+1, y_coord)
                self.unhide(x_coord-1, y_coord)
                return CERO
        return ERROR
    
    def put_flag(self, x_coord, y_coord):
        self.board_matrix[y_coord][x_coord].set_flag()

    
    def coords_are_in_matrix(self, x_coord, y_coord):
        return (x_coord >= 0 and y_coord >= 0 and x_coord < self._size_x and y_coord < self._size_y)
    
    def is_clean(self):
        acum = 0
        for line in self.board_matrix:
            for cell in line:
                if cell.is_flagged():
                    if cell.get_item() != BOMB:
                        return False
                    else:
                        acum = acum + 1
        
        return acum == len(self._list_bombs)                
        

            
                

            

