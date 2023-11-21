import pyxel
from gameObject import GameObject

class Enemy(GameObject):
    
    def __init__(self, x, y, w, h, path):
        super().__init__(x, y, w, h, 8)
        self.speed = 8/30
        self.speedVect = {"x": 0, "y": -1}
        self.path = path
        self.life = 10
    
    def update(self, game):
        if self.life < 1:
            game.enemies.delete(self)
        
        self.x += self.speed * self.speedVect["x"]
        self.y += self.speed * self.speedVect["y"]
        
        if self.y < self.path["yLimit"]:
            self.speedVect = {"x": 1, "y": 0}
            
        if self.x > self.path["xLimit"]:
            self.speedVect = {"x": 0, "y": 1}
    
    def draw(self):
        # print(self.x, self.y)
        pyxel.rectb(self.x, self.y, self.w, self.h, self.color)
    
    def takeDamage(self, damage):
        self.life -= damage