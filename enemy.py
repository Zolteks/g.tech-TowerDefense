import pyxel
from player import Ressources
from gameObject import GameObject

class normalEnemy(GameObject):
    
    def __init__(self, x, y, w, h, path):
        super().__init__(x, y, w, h, 10)
        self.speed = 8/30
        self.speedVect = {"x": 0, "y": -1}
        self.path = path
        self.life = 10
        self.goldValue = 10
        self.scenariumValue = 0
    
    def update(self, game):
        if self.life < 1:
            game.ressources.intGold += self.goldValue
            game.ressources.intScenarium += self.scenariumValue
            print(game.ressources.intGold)
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
        
class mediumEnemy(GameObject):
    
    def __init__(self, x, y, w, h, path):
        super().__init__(x, y, w, h, 8)
        self.speed = 8/30
        self.speedVect = {"x": 0, "y": -1}
        self.path = path
        self.life = 10
        self.goldValue = 25
        self.scenariumValue = 5
    
    def update(self, game):
        if self.life < 1:
            game.ressources.intGold += self.goldValue
            game.ressources.intScenarium += self.scenariumValue
            print(game.ressources.intGold)
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
        
class bigEnemy(GameObject):
    
    def __init__(self, x, y, w, h, path):
        super().__init__(x, y, w, h, 3)
        self.speed = 8/30
        self.speedVect = {"x": 0, "y": -1}
        self.path = path
        self.life = 10
        self.goldValue = 100
        self.scenariumValue = 25
    
    def update(self, game):
        if self.life < 1:
            game.ressources.intGold += self.goldValue
            game.ressources.intScenarium += self.scenariumValue
            print(game.ressources.intGold)
            game.enemies.delete(self)
        
        self.x += self.speed * self.speedVect["x"]
        self.y += self.speed * self.speedVect["y"]
        
        if not self.passed and game.screenW-60+30 > self.x and game.screenW-60 < self.x+self.w and game.screenH > self.y and game.screenH-10 < self.y+self.h:
            game.life -= 2
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