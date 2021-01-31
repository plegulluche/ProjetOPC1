import pygame

class Gardien:
    """Gardien class """
    name = "Gardien"

    def __init__(self, latitude=0, longitude=0):
        """class constructor"""
        self.image = pygame.image.load("ressource/Gardien.png").convert_alpha()
        self.latitude = latitude
        self.longitude = longitude

    def __repr__(self):
        """display gardian in console"""
        return "G"
    
    def __str__(self):
        """display gardian object for print method"""
        return repr(self)