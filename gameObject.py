import pyxel

class GameObject:
    
    def __init__(self, x, y, w, h, c):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.speed = 1
        self.color = c
    
    def draw(self):
        pyxel.rectb(self.x, self.y, self.w, self.h, self.color)