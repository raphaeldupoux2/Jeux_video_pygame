import math
from random import randint, uniform

from acteur import Acteur


class Mechant(Acteur):

    def __init__(self, game_instance, cible):
        super().__init__(game_instance, randint(300, 1000), randint(200, 550), 0.4, 40, 40, (255, 0, 0), True, True)
        self.cible = cible
        self.pv = 10

    def comportement(self):
        self.move()
        self.fight()

    def affiche(self):
        super().affiche()
        self.game_instance.affiche_pv(self)

    def random_move(self):
        self.direction += uniform(-math.pi / 48, math.pi / 48)
        self.bouge()

    def move(self):
        if self.cible.hidden:
            self.vel = 0.1
            self.random_move()

        else:
            self.vel = 0.4
            self.direction = self.angle_vers(self.cible)
            self.bouge()

    def fight(self):
        if self.touche(self.cible, marge=1):
            self.cible.prend_degat(3)
