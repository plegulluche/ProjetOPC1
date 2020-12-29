class Mac:
    """classe mac que des coords en attributs"""
    name = "Mac"

    def __init__(self, latitude=0, longitude=0):
        """constructeur classe Mac prend en parametre latitude et longitude sous forme d'integer"""
        self.latitude = latitude
        self.longitude = longitude

    def __repr__(self):
        """afficher notre personnage Mac dans la console"""
        return "M"  
    
    def __str__(self):
        """affiche notre mac quand print est appelé"""
        return repr(self)

    def __getattr__(self):
        pass