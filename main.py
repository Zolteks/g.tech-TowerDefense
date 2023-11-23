import pyxel
import player
import random
import math
from intellist import Intellist
from enemy import *
import tweening

class Game:

    def __init__(self):
        
        self.screenW = 200
        self.screenH = 128

        pyxel.init(
            self.screenW,
            self.screenH,
            fps=60,
            quit_key=pyxel.KEY_ESCAPE,
            capture_sec=30
        )
        
        self.state = "menu"
        self.building = False
        self.life = 20
        self.gold = 100
        self.scenarium = 0
        self.enemySpawnCD = tweening.TimedBool(60*2)
        self.enemies = Intellist(50)
        self.bullets = Intellist(100)
        self.turrets = Intellist(10)
        for i in range(7):
            self.turrets.add(player.TurretSpace(self, 15 + 25*i, 5))

        pyxel.run(self.update, self.draw)
    
    def update(self):
        if self.state == "menu":
            self.updateMenu()
        elif self.state == "level":
            self.updateLevel()
        
    def updateMenu(self):
        mouseX, mouseY = pyxel.mouse_x, pyxel.mouse_y
        
        if pyxel.btn(pyxel.MOUSE_BUTTON_LEFT) and mouseX > 30 and mouseX < 30+41 and mouseY > 30 and mouseY < 30+11:
            self.state = "level"
            self.initLevel()

        if pyxel.btn(pyxel.MOUSE_BUTTON_LEFT) and mouseX > 30 and mouseX < 30+37 and mouseY > 45 and mouseY < 45+11:
            pyxel.quit()        
        
        pyxel.rect(30, 30, 41, 7, 11)
        pyxel.text(31, 31, "Start Game", 0)
        pyxel.rect(30, 45, 37, 7, 11)
        pyxel.text(31, 46, "Quit Game", 0)
    
    def updateLevel(self):
        if self.life < 1:
            self.state = "menu"
        self.enemies.update(self)
        self.bullets.update(self)
        self.turrets.update(self)
        self.checkCollisions()
        if self.enemySpawnCD.elapsed():
            self.spawnEnemy()
            self.enemySpawnCD.reset()
    
    def initLevel(self):
        self.enemySpawnCD.reset()
        self.building = False
        self.life = 20
        self.gold = 100000
        self.scenarium = 0
        self.enemySpawnCD = tweening.TimedBool(60*2)
        self.enemies = Intellist(50)
        self.bullets = Intellist(100)
        self.turrets = Intellist(10)
        for i in range(7):
            self.turrets.add(player.TurretSpace(self, 15 + 25*i, 5))
    
    def rect_overlap(self, bullet, enemy):
        return bullet.x < enemy.x + enemy.w and bullet.x + bullet.w > enemy.x and bullet.y < enemy.y + enemy.h and bullet.y + bullet.h > enemy.y

    def circ_overlap(self, bullet, enemy):
        enemyCenterX = enemy.x + enemy.w
        enemyCenterY = enemy.y + enemy.h
        distToEnemy = math.sqrt((enemyCenterX-bullet.x)**2 + (enemyCenterY-bullet.y)**2)
        return distToEnemy < bullet.radius.value()

    
    def checkCollisions(self):
        for j in range(self.enemies.size):
            if not self.enemies.array[j]:
                continue
            curE = self.enemies.array[j]
            for i in range(self.bullets.size):
                if not self.bullets.array[i]:
                    continue
                curB = self.bullets.array[i]
                if curB.type!="tesla" and self.rect_overlap(curB, curE):
                    curE.takeDamage(curB.damage)
                    self.bullets.delete(curB)
                elif self.circ_overlap(curB, curE):
                    curE.takeDamage(curB.damage)
                    self.bullets.delete(curB)
    
    def spawnEnemy(self):
        # enemyType = [normalEnemy,mediumEnemy,bigEnemy]
        # enemyRandomSpawn = random.choice(enemyType)
        enemyW = 10
        enemyH = 10
        spawnX = 30 + enemyW
        spawnY = self.screenH
        rand = random.randint(1, 100)
        if rand <= 50:
            enemyToSpawn = normalEnemy(spawnX, spawnY, enemyW, enemyH, {"xLimit": self.screenW - 40 -10, "yLimit": 40} )
        elif rand <= 95:
            enemyToSpawn = mediumEnemy(spawnX, spawnY, enemyW, enemyH, {"xLimit": self.screenW - 40 -10, "yLimit": 40} )
        elif rand <= 100:
            enemyToSpawn = bigEnemy(spawnX, spawnY, enemyW, enemyH, {"xLimit": self.screenW - 40 -10, "yLimit": 40} )
        self.enemies.add(enemyToSpawn)
    
    def draw(self):
        if self.state == "menu":
            self.drawMenu()
        elif self.state == "level":
            self.drawLevel()
        
        pyxel.rect(pyxel.mouse_x, pyxel.mouse_y, 1, 1, 7)
        
    def drawMenu(self):
        pyxel.cls(0)
        pyxel.rect(30, 30, 41, 7, 11)
        pyxel.text(31, 31, "Start Game", 0)
        pyxel.rect(30, 45, 37, 7, 11)
        pyxel.text(31, 46, "Quit Game", 0)
    
    def drawLevel(self):
        pyxel.cls(13)
        
        color = 4
        
        pyxel.rect(0, 0, self.screenW, 30, color)
        pyxel.rect(0, 0, 30, self.screenH, color)
        pyxel.rect(self.screenW-30, 0, 30, self.screenH, color)
        pyxel.rect(self.screenW-60, self.screenH-10, 30, 10, 11)
        pyxel.rect(60, 60, self.screenW-30*4, self.screenH, color)

        pyxel.text(65, self.screenH-10, f"life: {self.life}", 7)
        pyxel.text(65, self.screenH-20, f"gold: {self.gold}", 7)
        # self.player.draw()
        self.enemies.draw()
        self.bullets.draw()
        self.turrets.draw()
        
Game()