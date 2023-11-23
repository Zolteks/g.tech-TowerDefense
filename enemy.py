import pyxel
from gameObject import GameObject

class Enemy(GameObject):
    
    def __init__(self, x, y, w, h, path, c):
        super().__init__(x, y, w, h, c)
        self.speed = 16/60
        self.speedVect = {"x": 0, "y": -1}
        self.path = path
        self.life = 10
        self.goldValue = 10
        self.scenariumValue = 1
        self.damage = 0
        self.passed = False
    
    def update(self, game):
        if self.life < 1:
            game.gold += self.goldValue
            game.enemies.delete(self)
        
        self.x += self.speed * self.speedVect["x"]
        self.y += self.speed * self.speedVect["y"]
        
        if not self.passed and game.screenW-60+30 > self.x and game.screenW-60 < self.x+self.w and game.screenH > self.y and game.screenH-10 < self.y+self.h:
            game.life -= self.damage
            self.passed = True

        if self.y < self.path["yLimit"]:
            self.speedVect = {"x": 1, "y": 0}
            
        if self.x > self.path["xLimit"]:
            self.speedVect = {"x": 0, "y": 1}
    
    def draw(self):
        # print(self.x, self.y)
        pyxel.rectb(self.x, self.y, self.w, self.h, self.color)
    
    def takeDamage(self, damage):
        self.life -= damage

class normalEnemy(Enemy):

    def __init__(self, x, y, w, h, path):
        super().__init__(x, y, w, h, path, 10)
        self.speed = 30/60
        self.speedVect = {"x": 0, "y": -1}
        self.path = path
        self.life = 10
        self.goldValue = 10
        self.scenariumValue = 0
        self.damage = 1
class mediumEnemy(Enemy):
    
    def __init__(self, x, y, w, h, path):
        super().__init__(x, y, w, h, path, 5)
        self.speed = 16/60
        self.speedVect = {"x": 0, "y": -1}
        self.path = path
        self.life = 30
        self.goldValue = 25
        self.scenariumValue = 5
        self.damage = 2
class bigEnemy(Enemy):
    
    def __init__(self, x, y, w, h, path):
        super().__init__(x, y, w, h, path, 11)
        self.speed = 8/60
        self.speedVect = {"x": 0, "y": -1}
        self.path = path
        self.life = 150
        self.goldValue = 100
        self.scenariumValue = 25
        self.damage = 10