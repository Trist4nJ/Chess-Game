from board import *
from pieces import *

class Game:
    def __init__(self):
        self.turn = 'white'
        self.game_started = False
        self.launch_game()

    def launch_game(self):
        self.game_started = True
        piece = input()