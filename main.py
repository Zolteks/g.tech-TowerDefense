import pyxel
from player import Player
from intellist import Intellist

class Game:

    def __init__(self):

        pyxel.init(
            128,
            128,
            fps=30,
            quit_key=pyxel.KEY_ESCAPE,
            capture_sec=30
        )
        
        self.player = Player()
        self.ennemiesList = Intellist(20)

        pyxel.run(self.update, self.draw)
    
    def update(self):
        self.player.update()
    
    def draw(self):
        pyxel.cls(0)
        self.player.draw()
        
Game()