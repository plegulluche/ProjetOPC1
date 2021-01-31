#!/usr/bin/python3
# -*- coding: Utf-8 -*

import pygame
import os
from entities.game import Game


"""
Game MacGyver versus the labyrinth.
Make Mac get out of the labyrinth.

Scripts Python
Fichiers: labyrinthe.py, mac.py, gardien.py, constantes.py, items.py, main.py
"""

def main():
    game = Game()
    game.rungame()

if __name__ == "__main__":
    main()
  