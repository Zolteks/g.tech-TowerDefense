import pyxel

class Player:
    
    def __init__(self):
        self.x = 10
        self.y = 10
        self.w = 10
        self.h = 10
        self.speed = 1
    
    def update(self):
        up = pyxel.btn(pyxel.KEY_UP) or pyxel.btn(pyxel.KEY_Z)
        down = pyxel.btn(pyxel.KEY_DOWN) or pyxel.btn(pyxel.KEY_S)
        left = pyxel.btn(pyxel.KEY_LEFT) or pyxel.btn(pyxel.KEY_Q)
        right = pyxel.btn(pyxel.KEY_RIGHT) or pyxel.btn(pyxel.KEY_D)
        
        if up:
            self.y -= self.speed
        if down:
            self.y += self.speed
        if left:
            self.x -= self.speed
        if right:
            self.x += self.speed
    
    def draw(self):
        pyxel.rectb(self.x, self.y, self.w, self.h, 10)