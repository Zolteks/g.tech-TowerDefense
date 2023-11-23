import pyxel
import math
import tweening
from shockWave import ShockWave
from gameObject import GameObject
from bullet import Bullet

class TurretSpace(GameObject):

    def __init__(self, game, x, y):
        super().__init__(x, y, 20, 20, 7)
        self.game = game
        self.turret = None
        self.gatlingPrice = 50
        self.sniperPrice = 100
        self.teslaPrice = 200
        self.gatlingPriceScenarium = 25
        self.sniperPriceScenarium = 75
        self.teslaPriceScenarium = 150
        self.message = ""
        self.messageCooldown = tweening.TimedBool(60*3)
    
    def draw(self):
        originX = 35
        originY = 35
        t1X = originX + 10
        t1Y = originY + 10
        t2X = t1X + 40
        t2Y = t1Y
        t3X = t2X + 40
        t3Y = originY + 10
        if self.turret:
            self.turret.draw()
        else:
            pyxel.rectb(self.x, self.y, self.w, self.h, self.color)
            pyxel.line(self.x, self.y, self.x + self.w-1, self.y + self.h-1, self.color)
            pyxel.line(self.x + self.w-1, self.y, self.x, self.y + self.h-1, self.color)
        
        if self.game.building:
            pyxel.rect(originX, originY, self.game.screenW - originX*2, self.game.screenH/2, 0)
            pyxel.rectb(originX, originY, self.game.screenW - originX*2, self.game.screenH/2, 10)

            # button 1
            pyxel.rect(t1X, t1Y, 30, 30, 10)
            pyxel.text(t1X, t1Y + 35, str(self.gatlingPrice), 7)

            # button 2
            pyxel.rect(t2X, t2Y, 30, 30, 5)
            pyxel.text(t2X, t2Y + 35, str(self.sniperPrice), 7)
            
            # button 3
            pyxel.rect(t3X, t3Y, 30, 30, 11)
            pyxel.text(t3X, t3Y + 35, str(self.teslaPrice), 7)
            pyxel.text(t2X-len(self.message), t2Y + 45, str(self.message), 7)
            
        elif self.game.upgrade:
            pyxel.rect(originX, originY, self.game.screenW - originX*2, self.game.screenH/2, 0)
            pyxel.rectb(originX, originY, self.game.screenW - originX*2, self.game.screenH/2, 10)

            # button 1
            pyxel.rect(t1X, t1Y, 30, 30, 10)
            pyxel.text(t1X, t1Y + 35, str(self.gatlingPriceScenarium), 7)

            # button 2
            pyxel.rect(t2X, t2Y, 30, 30, 5)
            pyxel.text(t2X, t2Y + 35, str(self.sniperPriceScenarium), 7)
            
            # button 3
            pyxel.rect(t3X, t3Y, 30, 30, 11)
            pyxel.text(t3X, t3Y + 40, str(self.teslaPriceScenarium), 7)
            pyxel.text(t2X-len(self.message), t2Y + 35, str(self.message), 7)
    
    def placeTurret(self, turretType="classic"):
        if turretType == "classic":
            self.game.gold -= self.gatlingPrice
            self.turret = Turret(self.game, self.x, self.y, self.w, self.h)
        if turretType == "sniper":
            self.game.gold -= self.sniperPrice
            self.turret = Sniper(self.game, self.x, self.y, self.w, self.h)
        if turretType == "tesla":
            self.game.gold -= self.teslaPrice
            self.turret = Tesla(self.game, self.x, self.y, self.w, self.h)
    
    def update(self, game):
        mouseX = pyxel.mouse_x
        mouseY = pyxel.mouse_y
        if pyxel.btn(pyxel.MOUSE_BUTTON_LEFT) and not self.game.building:
            if mouseX > self.x and mouseX < self.x+self.w and mouseY > self.y and mouseY < self.y+self.h:
                self.game.building = self
                # self.placeTurret("classic")
        elif pyxel.btn(pyxel.MOUSE_BUTTON_RIGHT) and not self.game.building:
            if mouseX > self.x and mouseX < self.x+self.w and mouseY > self.y and mouseY < self.y+self.h:
                self.game.upgrade = self
        elif pyxel.btn(pyxel.KEY_Q):
            self.game.building = False
            self.game.upgrade = False
            self.message = ""
        if self.turret:
            self.turret.update()
        if self.game.building:
            originX = 35
            originY = 35
            size = 30
            t1X = originX + 10
            t1Y = originY + 10
            t2X = t1X + 40
            t2Y = t1Y
            t3X = t2X + 40
            t3Y = originY + 10
            if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
                # turret 1
                if mouseX > t1X and mouseX < t1X + size and mouseY > t1Y and mouseY < t1Y + size:
                    if self.gatlingPrice <= self.game.gold:
                        if not self.game.building.turret or self.game.building.turret.type != "classic":
                            self.game.building.placeTurret("classic")
                            self.game.messageGlobal = "Turret built ! \n - 50 gold"
                            self.game.building = False
                        else:
                            self.message = "There is already one !"
                    else:
                        self.message = "Not enough gold !"

                # turret 2
                if mouseX > t2X and mouseX < t2X + size and mouseY > t2Y and mouseY < t2Y + size:
                    if self.sniperPrice <= self.game.gold:
                        if not self.game.building.turret or self.game.building.turret.type != "sniper":
                            self.game.building.placeTurret("sniper")
                            self.game.messageGlobal = "Sniper built ! \n - 100 gold"
                            self.game.building = False
                        else:
                            self.message = "There is already one !"
                    else:
                        self.message = "Not enough gold !"

                # turret 3
                if mouseX > t3X and mouseX < t3X + size and mouseY > t3Y and mouseY < t3Y + size:
                    if self.teslaPrice <= self.game.gold:
                        if not self.game.building.turret or self.game.building.turret.type != "tesla":
                            self.game.building.placeTurret("tesla")
                            self.game.messageGlobal = "Tesla built ! \n - 200 gold"
                            self.game.building = False
                        else:
                            self.message = "There is already one !"
                    else:
                        self.message = "Not enough gold !"
                    
        elif self.game.upgrade:
            originX = 35
            originY = 35
            size = 30
            t1X = originX + 10
            t1Y = originY + 10
            t2X = t1X + 40
            t2Y = t1Y
            t3X = t2X + 40
            t3Y = originY + 10
            if not self.game.upgrade.turret:
                self.game.messageGlobal = "There is no turret to upgrade!"
            else:
                if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
                    # turret 1
                    if mouseX > t1X and mouseX < t1X + size and mouseY > t1Y and mouseY < t1Y + size:
                        if self.gatlingPriceScenarium <= self.game.scenarium:
                            if self.game.upgrade.turret.type == "classic":
                                self.game.upgrade.turret.damage *= 2
                                self.game.scenarium -= self.gatlingPriceScenarium
                                self.gatlingPriceScenarium *= 2
                                self.game.messageGlobal = "Turret Upgrade ! \n - "+str(self.gatlingPriceScenarium)+" Scenarium"
                                self.game.upgrade = False
                            else:
                                self.message = "Not the same turret!"
                        else:
                            self.message = "Not enough scenarium !"

                    # turret 2
                    if mouseX > t2X and mouseX < t2X + size and mouseY > t2Y and mouseY < t2Y + size:
                        if self.sniperPriceScenarium <= self.game.scenarium:
                            if self.game.upgrade.turret.type == "sniper":
                                self.game.upgrade.turret.damage *= 2
                                self.game.scenarium -= self.sniperPriceScenarium
                                self.sniperPriceScenarium *= 2
                                self.game.messageGlobal = "Turret Upgrade ! \n - "+str(self.sniperPriceScenarium)+" Scenarium"
                                self.game.upgrade = False
                            else:
                                self.message = "Not the same turret!"
                        else:
                            self.message = "Not enough scenarium !"
                    # turret 3
                    if mouseX > t3X and mouseX < t3X + size and mouseY > t3Y and mouseY < t3Y + size:
                        if self.teslaPriceScenarium <= self.game.scenarium:
                            if self.game.upgrade.turret.type == "tesla":
                                self.game.upgrade.turret.damage *= 2
                                self.game.scenarium -= self.teslaPriceScenarium
                                self.teslaPriceScenarium *= 2
                                self.game.messageGlobal = "Turret Upgrade ! \n - "+str(self.teslaPriceScenarium)+" Scenarium"
                                self.game.upgrade = False
                            else:
                                self.message = "Not the same turret!"
                        else:
                            self.message = "Not enough scenarium !"

        if self.messageCooldown.elapsed():
            self.message = ""
            self.game.messageGlobal = ""

class Turret(GameObject):
    
    def __init__(self, game, x, y, w, h, c=10):
        super().__init__(x, y, w, h, c)
        self.game = game
        self.fireCooldown = tweening.TimedBool(15)
        self.range = 80
        self.target = None
        self.type = "classic"
        self.damage = 1
    
    def getDistance(self, enemy):
        x = enemy.x+enemy.w/2
        y = enemy.y+enemy.w/2
        x -= self.x + self.w/2
        y -= self.y + self.h/2
        return math.sqrt((x)**2+(y)**2)

    def updateTarget(self):
        # Lock onto an enemy
        if not self.target:
            for i in range(self.game.enemies.size):
                cur = self.game.enemies.array[i]
                if not cur:
                    continue
                distanceToEnemy = self.getDistance(cur)
                if distanceToEnemy < self.range:
                    self.target = cur
        # Break target lock
        else:
            distanceToEnemy = self.getDistance(self.target)
            if distanceToEnemy > self.range or self.target.life < 1:
                self.target = None
    
    def update(self):
        self.updateTarget()
        
        if self.target and self.fireCooldown.elapsed():
            self.fireCooldown.reset()
            self.shoot()
    
    def draw(self):
        pyxel.rect(self.x, self.y, self.w, self.h, self.color)
    
    def shoot(self):
        directionX = (self.target.x + self.target.w/2 + self.target.speedVect["x"]*self.target.speed*10) - (self.x + self.w/2)
        directionY = (self.target.y + self.target.h/2 + self.target.speedVect["y"]*self.target.speed*10) - (self.y + self.h/2)
        norme = math.sqrt(directionX**2 + directionY**2)
        direction = {"x": directionX/norme, "y": directionY/norme}
        self.game.bullets.add(Bullet(self.x + self.w/2, self.y + self.h/2, 2, 2, direction, self.type, self.range,self.damage))

class Sniper(Turret):
    
    def __init__(self, game, x, y, w, h):
        super().__init__(game, x, y, w, h, 5)
        self.fireCooldown = tweening.TimedBool(60*3)
        self.range = 120
        self.type = "sniper"
        self.damage = 10

class Tesla(Turret):
    
    def __init__(self, game, x, y, w, h):
        super().__init__(game, x, y, w, h, 11)
        self.fireCooldown = tweening.TimedBool(60*2)
        self.range = 60
        self.type = "tesla"
        self.damage = 1
    
    def shoot(self):
        directionX = (self.target.x + self.target.w/2 + self.target.speedVect["x"]*self.target.speed*10) - (self.x + self.w/2)
        directionY = (self.target.y + self.target.h/2 + self.target.speedVect["y"]*self.target.speed*10) - (self.y + self.h/2)
        norme = math.sqrt(directionX**2 + directionY**2)
        direction = {"x": directionX/norme, "y": directionY/norme}
        self.game.bullets.add(ShockWave(self.x + self.w/2, self.y + self.h/2, 2, 2, direction, self.range, self.damage))
