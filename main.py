import pygame
import sys
from pygame.locals import *

from game_instance import Game_instance
from player import Player
from mechant import Mechant
from buisson import Buisson
from source import Source

pygame.init()
clock = pygame.time.Clock()


def parametre_game(game):
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


def parametre_paradis(game):
    player1 = Player(game)
    game.player.append(player1)


def run(game):
    pygame.time.delay(2)
    game.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


if __name__ == '__main__':

    game = Game_instance("Squarey", 1280, 720)
    parametre_game(game)

    print("start")
    while game.run:
        run(game)

    paradis = Game_instance("Paradis des Bouseux", 1280, 720)
    parametre_paradis(paradis)
    while paradis.run:
        run(paradis)

    # clock.tick(60)
    print("fin")
    pygame.quit()
