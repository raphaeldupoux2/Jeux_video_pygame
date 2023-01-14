import math
from random import randint, uniform
from acteur import Acteur


class Mechant(Acteur):

    def __init__(self, game_instance, cible):
        super().__init__(game_instance, randint(300, 1000), randint(200, 550), 0.4)
        self.cible = cible
        self.cible_atteinte = False
        self.direction = uniform(0, 2 * math.pi)
        self.hidden = False
        self.pv = 10
        self.sizeX = game_instance.size_mechantX
        self.sizeY = game_instance.size_mechantY

    def comportement(self):
        self.move()
        self.fight()

    def angle_vers(self, cible: Acteur):
        return math.atan2(cible.y - self.y, cible.x - self.x)

    def random_move(self):
        self.vel = 0.1
        self.direction += uniform(-math.pi/48, math.pi/48)
        self.x += math.cos(self.direction) * self.vel
        self.y += math.sin(self.direction) * self.vel

    def move(self):
        self.cible_atteinte = False
        self.limit()
        if self.cible.hidden is False:
            if self.x < self.cible.x - self.game_instance.size_mechantX or self.x > self.cible.x + self.game_instance.size_playerX or self.y < self.cible.y - self.game_instance.size_mechantY or self.y > self.cible.y + self.game_instance.size_playerY:
                self.vel = 0.4
                self.direction = self.angle_vers(self.cible)
                self.x += math.cos(self.direction) * self.vel
                self.y += math.sin(self.direction) * self.vel
            else:
                self.cible_atteinte = True

        else:
            if self.x >= self.cible.x - self.game_instance.size_mechantX and self.x <= self.cible.x + self.game_instance.size_playerX and self.y >= self.cible.y - self.game_instance.size_mechantY and self.y <= self.cible.y + self.game_instance.size_playerY:
                self.cible_atteinte = True
            self.random_move()

    def fight(self):
        if self.cible_atteinte:
            self.cible.prend_degat(3)
