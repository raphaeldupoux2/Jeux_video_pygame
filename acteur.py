import math
from abc import ABC, abstractmethod
from random import uniform

import pygame


class Acteur(ABC):

    def __init__(self, game_instance, x, y, vel, sizeX, sizeY, couleur, solide, vivant):
        self.x: float = x
        self.y: float = y
        self.vel: float = vel
        self.game_instance = game_instance
        self.game_instance.acteurs.append(self)
        self.pv = 1000
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.centreX = self.x - self.sizeX
        self.centreY = self.y - self.sizeY
        self.couleur = couleur
        self.solide = solide
        self.vivant = vivant
        self.direction = uniform(0, 2 * math.pi)
        self.hidden = False

    def prend_degat(self, degat: float):
        self.pv -= degat

    @abstractmethod
    def comportement(self):
        pass

    @property
    def x_rel(self):
        return self.x - self.game_instance.camera.x

    @property
    def y_rel(self):
        return self.y - self.game_instance.camera.y

    def affiche(self):
        pygame.draw.rect(self.game_instance.win, self.couleur, (self.x_rel, self.y_rel, self.sizeX, self.sizeY))

    def touche(self, acteur, marge=0):
        return acteur.x < self.x + self.sizeX + marge and self.x - marge < acteur.x + acteur.sizeX and \
               acteur.y < self.y + self.sizeY + marge and self.y - marge < acteur.y + acteur.sizeY

    def distance(self, acteur):
        distance = (self.x - acteur.x) ** 2 + (self.y - acteur.y) ** 2
        distanceX = self.x - acteur.x
        distanceY = self.y - acteur.x
        print(distanceX, distanceY)
        return distanceX, distanceY

    def angle_vers(self, cible):
        return math.atan2(cible.y - self.y, cible.x - self.x)

    def _bouge(self):
        self.x += math.cos(self.direction) * self.vel
        self.y += math.sin(self.direction) * self.vel

    def bouge(self):
        old_x, old_y = self.x, self.y
        self._bouge()
        if not self.solide:
            return

        for sol in self.game_instance.solides:
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

            # if abs(self.centreX - sol.centreX) < self.sizeX / 2 + sol.sizeX / 2 or abs(self.centreY - sol.centreY) < self.sizeY / 2 + sol.sizeY / 2:
            #     print("je suis bloqué dans un solide")
            #     self.couleur = (0, 0, 0)
                # self.solide = False

            # else:
            #     self.solide = True
