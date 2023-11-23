import pyxel
from bullet import Bullet
import tweening

class ShockWave(Bullet):

    def __init__(self, x, y, w, h, d, range):
        super().__init__(x, y, w, h, d, "tesla", range)
        self.radius = tweening.TimedValue(range, f="easeOutCubic")
        self.type = "tesla"
    
    def update(self, game):
        if self.alive.elapsed():
            game.bullets.delete(self)
    
    def draw(self):
        pyxel.circb(self.x, self.y, self.radius.value(), self.color)