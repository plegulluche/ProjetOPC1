class Labyrinthe:
    """ Class Game. Contains all methods necessary to run the game."""
    
    def __init__(self):
        """init method"""
        self.largeur = 15
        self.hauteur = 15
        self.murs = []
        self.fichier = "laby.txt"

    def read_lab_file(self):
        """fonction prennant en paremetre le fichier texte contenant le labyrinthe.
        Le lit et enregistre les coordonnées des murs, mac et du gardien dans des tuples"""
        with open(self.fichier, "r") as labyr:     
            colones = self.hauteur # a supprimer
            for colone in colones:
                ligne = labyr.readline()
                lignelist = list(elem for elem in ligne)
                for index in range(15):              
                    if lignelist[index] == "M":                                         
                        coord = (index, colone)
                        liste_mur.append(coord)
                    elif lignelist[index] == "G":    # lire fichier ligne par ligne ( boucler sur un fichier lpl)
                        coord = (index, colone)
                        liste_mur.append(coord)
                    elif lignelist[index] == "m":
                        coord = (index, colone)
                        liste_mur.append(coord)

                ligne = "MMMWMMA"
                index = 0
                for character in ligne:
                    if charater == "M":
                        self.walls.append((index, colonne))
                    elif character == "G":
                        self.gardian = Gardien(lattitude=index, longitude=colonne)
                    elif blablabla

    def reprlab(listemur):
        """fonction affichant le laby dans la console sans avoir besoin du fichier, 
        prend la liste des murs de mac et du gardien en parametre"""        
        lignes = range(0,15)
        colones = range(0,15)
        global mac
        global gardien
        for colone in colones:
            for ligne in lignes:            
                if (ligne, colone) in listemur:
                    if (ligne, colone) == (mac.latitude, mac.longitude):
                        print("M", end = "")
                    elif (ligne, colone) == (gardien.latitude, gardien.longitude):
                        print("G", end = "")
                    else:
                        if ligne != 15:
                            print("m", end = "")
                        else:
                            print()
                else:
                    if ligne != 15:
                        print("0", end = "")
                    else:
                        print()