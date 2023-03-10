from random import randint

import pygame

from acteur import Acteur


class Buisson(Acteur):
    def __init__(self, game_instance, x=0, y=0):
        super().__init__(game_instance, x, y, 0, 80, 40, (0, 255, 0), False, False)

    def hide(self, vivant):
        if self.touche(vivant):
            vivant.hidden = True

    def comportement(self):
        for vivant in self.game_instance.vivants:
            self.hide(vivant)
