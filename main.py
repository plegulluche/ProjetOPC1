#!/usr/bin/python3
# -*- coding: Utf-8 -*
"""
Game MacGyver versus the labyrinth.
Make Mac get out of the labyrinth.

Scripts Python
Fichiers: labyrinthe.py, mac.py, gardien.py, constantes.py, items.py, main.py
"""

import pygame
from pygame.locals import *
import os
from labyrinthe import Labyrinthe as labyr
import constantes

#initialize pygame modules
pygame.init()

WIDTH, HEIGHT = 450, 450
#opening pygame window
WIN = pygame.display.set_mode((WIDTH, HEIGHT), RESIZABLE)

#window label
pygame.display.set_caption("Mac gyver et le labyrinthe")


def main():

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
        #boucle title screen
        while run_acceuil:
            pygame.time.Clock().tick(FPS)

            for event in pygame.event.get():
                if event.type == QUIT:
                    run_acceuil = False
                    run = False
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
                        maze.movemac("right")
                    elif event.key == K_LEFT:
                        maze.movemac("left")
                    elif event.key == K_UP:
                        maze.movemac("up")
                    elif event.key == K_DOWN:
                        maze.movemac("down")

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

if __name__ == "__main__":
    main()
  