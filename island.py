import cfg
import pygame
import player
import os

###module island###
# used to define:
#
# position, image and global coordinates of an object
# setting object's vision surface to True or False
# move and display object across map if vision surface is True
#
###module island###

island1Img = pygame.image.load(os.path.join("resources", "image", "island.png"))
island2Img = pygame.image.load(os.path.join("resources", "image", "island2.png"))                             

#klasa otok
class Island(object):
    def __init__(self, position, islandImg, globalCoord):
        """
        setting object's vision to False and diffX to 0(distance difference between objectGlobalCoord X and shipGlobalCoord X)
        """
        
        self.islandPosition = position
        self.islandImg = islandImg
        self.image = cfg.Image(self.islandImg)
        self.islandGlobalCoord = globalCoord
        self.islandInVision = False
        self.diffX = 0
        pass

    def checkGlobal(self):
        """
        checks if ship's globalCoordinates are in object's vision, setting objectInVision to True or False
        """
        
        self.islandVisionSurfaceX1 = self.islandGlobalCoord[0] - cfg.scrWidth/2 - 400
        self.islandVisionSurfaceX2 = self.islandGlobalCoord[0] + cfg.scrWidth/2 + 400
        self.islandVisionSurfaceY1 = self.islandGlobalCoord[1] - cfg.scrHeight/2 - 400
        self.islandVisionSurfaceY2 = self.islandGlobalCoord[1] + cfg.scrHeight/2 + 400
        
        if player.ship.globalCoord[0] >= self.islandVisionSurfaceX1 and player.ship.globalCoord[0] <= self.islandVisionSurfaceX2 and player.ship.globalCoord[1] >= self.islandVisionSurfaceY1 and player.ship.globalCoord[1] <= self.islandVisionSurfaceY2:
            self.islandInVision = True
            self.moveIsland()
            self.displayIsland()
        else:
            self.islandInVision = False
            
    def moveIsland(self):
        """
        based on quadrant, add or substract distance difference to screenWidth/2 and screenHeight/2 to get object's position for displaying
        """
        
        if self.islandInVision:
            if player.ship.globalCoord[0] < self.islandGlobalCoord[0]:                        #prvi kvadrant
                if player.ship.globalCoord[1] > self.islandGlobalCoord[1]:
                    self.diffX = self.islandGlobalCoord[0] - player.ship.globalCoord[0]
                    self.diffY = player.ship.globalCoord[1] - self.islandGlobalCoord[1]
                    self.islandPosition[0] = cfg.scrWidth/2 + self.diffX
                    self.islandPosition[1] = cfg.scrHeight/2 - self.diffY
                                        
                else:                                                                         #cetvrti kvadrant
                    self.diffX = self.islandGlobalCoord[0] - player.ship.globalCoord[0]
                    self.diffY = self.islandGlobalCoord[1] - player.ship.globalCoord[1]
                    self.islandPosition[0] = cfg.scrWidth/2 + self.diffX
                    self.islandPosition[1] = cfg.scrHeight/2 + self.diffY
                    
            else:                                                                             #drugi kvadrant
                if player.ship.globalCoord[1] > self.islandGlobalCoord[1]:
                    self.diffX = player.ship.globalCoord[0] - self.islandGlobalCoord[0]
                    self.diffY = player.ship.globalCoord[1] - self.islandGlobalCoord[1]
                    self.islandPosition[0] = cfg.scrWidth/2 - self.diffX
                    self.islandPosition[1] = cfg.scrHeight/2 - self.diffY
                                        
                else:                                                                         #treci kvadrant
                    self.diffX = player.ship.globalCoord[0] - self.islandGlobalCoord[0]
                    self.diffY = self.islandGlobalCoord[1] - player.ship.globalCoord[1]
                    self.islandPosition[0] = cfg.scrWidth/2 - self.diffX
                    self.islandPosition[1] = cfg.scrHeight/2 + self.diffY
                    
        
    def displayIsland(self):
        """
        displaying object
        """
        
        self.image.imageRect.center = (self.islandPosition[0], self.islandPosition[1])
        self.image.run()

class seaObject(object):
    """
    sea object testing class
    """
    
    def __init__(self, position, image, globalCoord):
        self.objectPosition = position
        self.objectImage = image
        self.objectGlobalCoord = globalCoord
        
island1 = Island([0,0], island1Img, (1500,800))
island2 = Island([0,0], island2Img, (1200,-500))
