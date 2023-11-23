import pyxel
import player
from intellist import Intellist
from enemy import Enemy
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
        
        if pyxel.btn(pyxel.MOUSE_BUTTON_LEFT) and mouseX > 30 and mouseX < 30+50 and mouseY > 30 and mouseY < 30+10:
            self.state = "level"
            self.initLevel()
    
    def updateLevel(self):
        if self.life < 1:
            pyxel.quit()
        self.enemies.update(self)
        self.bullets.update(self)
        self.turrets.update()
        self.checkCollisions()
        if self.enemySpawnCD.elapsed():
            self.spawnEnemy()
            self.enemySpawnCD.reset()
    
    def initLevel(self):
        self.enemySpawnCD.reset()
    
    def rect_overlap(self, bullet, enemy):
        return bullet.x < enemy.x + enemy.w and bullet.x + bullet.w > enemy.x and bullet.y < enemy.y + enemy.h and bullet.y + bullet.h > enemy.y
    
    def checkCollisions(self):
        for i in range(self.bullets.size):
            if not self.bullets.array[i]:
                continue
            curB = self.bullets.array[i]
            for j in range(self.enemies.size):
                if not self.enemies.array[j]:
                    continue
                curE = self.enemies.array[j]
                if self.rect_overlap(curB, curE):
                    curE.takeDamage(curB.damage)
                    self.bullets.delete(curB)
    
    def spawnEnemy(self):
        enemyW = 10
        enemyH = 10
        spawnX = 30 + enemyW
        spawnY = self.screenH
        self.enemies.add(Enemy(spawnX, spawnY, enemyW, enemyH, {"xLimit": self.screenW - 40 -10, "yLimit": 40} ))
    
    def draw(self):
        if self.state == "menu":
            self.drawMenu()
        elif self.state == "level":
            self.drawLevel()
        
        pyxel.rect(pyxel.mouse_x, pyxel.mouse_y, 1, 1, 7)
        
    def drawMenu(self):
        pyxel.cls(0)
        pyxel.rect(30, 30, 50, 10, 11)
        pyxel.text(31, 31, "Start Game", 0)
    
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