from random import randint

import pygame

from acteur import Acteur


class Source(Acteur):
    def __init__(self, game_instance):
        super().__init__(game_instance, randint(300, 1000), randint(200, 450), 0)
        self.sizeX = 100
        self.sizeY = 100

    def heal(self, acteur_affecte: list):
        for acteur in acteur_affecte:
            if acteur.x < self.x + self.sizeX and acteur.x > self.x - self.game_instance.player[0].sizeX and acteur.y < self.y + self.sizeY and acteur.y > self.y - self.game_instance.player[0].sizeY:
                acteur.pv += 1
                # print(acteur.pv)

    def comportement(self):
        self.heal(self.game_instance.player)

    def affiche(self):
        pygame.draw.rect(self.game_instance.win, (0, 180, 255), (self.x, self.y, self.sizeX, self.sizeY))
