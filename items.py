class Items:
    """objets posés dans le labyrinthe"""

    def __init__(self, latitude, longitude, name, image):
        """constructeur de la classe Objects"""
        self.latitude = latitude
        self.longitude = longitude
        self.name = name
        self.image = image
    
    def __str__(self):
        """affiche les objects avec print"""
        return self.name

    def __repr__(self):
        """affiche les objects dans la console"""
        return self.name