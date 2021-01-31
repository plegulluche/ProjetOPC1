import pygame
import entities.constantes

class Mac:
    """classe mac que des coords en attributs"""
    name = "Mac"

    def __init__(self, latitude=0, longitude=0):
        """constructeur classe Mac prend en parametre latitude et longitude sous forme d'integer"""
        self.image = pygame.transform.scale(pygame.image.load("ressource/MacGyver.png").convert_alpha(),(30, 30))
        self.latitude = latitude
        self.longitude = longitude
        self.objects = []

    def __repr__(self):
        """display mac in console"""
        return "M"  
    
    def __str__(self):
        """display Mac object for print method"""
        return repr(self)

    def movemac(self, direction):
            """method to move mac around the labyrinth, checks for borders limits"""
            if direction == "up":
                self.longitude -= 1
            elif direction == "down":
                self.longitude += 1
            elif direction == "left":
                self.latitude -= 1
            elif direction == "right":
                self.latitude += 1
            else:
                print("invalid input")
                
            if self.latitude < 0:
                self.latitude += 1
            elif self.longitude < 0:
                self.longitude += 1
            elif self.latitude > 14:
                self.latitude -= 1
            elif self.longitude > 14:
                self.longitude -= 1
            
            