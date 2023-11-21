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
        
        # self.player = Turret(self)
        self.enemies = Intellist(50)
        self.bullets = Intellist(100)
        # self.enemies.add(Enemy(108, 108, 10, 10))
        self.enemySpawnCD = tweening.TimedBool(60*2)
        self.turrets = Intellist(10)
        self.spawnEnemy()
        self.turrets.add(player.TurretSpace(self, 5, 5))
        self.turrets.add(player.TurretSpace(self, 200 - 25, 5))

        pyxel.run(self.update, self.draw)
    
    def update(self):
        self.enemies.update(self)
        self.bullets.update(self)
        self.turrets.update()
        self.checkCollisions()
        if self.enemySpawnCD.elapsed():
            self.spawnEnemy()
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
        pyxel.cls(13)
        color = 4
        
        pyxel.rect(0, 0, self.screenW, 30, color)
        pyxel.rect(0, 0, 30, self.screenH, color)
        pyxel.rect(self.screenW-30, 0, 30, self.screenH, color)
        pyxel.rect(60, 60, self.screenW-30*4, self.screenH, color)

        # self.player.draw()
        self.turrets.draw()
        self.enemies.draw()
        self.bullets.draw()
        
        pyxel.rect(pyxel.mouse_x, pyxel.mouse_y, 1, 1, 7)
        
Game()