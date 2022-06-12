from board import Board
from keyboard import Keyboard
from endScreen import endScreen

class App(Keyboard, Board, endScreen):
    def __init__(self):
        super().__init__()

    def start(self):    
        self.mainloop()



    def restart(self):
        self.new_game()
        self.enable_binding_events()
        self.enable_keyboard()




if __name__ == "__main__":
    app = App()
    app.start()