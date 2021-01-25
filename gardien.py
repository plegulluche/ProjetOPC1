import pygame
import os

class Gardien:
    """classe gardien """
    name = "Gardien"

    def __init__(self, latitude=0, longitude=0):
        """constructeur de la classe , prend en parametres un latitude et longitude sous forme d'integer"""
        self.image = pygame.image.load("ressource/Gardien.png").convert_alpha()
        self.latitude = latitude
        self.longitude = longitude

    def __repr__(self):
        """affiche notre Gardien dans la console"""
        return "G"
    
    def __str__(self):
        """affiche Gardien quand print est appelé"""
        return repr(self)