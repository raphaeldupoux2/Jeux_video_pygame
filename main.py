from random import randint

import pygame
import sys
from pygame.locals import *

from game_instance import Game_instance
from player import Player
from mechant import Mechant
from buisson import Buisson
from rocher import Rocher
from source import Source

BROWN = (120, 80, 35)

pygame.init()
clock = pygame.time.Clock()


def run(game):
    pygame.time.delay(2)
    game.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


if __name__ == '__main__':

    game = Game_instance("Squarey")

    # Le décors est créé en premier pour qu'il soit à l'arrière plan.

    source1 = Source(game)
    # source2 = Source(game)
    buisson1 = Buisson(game)
    buisson2 = Buisson(game)
    source1 = Source(game)
    player1 = Player(game)
    game.players.append(player1)
    game.camera.cible = player1
    mechant1 = Mechant(game, player1)
    mechant2 = Mechant(game, player1)

    for i in range(20):
        rocher1 = Rocher(game, randint(0, 1200), randint(0, 700), randint(20, 100), randint(20, 100))
        # gros_rocher = Rocher(game, 700, 500, 200, 200)
        ligne_rocher = Rocher(game, 20 * i, 500)
        ligne_rocher2 = Rocher(game, 500, 20 * i)
        game.rocher.append(rocher1)
        game.rocher.append(ligne_rocher)
        game.rocher.append(ligne_rocher2)

    print("start")
    while game.run:
        run(game)

    # Passage après une mort pitoyable dans Le Paradis des Bouseux ...

    pdb = Game_instance("Paradis des Bouseux", color=BROWN)
    player1.game_instance = pdb

    while True:
        player1.game_instance = pdb
        pdb.run = True
        while pdb.run:
            run(pdb)

        player1.game_instance = game
        game.run = True
        while game.run:
            run(game)

    # clock.tick(60)
    print("fin")
    pygame.quit()
