import pyxel
from gameObject import GameObject

class Enemy(GameObject):
    
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.speed = 2/30
        self.speedVect = {"x": -1, "y": -1}
    
    def update(self):
        self.x += self.speed * self.speedVect["x"]
        self.y += self.speed * self.speedVect["y"]
    
    def draw(self):
        pyxel.rectb(self.x, self.y, self.w, self.h, 8)