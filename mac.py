class Mac:
    """classe mac que des coords en attributs"""

    def __init__(self):
        """constructeur classe Mac prend en parametre latitude et longitude sous forme d'integer"""
        self.latitude = 0
        self.longitude = 0

    def __repr__(self):
        """afficher notre personnage Mac dans la console"""
        return "M"  
    
    def __str__(self):
        """affiche notre mac quand print est appelé"""
        return repr(self)