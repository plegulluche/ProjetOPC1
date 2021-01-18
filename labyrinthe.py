from mac import Mac
from gardien import Gardien
from items import Items
from constantes import *
from random import randint

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
        """fonction prennant en paremetre le fichier texte contenant le labyrinthe.
        Le lit et enregistre les coordonnées des murs, mac et du gardien dans des tuples"""
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

    def reprlab(self):
        """Display labyrinth in the console"""    
        for colone in range(self.hauteur):
            for ligne in range(self.largeur):
                if (ligne, colone) in self.walls:
                    print("m", end="")
                elif (ligne, colone) in [(items.latitude, items.longitude) for items in self.item]: 
                    print("#", end="")
                elif ligne == self.mac.latitude and colone == self.mac.longitude:
                    print("M", end="")
                elif ligne == self.gardien.latitude and colone == self.gardien.longitude:
                    print("G", end="")
                else:
                    print("_", end="")
            print()

    
    def movemac(self):
        """moving method for mac, print the lab when mac have moved with new mac position"""
        self.user_move = input("aller en haut (U), en bas (D), a gauche (L), a droite (R) : ")
        if self.user_move.lower() == "u":
            self.mac.longitude -= 1
            if (self.mac.latitude, self.mac.longitude) in self.walls:
                self.mac.longitude += 1
        elif self.user_move.lower() == "d":
            self.mac.longitude += 1
            if (self.mac.latitude, self.mac.longitude) in self.walls:
                self.mac.longitude -=1 
        elif self.user_move.lower() == "l":
            self.mac.latitude -= 1
            if (self.mac.latitude, self.mac.longitude) in self.walls:
                self.mac.latitude += 1
        elif self.user_move.lower() == "r":
            self.mac.latitude += 1
            if (self.mac.latitude, self.mac.longitude) in self.walls:
                self.mac.latitude -= 1
        else:
            print("invalid input")
            
        if self.mac.latitude < 0:
            self.mac.latitude += 1
        elif self.mac.longitude < 0:
            self.mac.longitude += 1
        elif self.mac.latitude > 14:
            self.mac.latitude -= 1
        elif self.mac.longitude > 14:
            self.mac.longitude -= 1
        
        for item in self.item:
            if (item.latitude, item.longitude) == (self.mac.latitude, self.mac.longitude):
                self.mac.objects.append(item)                
                self.item.remove(item)
                
       
        self.reprlab()

    def additemstolab(self):
        """ajouter les objets aléatoirement dans le labyrinthe"""
        for elements in itemlaby:
            condition = True
            while condition:
                itemposition = (randint(0, self.largeur-1), randint(0, self.hauteur-1))
                if itemposition not in self.walls and itemposition != (self.mac.latitude, self.mac.longitude) and itemposition != (self.gardien.latitude, self.gardien.longitude):               
                    self.item.append(Items(itemposition[0],itemposition[1],elements.get("name"),elements.get("image")))
                    condition = False
