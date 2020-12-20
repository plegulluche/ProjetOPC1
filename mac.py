class Mac:
    """classe mac que des coords en attributs"""

    def __init__(self, latitude, longitude):
        """constructeur classe Mac prend en parametre latitude et longitude sous forme d'integer"""
        self.latitude = latitude
        self.longitude = longitude

    def __repr__(self):
        """afficher notre personnage Mac dans la console"""
        return "M"  
    
    def __str__(self):
        """affiche notre mac quand print est appelé"""
        return repr(self)