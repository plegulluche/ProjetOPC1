from mac import *
from gardien import *

liste_mur = []
MAC = Mac()
GARDIEN = Gardien()

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
        
                

tuplesmurs("laby.txt")
print(liste_mur)

def reprlab(listemur):
    """fonction affichant le laby dans la console sans avoir besoin du fichier, prend la liste des murs en parametre"""                # supprimer le while en for 
    lignes = range(0,15)
    colones = range(0,15)
    for colone in colones:
        print("colone =", colone)
        for ligne in lignes:
            print("ligne =", ligne)
            if (ligne, colone) in liste_mur:
                if (ligne, colone) == (MAC.latitude, MAC.longitude):
                    print("M")
                elif (ligne, colone) == (GARDIEN.latitude, GARDIEN.longitude):
                    print("G")
                else:
                    print("m")
            else:
                print("0")
                
                  #print sans l avoir dans la console dans le mettre dans une variable caractere par caractere 
       

reprlab(liste_mur)
