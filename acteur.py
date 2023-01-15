import math
from abc import ABC, abstractmethod
from random import uniform

import pygame


class Acteur(ABC):

    def __init__(self, game_instance, x, y, vel, sizeX, sizeY, couleur, solide):
        self.x: float = x
        self.y: float = y
        self.vel: float = vel
        self.game_instance = game_instance
        self.game_instance.acteurs.append(self)
        self.pv = 1000
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.couleur = couleur
        self.solide = solide
        self.direction = uniform(0, 2 * math.pi)

    def limit(self):
        if self.x < 0:
            self.x = 0
        if self.x + self.game_instance.player[0].sizeX > self.game_instance.width:
            self.x = self.game_instance.width - self.game_instance.player[0].sizeX
        if self.y < 0:
            self.y = 0
        if self.y + self.game_instance.player[0].sizeY > self.game_instance.hidth:
            self.y = self.game_instance.hidth - self.game_instance.player[0].sizeY

    def prend_degat(self, degat: float):
        self.pv -= degat

    @abstractmethod
    def comportement(self):
        pass

    def affiche(self):
        pygame.draw.rect(self.game_instance.win, self.couleur, (self.x, self.y, self.sizeX, self.sizeY))

    def touche(self, acteur, marge=0):
        return acteur.x < self.x + self.sizeX + marge and self.x - marge < acteur.x + acteur.sizeX and \
            acteur.y < self.y + self.sizeY + marge and self.y - marge < acteur.y + acteur.sizeY

    def _bouge(self):
        self.x += math.cos(self.direction) * self.vel
        self.y += math.sin(self.direction) * self.vel

    def bouge(self):
        old_x, old_y = self.x, self.y
        self._bouge()
        if not self.solide:
            return

        for sol in filter(lambda x: x.solide, self.game_instance.acteurs):
            if sol != self and sol.touche(self):
                new_x = self.x
                self.x = old_x
                if not sol.touche(self):
                    continue

                self.x = new_x
                self.y = old_y
                if not sol.touche(self):
                    continue

                self.x = old_x
                break
