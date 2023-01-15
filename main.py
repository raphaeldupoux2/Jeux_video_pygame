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

    player1 = Player(game)
    game.player.append(player1)

    mechant1 = Mechant(game, player1)
    mechant2 = Mechant(game, player1)
    game.mechant.append(mechant1)
    game.mechant.append(mechant2)

    game.etre_vivant = game.mechant + game.player

    buisson1 = Buisson(game)
    game.buisson.append(buisson1)
    source1 = Source(game)
    game.source.append(source1)

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
        while pdb.run:
            run(pdb)

        player1.game_instance = game
        while game.run:
            run(game)

    # clock.tick(60)
    print("fin")
    pygame.quit()
