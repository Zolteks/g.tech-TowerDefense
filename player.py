import pyxel
import math
from gameObject import GameObject
from bullet import Bullet

class TurretSpace(GameObject):

    def __init__(self, game, x, y):
        super().__init__(x, y, 20, 20, 7)
        self.game = game
        self.turret = None
    
    def draw(self):
        if self.turret:
            self.turret.draw()
        else:
            pyxel.rectb(self.x, self.y, self.w, self.h, self.color)
            pyxel.line(self.x, self.y, self.x + self.w-1, self.y + self.h-1, self.color)
            pyxel.line(self.x + self.w-1, self.y, self.x, self.y + self.h-1, self.color)
    
    def placeTurret(self, turretType="classic"):
        if turretType == "classic":
            self.turret = Turret(self.game, self.x, self.y, self.w, self.h)
    
    def update(self):
        if pyxel.btn(pyxel.MOUSE_BUTTON_RIGHT):
            mouseX = pyxel.mouse_x
            mouseY = pyxel.mouse_y
            if mouseX > self.x and mouseX < self.x+self.w and mouseY > self.y and mouseY < self.y+self.h:
                self.placeTurret()
        if self.turret:
            self.turret.update()

class Turret(GameObject):
    
    def __init__(self, game, x, y, w, h):
        super().__init__(x, y, w, h, 10)
        self.game = game
        self.fireCooldown = 0
        self.range = 80
        self.target = None
    
    def update(self):
        for i in range(self.game.enemies.size):
            cur = self.game.enemies.array[i]
            if not cur:
                continue
            distanceToEnemy = math.sqrt((cur.x+cur.w/2)**2+(cur.y+cur.w/2)**2)
            print(distanceToEnemy)
            if distanceToEnemy < self.range:
                self.target = cur
    
    def draw(self):
        pyxel.rect(self.x, self.y, self.w, self.h, self.color)
        pyxel.circb(self.x + self.w/2, self.y + self.h/2, self.range, self.color)
        if self.target:
            pyxel.line(self.x + self.w, self.y + self.h, self.target.x, self.target.y, self.color)
    
    def shoot(self):
        directionX = pyxel.mouse_x - self.x
        directionY = pyxel.mouse_y - self.y
        norme = math.sqrt(directionX**2 + directionY**2)
        direction = {"x": directionX/norme, "y": directionY/norme}
        self.game.bullets.add(Bullet(self.x, self.y, 2, 2, direction, True))
