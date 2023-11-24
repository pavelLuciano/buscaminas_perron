from abc import ABC, abstractmethod
from input_receiver import Input_Receiver

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
