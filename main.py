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

    for i in range(20):
        rocher = Rocher(game, randint(0, 1200), randint(0, 700))
        ligne_rocher = Rocher(game, 20 * i, 500)
        ligne_rocher2 = Rocher(game, 500, 20 * i)
        game.rocher.append(rocher).append(ligne_rocher2).append(ligne_rocher2)
    source1 = Source(game)
    buisson1 = Buisson(game)
    game.buisson.append(buisson1)
    source1 = Source(game)
    game.source.append(source1)

    player1 = Player(game)
    game.player.append(player1)


    mechant1 = Mechant(game, player1)
    mechant2 = Mechant(game, player1)
    game.mechant.append(mechant1)
    game.mechant.append(mechant2)

    game.etre_vivant = game.mechant + game.player

    print("start")
    while game.run:
        run(game)

    # Passage après une mort pitoyable dans Le Paradis des Bouseux ...

    pdb = Game_instance("Paradis des Bouseux", color=BROWN)
    player1.game_instance = pdb
    pdb.player.append(player1)
    pdb.acteurs.append(player1)

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
