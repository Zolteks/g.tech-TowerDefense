import pyxel

class Bullet:
    
    def __init__(self, x, y, w, h, d, friendly=False):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.speed = 1
        self.speedVect = d
        self.friendly = friendly
    
    def update(self, game):
        self.x += self.speed * self.speedVect["x"]
        self.y += self.speed * self.speedVect["y"]
        
        if self.x + self.w > 128:
            game.bullets.delete(self)
        if self.x < 0:
            game.bullets.delete(self)
        if self.y + self.h > 128:
            game.bullets.delete(self)
        if self.y < 0:
            game.bullets.delete(self)
    
    def draw(self):
        pyxel.rectb(self.x, self.y, self.w, self.h, 8)