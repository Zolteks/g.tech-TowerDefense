import pyxel
from gameObject import GameObject

class Enemy(GameObject):
    
    def __init__(self, x, y, w, h, path, c):
        super().__init__(x, y, w, h, c)
        self.speed = 8/30
        self.speedVect = {"x": 0, "y": -1}
        self.path = path
        self.life = 10
        self.goldValue = 10
        self.scenariumValue = 0
    
    def update(self, game):
        if self.life < 1:
            game.gold += self.goldValue
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

class normalEnemy(Enemy):

    def __init__(self, x, y, w, h, path):
        super().__init__(x, y, w, h, path, 10)
        self.speed = 8/30
        self.speedVect = {"x": 0, "y": -1}
        self.path = path
        self.life = 10
        self.goldValue = 10
        self.scenariumValue = 0
class mediumEnemy(Enemy):
    
    def __init__(self, x, y, w, h, path):
        super().__init__(x, y, w, h, path, 5)
        self.speed = 8/30
        self.speedVect = {"x": 0, "y": -1}
        self.path = path
        self.life = 10
        self.goldValue = 25
        self.scenariumValue = 5
class bigEnemy(Enemy):
    
    def __init__(self, x, y, w, h, path):
        super().__init__(x, y, w, h, path, 11)
        self.speed = 8/30
        self.speedVect = {"x": 0, "y": -1}
        self.path = path
        self.life = 10
        self.goldValue = 100
        self.scenariumValue = 25