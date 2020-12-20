class Gardien:
    """classe gardien """

    def __init__(self, latitude, longitude):
        """constructeur de la classe , prend en parametres un latitude et longitude sous forme d'integer"""
        self.latitude = latitude
        self.longitude = longitude

    def __repr__(self):
        """affiche notre Gardien dans la console"""
        return "G"
    
    def __str__(self):
        """affiche Gardien quand print est appelé"""
        return repr(self)