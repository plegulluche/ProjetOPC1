from entities.mac import Mac
from entities.gardien import Gardien
from entities.items import Items
from entities.constantes import *
from random import randint
import os
import pygame
from pygame.locals import *

class Labyrinthe:
    """ Class Labyrinthe"""
    
    def __init__(self):
        """init method"""
        self.largeur = 0  
        self.hauteur = 0
        self.walls = []
        self.item = []
        self.fichier = fichier
        self.itemlist = itemlaby
     
    def read_lab_file(self):
        """method to read a file text containing blueprint of the maze and saving elements in variables"""
        with open(self.fichier, "r") as labyr:     
            lines = labyr.readlines() 
            self.largeur = len(lines[0])-1
            index = 0
            line_number = 0
            for idx, line in enumerate(lines):
                for characters in line:
                    if characters == "M":
                        self.mac = Mac(latitude=index, longitude=line_number) 
                    elif characters == "G":
                        self.gardien = Gardien(latitude=index, longitude=line_number)
                    elif characters == "m":
                        self.walls.append((index, line_number))
                    index += 1
                index = 0
                line_number += 1           
            self.hauteur = idx + 1

    def reprlab(self, WIN):
        """method displaying level with list of the walls and mac and gardian objects"""
        #loading images
        mur = pygame.image.load(os.path.join("ressource", "mur_laby.png")).convert()
        #going through each line    
        for colone in range(self.hauteur):
            #going through each sprite in the line
            for ligne in range(self.largeur):
                #calculating real position in pixel
                x = ligne * sprite_size
                y = colone * sprite_size
                if (ligne, colone) in self.walls:
                    WIN.blit(mur, (x,y))
                elif ligne == self.mac.latitude and colone == self.mac.longitude:
                    WIN.blit(self.mac.image, (x,y))
                elif ligne == self.gardien.latitude and colone == self.gardien.longitude:
                    WIN.blit(self.gardien.image, (x,y))
                else:
                    for items in self.item:                  
                        if (ligne, colone) == (items.latitude, items.longitude):
                            WIN.blit(items.image, (x,y))

    def additemstolab(self):
        """method to add in a random fashion the items in the labyrinth"""
        for elements in itemlaby:
            condition = True
            while condition:
                itemposition = (randint(0, self.largeur-1), randint(0, self.hauteur-1))
                if itemposition not in self.walls and itemposition != (self.mac.latitude, self.mac.longitude) and itemposition != (self.gardien.latitude, self.gardien.longitude):               
                    self.item.append(Items(itemposition[0],itemposition[1],elements.get("name"),elements.get("image")))
                    condition = False
