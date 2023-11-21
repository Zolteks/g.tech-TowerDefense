import pyxel
import tweening

class Bullet:
    
    def __init__(self, x, y, w, h, d, range=60, damage=1, speed=2):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.speed = speed
        self.speedVect = d
        self.alive = tweening.TimedBool(range/self.speed)
        self.damage = damage
    
    def update(self, game):
        self.x += self.speed * self.speedVect["x"]
        self.y += self.speed * self.speedVect["y"]
        
        if self.alive.elapsed():
            game.bullets.delete(self)
        
        # if self.x + self.w > 200:
        #     game.bullets.delete(self)
        # if self.x < 0:
        #     game.bullets.delete(self)
        # if self.y + self.h > 128:
        #     game.bullets.delete(self)
        # if self.y < 0:
        #     game.bullets.delete(self)
    
    def draw(self):
        pyxel.rectb(self.x, self.y, self.w, self.h, 8)