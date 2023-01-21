import pygame
import sys
from pygame.locals import *

from game_instance import Game_instance
from player import Player
from mechant import Mechant
from buisson import Buisson
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
    buisson1 = Buisson(game)
    buisson2 = Buisson(game)
    source1 = Source(game)
    player1 = Player(game)
    game.players.append(player1)
    game.camera.cible = player1
    mechant1 = Mechant(game, player1)
    mechant2 = Mechant(game, player1)

    print("start")
    while game.run:
        run(game)

    # Passage après une mort pitoyable dans Le Paradis des Bouseux ...

    pdb = Game_instance("Paradis des Bouseux", color=BROWN)
    player1.game_instance = pdb

    while True:
        player1.game_instance = pdb
        while pdb.run:
            run(pdb)

        player1.game_instance = game
        while game.run:
            run(game)

    # clock.tick(60)
    print("fin")
    pygame.quit()
