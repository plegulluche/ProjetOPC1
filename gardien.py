class Gardien:
    """classe gardien """

    def __init__(self):
        """constructeur de la classe , prend en parametres un latitude et longitude sous forme d'integer"""
        self.latitude = 14
        self.longitude = 14

    def __repr__(self):
        """affiche notre Gardien dans la console"""
        return "G"
    
    def __str__(self):
        """affiche Gardien quand print est appelé"""
        return repr(self)