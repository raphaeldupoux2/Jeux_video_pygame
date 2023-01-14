from random import randint

import pygame

from acteur import Acteur


class Buisson(Acteur):
    def __init__(self, game_instance):
        super().__init__(game_instance, randint(300, 1000), randint(200, 450), 0)
        self.sizeX = 80
        self.sizeY = 40

    def hide(self, acteur_affecte: list):
        for acteur in acteur_affecte:
            if acteur.x < self.x + self.sizeX and acteur.x > self.x - self.game_instance.player[0].sizeX and acteur.y < self.y + self.sizeY and acteur.y > self.y - self.game_instance.player[0].sizeY:
                acteur.hidden = True
            else:
                acteur.hidden = False

    def comportement(self):
        self.hide(self.game_instance.etre_vivant)

    def affiche(self):
        pygame.draw.rect(self.game_instance.win, (0, 255, 0), (self.x, self.y, self.sizeX, self.sizeY))
