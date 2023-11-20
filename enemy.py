import pyxel
from gameObject import GameObject

class Enemy(GameObject):
    
    def __init__(self, x, y, w, h, path):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.speed = 2/30
        self.speedVect = {"x": 0, "y": -1}
        self.path = path
    
    def update(self):
        self.x += self.speed * self.speedVect["x"]
        self.y += self.speed * self.speedVect["y"]
        
        print(self.y,  self.path["yLimit"])
        if self.y < self.path["yLimit"]:
            self.speedVect = {"x": 1, "y": 0}
            
        if self.x > self.path["xLimit"]:
            self.speedVect = {"x": 0, "y": 1}
    
    def draw(self):
        # print(self.x, self.y)
        pyxel.rectb(self.x, self.y, self.w, self.h, 8)