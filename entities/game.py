import pygame
import os
from pygame.locals import *
from entities.labyrinthe import Labyrinthe as labyr
import entities.constantes

class Game:
    """Game class, initalize pygame frame and run the game loops"""
    def __init__(self):
        """Game class constructor"""
        pass

    def rungame(self):
        """Method to run the game loops"""
        #initialize pygame modules
        pygame.init()

        WIDTH, HEIGHT = 450, 450
        #opening pygame window
        WIN = pygame.display.set_mode((WIDTH, HEIGHT), RESIZABLE)

        #window label
        pygame.display.set_caption("Mac gyver et le labyrinthe")

        #main loop
        run = True
        FPS = 30
        while run:
            #load title screen
            fondacceuil = pygame.transform.scale(pygame.image.load(os.path.join("ressource", "ecran_acceuil.jpg")).convert(),(450, 450))
            WIN.blit(fondacceuil, (0,0))
            pygame.display.flip()
            run = True

            run_acceuil = True
            #title screen loop
            while run_acceuil:
                pygame.time.Clock().tick(FPS)

                for event in pygame.event.get():
                    if event.type == QUIT:
                        run_acceuil = False
                        run = False
                        rungame = False
                    elif event.type == KEYDOWN:
                        if event.key == K_SPACE:
                            run_acceuil = False
                            game = "go"
            
            if game == "go":
                #generate level  
                fond = pygame.image.load(os.path.join("ressource", "fond_laby.jpg")).convert()
                WIN.blit(fond, (0,0))
                pygame.display.flip()            
                maze = labyr()
                maze.read_lab_file()
                maze.additemstolab()
                maze.reprlab(WIN)
                pygame.display.flip()
                rungame = True

            while rungame:
                #game loop
                pygame.time.Clock().tick(FPS)

            
                for event in pygame.event.get():
                    if event.type == QUIT:
                        run = False
                        run_acceuil = False
                        rungame = False

                    elif event.type == KEYDOWN:

                        if event.key == K_RIGHT:
                            maze.mac.movemac("right")
                            if (maze.mac.latitude, maze.mac.longitude) in maze.walls:
                                maze.mac.latitude -= 1
                        elif event.key == K_LEFT:
                            maze.mac.movemac("left")
                            if (maze.mac.latitude, maze.mac.longitude) in maze.walls:
                                maze.mac.latitude += 1
                        elif event.key == K_UP:
                            maze.mac.movemac("up")
                            if (maze.mac.latitude, maze.mac.longitude) in maze.walls:
                                maze.mac.longitude += 1
                        elif event.key == K_DOWN:
                            maze.mac.movemac("down")
                            if (maze.mac.latitude, maze.mac.longitude) in maze.walls:
                                maze.mac.longitude -=1 
                        for item in maze.item:
                            if (item.latitude, item.longitude) == (maze.mac.latitude, maze.mac.longitude):
                                maze.mac.objects.append(item)                
                                maze.item.remove(item)

                WIN.blit(fond, (0,0))
                maze.reprlab(WIN)
                pygame.display.flip()

                #win condition
                if maze.mac.latitude == maze.gardien.latitude and maze.mac.longitude == maze.gardien.longitude:
                    #end loop
                    endloop = True
                    rungame = False
                    while endloop:
                        pygame.time.Clock().tick(FPS)

                        if len(maze.mac.objects) == len(maze.itemlist):
                            fondvictoire = pygame.transform.scale(pygame.image.load("ressource/fond_victoire.jpg").convert(), (450,450))
                            WIN.blit(fondvictoire, (0,0))
                            pygame.display.flip()

                            for event in pygame.event.get():
                                if event.type == QUIT:
                                    run = False
                                    run_acceuil = False
                                    rungame = False 
                                    endloop = False
                                    
                                elif event.type == KEYDOWN:

                                    if event.key == K_SPACE:
                                        endloop = False
                                        run_acceuil = True
                                    elif event.key == K_ESCAPE or event.type == QUIT:
                                        run = False
                                        run_acceuil = False
                                        rungame = False
                                        endloop = False

                        else:
                            fond_defaite = pygame.image.load("ressource/fond_defaite.jpg").convert()
                            WIN.blit(fond_defaite, (0,0))
                            pygame.display.flip()

                            for event in pygame.event.get():
                                if event.type == QUIT:
                                    run = False
                                    run_acceuil = False
                                    rungame = False
                                    endloop = False
                                if event.type == KEYDOWN:

                                    if event.key == K_SPACE:
                                        endloop = False