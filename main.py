import pygame
import sys
from pygame.locals import *

from game_instance import Game_instance

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

    print("start")
    game.init_game()
    while game.run:
        run(game)

    print("fin")
    pygame.quit()
