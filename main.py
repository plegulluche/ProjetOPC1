from labyrinthe import Labyrinthe as labyr

def rungame():
    maze = labyr()
    maze.read_lab_file()
    maze.additemstolab()
    maze.reprlab()
    game = True
    while game:
        maze.movemac()
        if maze.mac.latitude == maze.gardien.latitude and maze.mac.longitude == maze.gardien.longitude:
            if len(maze.mac.objects) == len(maze.itemlist):
                game = False
                print("vous avez vaincu le gardien")
            else:
                print("perdu")
                tryagain = input("play again ? (y/n")
                if tryagain.lower() == "y":
                    rungame()
                else:
                    break

if __name__ == "__main__":
    rungame()
 
       