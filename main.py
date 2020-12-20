from mac import *
from gardien import *

liste_mur = []
MAC = Mac(0, 0)
GARDIEN = Gardien(14, 14)

def tuplesmurs(fichier):
    """fonction prennant en paremetre le fichier texte contenant le labyrinthe.Le lit et enregistre les coordonnées des tuples dans des murs"""
    with open(fichier, "r") as labyr:
        ligne = labyr.readline()
        colone = 0
        while ligne != "":
            for index in range(0,15,1):
                if ligne[index] == "m":
                    mur = (index,colone)
                    liste_mur.append(mur)
            colone += 1
            ligne = labyr.readline()


tuplesmurs("laby.txt")

def reprlab(listemur):
    """fonction affichant le laby dans la console sans avoir besoin du fichier, prend la liste des murs en parametre"""
    count = 0
    colone = 0
    lignecomplete = ""
    while count != 15:
        for index in range(0, 15):
            coord = (index, colone)
            if coord == (MAC.latitude, MAC.longitude):
                lignecomplete += "M"
                continue
            if coord == (GARDIEN.latitude, GARDIEN.longitude):
                lignecomplete += "G"
                continue
            if coord in listemur:
                lignecomplete += "m"
            else:               
                lignecomplete += "0"
        colone +=1
        print(lignecomplete)
        lignecomplete = ""
        count += 1 

reprlab(liste_mur)





        


