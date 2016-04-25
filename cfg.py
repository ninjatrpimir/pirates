import pygame

###module config###
# used to define:
#
# screen dimensions in pixels - scrDim
# screen center - scrWidth/2, scrHeight/2
# gameWindow for initializing and setting screen dimensions used in gameship.py
# left and right click set to False (defined after in gameship.py)
# pygame fonts - menuFont
# clock
# mouse position - mousePos
###module config###


scrDim = scrWidth, scrHeight = 1600, 900                                  # sceen dimensions
scrCenter = scrWidth/2, scrHeight/2
#gameWindow = pygame.display.set_mode(scrDim, pygame.FULLSCREEN)          # display is initialized and set as scrDim value
gameWindow = pygame.display.set_mode(scrDim, 0, 32)
leftMouseBClicked = False                                                 # set to True if left mouse button is clicked, else false
rightMouseBClicked = False
pygame.font.init()                                                        # initializes pygame fonts
menuFont = pygame.font.Font(None, 40)
clock = pygame.time.Clock()
minutes = 0
seconds = 0
milliseconds = 0
mousePos = (0,0)

#class Image used for managing images
class Image(object):
    def __init__(self, image, hoveredImage = None, positionCords = (0,0), positionCenter = 'center' ):
        """
        image - recevies image i.e.
            newImage = pygame.image.load(os.path.join("resources", "image", "imagename"))
            cfg.Image(newImage)
        hoveredImage - receives hovered image, if not sets to none
        positionCords - receives position on screen, if not sets to top-left
        positionCenter - receives imageRect.positionCenter
        
        """
        self.image = image
        self.hoveredImage = hoveredImage
        self.positionCords = positionCords
        self.positionCenter = positionCenter

        self.hovered = False
        self.clicked = False
        self.getImageRect()                                                                     #calling image.get_rect(), receiving imageRect
        self.positionRect()                                                                     #calling imageRect, receiving imageRect.positionCenter, i.e. imageRect.bottomright = self.positionCords
        self.getHoveredImageRect()
        # still need to check
        #self.selected = False

    def getImageRect(self):
        """
        called in __init__, passing imageRect
        """
        
        self.imageRect = self.image.get_rect()
    
    def positionRect(self):
        """
        called in __init__, receives argument positionCenter, passing imageRect.positionCenter i.e. imageRect.topleft
        """
        
        if self.positionCenter == 'center':
            self.imageRect.center = self.positionCords
        if self.positionCenter == 'topleft':
            self.imageRect.topleft = self.positionCords
        if self.positionCenter == 'topright':
            self.imageRect.topright = self.positionCords
        if self.positionCenter == 'bottomleft':
            self.imageRect.bottomleft = self.positionCords
        if self.positionCenter == 'bottomright':
            self.imageRect.bottomright = self.positionCords 

    def getHoveredImageRect(self):
        """
        called in __init__ ,receving hoveredImage, passing hoveredImage.get_rect() and hoveredImage.center
        """
        
        if self.hoveredImage != None:
            self.hoveredImageRect = self.hoveredImage.get_rect()
            self.hoveredImageRect.center = self.imageRect.center
        else:
            pass
  
    def checkClick(self):
        """
        called in Image.run()
        """
        
        if leftMouseBClicked and self.imageRect.collidepoint(pygame.mouse.get_pos()):
            self.clicked = True
        else:
            self.clicked = False

    def checkHover(self):
        """
        called in Image.run(), setting hovered flag to True or False
        """
        
        if self.imageRect.collidepoint(pygame.mouse.get_pos()):
            self.hovered = True
        else:
            self.hovered = False

    def displayImage(self):
        """
        called in Image.run(), setting to image or hoveredImage
        """
        
        if self.hovered and self.hoveredImage != None:
            gameWindow.blit(self.hoveredImage, self.hoveredImageRect)
        else:
            gameWindow.blit(self.image, self.imageRect)

    def run(self):
        self.checkClick()
        self.checkHover()
        self.displayImage()
