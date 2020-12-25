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
        while ligne != "":  #lire un fichier ligne par ligne et le refaire sans le while
            for index in range(0,15,1): #rajouter ajout de mac et du gardien a partir du fichier
                if ligne[index] == "m":
                    mur = (index,colone)
                    liste_mur.append(mur)
            colone += 1
            ligne = labyr.readline()


tuplesmurs("laby.txt")

def reprlab(listemur):
    """fonction affichant le laby dans la console sans avoir besoin du fichier, prend la liste des murs en parametre"""
    count = 0                 # supprimer le while en for 
    colone = 0
    lignecomplete = ""
    while count != 15:
        for index in range(0, 15):
            coord = (index, colone)
            if coord == (MAC.latitude, MAC.longitude):
                lignecomplete += "M"
                continue
            if coord == (GARDIEN.latitude, GARDIEN.longitude): #elif a la place de if
                lignecomplete += "G"
                continue
            if coord in listemur:
                lignecomplete += "m"
            else:               
                lignecomplete += "0"
        colone +=1
        print(lignecomplete) #print sans l avoir dans la console dans le mettre dans une variable caractere par caractere 
        lignecomplete = ""
        count += 1 

reprlab(liste_mur)





        


