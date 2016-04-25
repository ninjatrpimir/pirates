import sys
import pygame
from pygame.locals import *
import time
import cfg
import board
import player
import island
import threading


#import engine

###module gameship###
# used to define:
#
# main module, event types such as keyboard and mouse input
# initializing game
#
###module gameship###


def runMouse():
    cfg.mousePos = pygame.mouse.get_pos()

class Game(object):
    """
    main game class
    """
    
    def __init__(self):
        while True:
            cfg.leftMouseBClicked = False
            cfg.rightMouseBClicked = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    pass
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        cfg.leftMouseBClicked = True
                    elif event.button == 3:
                        cfg.rightMouseBClicked = True
            runMouse()
            board.sea.displaySea()
            island.island1.checkGlobal()
            island.island2.checkGlobal()
            player.stormAbility.run()
            player.ghostAbility.run()
            player.sonarAbility.run()
            player.ship.runShip()
            #print('posOtoka1',island.island1.islandPosition,'globBroda',player.ship.newGlobalX, player.ship.newGlobalY, player.ship.globalCoord)
            print(player.ship.angle, player.ship.finalAngle, player.ship.angleReversed)
            pygame.display.update()
            cfg.clock.tick()


if __name__ == '__main__':
    pygame.init()                     # logging events in case of errors,
    print('initializing pygame')      # advice from http://gamedev.stackexchange.com 
        # declare PirateThread objects
    # firstThread = PirateThread(arg)
    # firstThread.setName('Thread 1')

        # start running threads
    # firstThread.start()
    
        # wait for threads to finish
    # firstThread.join()
    
    
    
    
    # event = threading.Event()

        # a client thread can wait for the flag to be set
    # event.wait()

        # a server thread can set or reset it
    # event.set()
    # event.clear()
    
    cfg.clock.tick()
    Game().main(cfg.gameWindow)
