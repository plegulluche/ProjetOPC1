class Game:
    """ Class Game. Contains all methods necessary to run the game."""

    def __init__(self):
        """init method"""
    
    
    def tuplesmurs(fichier):
    """fonction prennant en paremetre le fichier texte contenant le labyrinthe.Le lit et enregistre les coordonnées des murs dans des tuples"""
    with open(fichier, "r") as labyr:
        ligne = labyr.readline()
        lignelist = list(elem for elem in ligne)
        print(type(lignelist))
        print(lignelist)
    colones = range(16)
    for colone in colones:
        for index in range(0,15):
            if ligne[index] == "M":                                          #lire un fichier ligne par ligne et le refaire sans le while
                coord = (index, colone)                                      #rajouter ajout de mac et du gardien a partir du fichier
                liste_mur.append(coord)
            elif ligne[index] == "G":
                coord = (index, colone)
                liste_mur.append(coord)
            elif ligne[index] == "m":
                coord = (index, colone)
                liste_mur.append(coord)