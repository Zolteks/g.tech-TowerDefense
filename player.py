import pyxel
import math
from bullet import Bullet

class Turret:
    
    def __init__(self, game):
        self.game = game
        self.x = 10
        self.y = 10
        self.w = 10
        self.h = 10
        self.speed = 1
        self.fireCooldown = 0
    
    def update(self):
        up = pyxel.btn(pyxel.KEY_UP) or pyxel.btn(pyxel.KEY_Z)
        down = pyxel.btn(pyxel.KEY_DOWN) or pyxel.btn(pyxel.KEY_S)
        left = pyxel.btn(pyxel.KEY_LEFT) or pyxel.btn(pyxel.KEY_Q)
        right = pyxel.btn(pyxel.KEY_RIGHT) or pyxel.btn(pyxel.KEY_D)
        
        if pyxel.btn(pyxel.MOUSE_BUTTON_LEFT) and self.fireCooldown < pyxel.frame_count:
            self.fireCooldown = pyxel.frame_count + 10
            self.shoot()
        
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
    
    def shoot(self):
        directionX = pyxel.mouse_x - self.x
        directionY = pyxel.mouse_y - self.y
        norme = math.sqrt(directionX**2 + directionY**2)
        direction = {"x": directionX/norme, "y": directionY/norme}
        self.game.bullets.add(Bullet(self.x, self.y, 2, 2, direction, True))
        