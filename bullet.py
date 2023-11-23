import pyxel
import tweening

class Bullet:
    
    def __init__(self, x, y, w, h, d, bulletType, range):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.speedVect = d
        self.type = ""
        if bulletType == "classic":
            self.speed = 2
            self.damage = 1
            self.alive = tweening.TimedBool(range/self.speed)
            self.type = "classic"
            self.color = 8
        if bulletType == "sniper":
            self.speed = 10
            self.damage = 10
            self.alive = tweening.TimedBool(range/self.speed)
            self.type = "sniper"
            self.color = 7
        if bulletType == "tesla":
            self.speed = 1
            self.damage = 1
            self.alive = tweening.TimedBool(range/self.speed)
            self.color = 3
    
    def update(self, game):
        self.x += self.speed * self.speedVect["x"]
        self.y += self.speed * self.speedVect["y"]
        
        if self.alive.elapsed():
            game.bullets.delete(self)
    
    def draw(self):
        pyxel.rectb(self.x, self.y, self.w, self.h, self.color)