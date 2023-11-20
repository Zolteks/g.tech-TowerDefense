import pyxel
from player import Player
from intellist import Intellist
from enemy import Enemy

class Game:

    def __init__(self):

        pyxel.init(
            128,
            128,
            fps=30,
            quit_key=pyxel.KEY_ESCAPE,
            capture_sec=30
        )
        
        self.player = Player(self)
        self.enemies = Intellist(20)
        self.bullets = Intellist(5)
        self.enemies.add(Enemy(108, 108, 10, 10))

        pyxel.run(self.update, self.draw)
    
    def update(self):
        self.player.update()
        self.enemies.update()
        self.bullets.update(self)
    
    def draw(self):
        pyxel.cls(0)
        pyxel.rect(pyxel.mouse_x, pyxel.mouse_y, 1, 1, 7)
        self.player.draw()
        self.enemies.draw()
        self.bullets.draw()
        
Game()