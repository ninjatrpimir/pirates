import pygame
import cfg
import math
import os

###module player###
# used to define:
#
# ship's movement, rotation, defining abilities and hopefully menu
# initializing game
#
###module player###

class Ship(object):

    def __init__(self):
        self.shipPosition = [cfg.scrWidth/2, cfg.scrHeight/2]
        self.globalCoord = [1000, 1000]
        self.newGlobalX = 1000
        self.newGlobalY = 1000
        self.globalCoordVisionX = 1000
        self.globalCoordVisionY = 1000
        self.shipImg = pygame.image.load(os.path.join("resources", "image", "newboat.png"))
        self.image = cfg.Image(self.shipImg)
        self.rotateShipFlag = False
        self.angle = 0
        self.finalAngle = 0
        self.angleReversed = False
        self.displayFirst = True
        self.newPosition = [0,0]
        self.isMoving = False
        self.shipSpeed = 4
        self.combatSpeed = 1
        self.armor = 1
        self.crew = 1
        self.moral = 1
        self.food = 10
        self.water = 10
        self.fruit = 10
        self.cannons = 1
        self.engine = 1
        self.vision = 1
        self.abilityDict = {'storm' : {'runCondition' : False,
                                       'abilityDuration' : 10000},
                            'ghost' : {'runCondition' : False,
                                       'abilityDuration' : 10000},
                            'sonar' : {'runCondition' : False,
                                       'abilityDuration' : 10000}
                            }
        self.getAbilityImage()
        

    def displayShip(self):
        """
        displaying ship on screen
        """
        
        self.rotateShip()
        self.image.imageRect.center = self.shipPosition[0], self.shipPosition[1]
        self.image.run()


    def getNewPosition(self):
        """
        receives mouse position
        """
        
        if cfg.rightMouseBClicked:
            self.newPosition = cfg.mousePos
            self.isMoving = True
            self.displayFirst = False


    def getRotation(self):
        """
        receives ending angle in integer
        """
        
        if cfg.rightMouseBClicked:
            self.rotateShipFlag = True
            self.finalAngle = math.atan2(self.newPosition[1]-(self.shipPosition[1]+32),self.newPosition[0]-(self.shipPosition[0]+26))
            self.finalAngle = int((self.finalAngle * 10) + 0.5) / 10.0


    def rotateShip(self):
        """
        defines ship's rotation moving based on ship's starting and ending angle
        """
        
        self.getRotation()
        if self.rotateShipFlag == True:
            if self.finalAngle < self.angle:
                if self.angle > 1.5 and self.angle <= 3.1 and self.finalAngle < -1.5 and self.finalAngle >= -3.0:
                    if self.angle == 3.1:
                        self.angle = -3.1
                        self.angle += 0.1
                        self.angle = int((self.angle * 10) + 0.5) / 10.0
                        self.rotatedShipImg = pygame.transform.rotate(self.shipImg, 360-self.angle*57.29)
                        self.image = cfg.Image(self.rotatedShipImg)
                    else:
                        self.angle += 0.1
                        self.angle = int((self.angle * 10) + 0.5) / 10.0
                        self.rotatedShipImg = pygame.transform.rotate(self.shipImg, 360-self.angle*57.29)
                        self.image = cfg.Image(self.rotatedShipImg)
                else:
                    self.angle -= 0.1
                    self.angle = int((self.angle * 10) - 0.5) / 10.0
                    self.rotatedShipImg = pygame.transform.rotate(self.shipImg, 360-self.angle*57.29)
                    self.image = cfg.Image(self.rotatedShipImg)
            elif self.finalAngle > self.angle:
                if self.angle < -1.5 and self.angle >= -3.0 and self.finalAngle <= 3.0 and self.finalAngle > 1.5:
                    if self.angle == -3.0:
                        self.angle = 3.1
                        self.angle -= 0.1
                        self.angle = int((self.angle * 10) - 0.5) / 10.0
                        self.rotatedShipImg = pygame.transform.rotate(self.shipImg, 360-self.angle*57.29)
                        self.image = cfg.Image(self.rotatedShipImg)
                    else:
                        self.angle -= 0.1
                        self.angle = int((self.angle * 10) - 0.5) / 10.0
                        self.rotatedShipImg = pygame.transform.rotate(self.shipImg, 360-self.angle*57.29)
                        self.image = cfg.Image(self.rotatedShipImg)
                else:
                    self.angle += 0.1
                    self.angle = int((self.angle * 10) + 0.5) / 10.0
                    self.rotatedShipImg = pygame.transform.rotate(self.shipImg, 360-self.angle*57.29)
                    self.image = cfg.Image(self.rotatedShipImg)
            elif self.finalAngle == 0.0:
                if self.angle < self.finalAngle:
                    self.angle += 0.1
                    self.angle = int((self.angle * 10) + 0.5) / 10.0
                    self.rotatedShipImg = pygame.transform.rotate(self.shipImg, 360-self.angle*57.29)
                    self.image = cfg.Image(self.rotatedShipImg)
                elif self.angle > self.finalAngle:
                    self.angle -= 0.1
                    self.angle = int((self.angle * 10) + 0.5) / 10.0
                    self.rotatedShipImg = pygame.transform.rotate(self.shipImg, 360-self.angle*57.29)
                    self.image = cfg.Image(self.rotatedShipImg)
                else:
                    pass
        else:
            self.rotateShipFlag = False                                                                                                                 # flag True set on mouseclick

        if self.angle == self.finalAngle:
            self.angleReversed = False                                                                                                                  # flag True set for reversing angle


    def getCoords(self):
        """
        counting and storing ship's global coordinates
        """
        
        if self.newPosition[0] < cfg.scrWidth/2:
            if self.newPosition[1] < cfg.scrHeight/2:                              # 2nd quadrant
                self.diffX = cfg.scrWidth/2 - self.newPosition[0]
                self.diffY = cfg.scrHeight/2 - self.newPosition[1]
                self.newGlobalX = self.globalCoord[0] - self.diffX
                self.newGlobalY = self.globalCoord[1] - self.diffY
                    
            else:                                                                  # 3rd quadrant
                self.diffX = cfg.scrWidth/2 - self.newPosition[0]
                self.diffY =  self.newPosition[1] - cfg.scrHeight/2
                self.newGlobalX = self.globalCoord[0] - self.diffX
                self.newGlobalY = self.globalCoord[1] + self.diffY

        else:                                                                      # 4tf quadrant
            if self.newPosition[1] > cfg.scrHeight/2: 
                self.diffX =  self.newPosition[0] - cfg.scrWidth/2
                self.diffY = self.newPosition[1] - cfg.scrHeight/2
                self.newGlobalX = self.globalCoord[0] + self.diffX
                self.newGlobalY = self.globalCoord[1] + self.diffY
                    
            else:                                                                  # 1st quadrant
                self.diffX = self.newPosition[0] - cfg.scrWidth/2
                self.diffY = cfg.scrHeight/2 - self.newPosition[1]
                self.newGlobalX = self.globalCoord[0] + self.diffX
                self.newGlobalY = self.globalCoord[1] - self.diffY

    def getMovementPath(self):
        """
        counting diagonal distance between starting and ending coordinate position and storing coordinates for that path
        """
        if self.isMoving:
            self.getCoords()
            self.listY = []
            self.listX = []

            if self.diffX > self.diffY:
                if self.newGlobalX > self.globalCoord[0]:
                    self.listX = range(int(self.globalCoord[0]), int(self.newGlobalX + 1))
                else:
                    self.listX = range(int(self.newGlobalX), int(self.globalCoord[0] + 1))
                    self.listX = self.listX[::-1]

                for x in self.listX:
                    self.Y = (self.globalCoord[1] - self.newGlobalY) / (self.globalCoord[0] - self.newGlobalX) * (x - self.globalCoord[0]) + self.globalCoord[1]
                    self.listY.append(int(self.Y))

                self.coordIndexMaxLength = len(self.listX) - 1
                self.coordIndex = 0

            else:
                if self.newGlobalY > self.globalCoord[1]:
                    self.listY = range(int(self.globalCoord[1]), int(self.newGlobalY + 1))
                else:
                    self.listY = range(int(self.newGlobalY), int(self.globalCoord[1] + 1))
                    self.listY = self.listY[::-1]

                for y in self.listY:
                    self.X = (self.globalCoord[0] - self.newGlobalX) / (self.globalCoord[1] - self.newGlobalY) * (y - self.globalCoord[1]) + self.globalCoord[0]
                    self.listX.append(int(self.X))

                self.coordIndexMaxLength = len(self.listY) - 1
                self.coordIndex = 0
        
        self.isMoving = False


    def moveShip(self):
        if self.newGlobalX != self.globalCoord[0] and self.newGlobalY != self.globalCoord[1]:
            if self.coordIndex <= self.coordIndexMaxLength:
                self.globalCoord[0] = self.listX[self.coordIndex]
                self.globalCoord[1] = self.listY[self.coordIndex]
                self.coordIndex += self.shipSpeed
            else:
                self.globalCoord[0] = self.newGlobalX
                self.globalCoord[1] = self.newGlobalY
                

    def setGlobalCoords(self):
        if self.globalCoord[0] > self.newGlobalX:
            self.globalCoord[0] -= self.shipSpeed
            if self.globalCoord[0] <= self.newGlobalX:
                self.globalCoord[0] = self.newGlobalX
                
        elif self.globalCoord[0] < self.newGlobalX:
            self.globalCoord[0] += self.shipSpeed
            if self.globalCoord[0] >= self.newGlobalX:
                self.globalCoord[0] = self.newGlobalX
                
        else:
            pass

        if self.globalCoord[1] > self.newGlobalY:
            self.globalCoord[1] -= self.shipSpeed
            if self.globalCoord[1] <= self.newGlobalY:
                self.globalCoord[1] = self.newGlobalY
                
        elif self.globalCoord[1] < self.newGlobalY:
            self.globalCoord[1] += self.shipSpeed
            if self.globalCoord[1] >= self.newGlobalY:
                self.globalCoord[1] = self.newGlobalY
                
        else:
            pass
            

    def getAbilityImage(self):
        self.stormImage = pygame.image.load(os.path.join("resources", "image", "olujaFINAL.png"))
        self.stormImageRect = self.stormImage.get_rect()

    def runAbility(self, name):
        self.name = name
        if self.name == "storm":
            self.abilityDict[self.name]['runCondition'] = True
            self.stormDuration = 0
        elif self.name == "ghost":
            self.abilityDict[self.name]['runCondition'] = True
            self.ghostDuration = 0
        elif self.name == "sonar":
            self.abilityDict[self.name]['runCondition'] = True
            self.sonarDuration = 0
        else:
            pass
            
    def displayAbility(self):
        if self.abilityDict['storm']['runCondition']:
            if self.stormDuration <= self.abilityDict['storm']['abilityDuration']:
                self.stormImageRect.center = self.shipPosition
                cfg.gameWindow.blit(self.stormImage, self.stormImageRect)
                self.stormDuration += 10
            else:
                self.abilityDict['storm']['runCondition'] = False
        if self.abilityDict['ghost']['runCondition']:
            print('ghost')
            self.abilityDict['ghost']['runCondition'] = False
        if self.abilityDict['sonar']['runCondition']:
            print('sonar')
            self.abilityDict['sonar']['runCondition'] = False
                
    def runShip(self):
        self.getNewPosition()
        self.getMovementPath()
        self.moveShip()
        self.displayShip()
        self.displayAbility()

        
ship = Ship()

#klasa Ability
class Ability(object):
    def __init__(self, position, name):
        self.position = position
        self.name = name
        self.surface = pygame.Surface((75,30))
        self.surface.fill((0,0,0))
        self.rect = pygame.Rect(self.position, (75,30))
        
    def display(self):
        cfg.gameWindow.blit(self.surface, self.rect)
        
    def runAbility(self):
        if cfg.leftMouseBClicked and self.rect.collidepoint(cfg.mousePos):
            ship.runAbility(self.name)

            
    def run(self):
        self.display()
        self.runAbility()

stormAbility = Ability((100, 700), "storm")
ghostAbility = Ability((200, 700), "ghost")
sonarAbility = Ability((300, 700), "sonar")
