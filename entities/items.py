import pygame

class Items:
    """items for our labyrinth"""

    def __init__(self, latitude, longitude, name, image):
        """Items class constructor"""
        self.latitude = latitude
        self.longitude = longitude
        self.name = name
        self.image = pygame.transform.scale(pygame.image.load(image).convert_alpha(),(30,30))
    
    def __str__(self):
        """display Items object for print method"""
        return self.name

    def __repr__(self):
        """display items in console"""
        return self.name