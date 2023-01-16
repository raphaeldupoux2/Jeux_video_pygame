import math
import random

import pygame
from acteur import Acteur


class Player(Acteur):

    def __init__(self, game_instance):
        super().__init__(game_instance, 100, 100, 0.5, 20, 20, (0, 0, 255), True)
        self.hidden = False
        self.dead = False

    def move(self):
        keys = pygame.key.get_pressed()
        self.limit()
        if keys[pygame.K_LEFT]:
            self.direction = math.pi
            self.bouge()
        if keys[pygame.K_RIGHT]:
            self.direction = 0
            self.bouge()
        if keys[pygame.K_UP]:
            self.direction = - math.pi / 2
            self.bouge()
        if keys[pygame.K_DOWN]:
            self.direction = math.pi / 2
            self.bouge()

    def prend_degat(self, degat: float):
        super().prend_degat(degat)
        if not self.dead:
            if self.pv <= 0:
                self.game_instance.run = False
                self.dead = True
        else:
            if self.pv <= -1000:
                self.game_instance.run = False

    def dig(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if pygame.key.get_focused() and pygame.key.get_pressed()[pygame.K_SPACE]:
                    print("digging")
                    dug = random.randint(0, 100)
                    if dug == 0:
                        print("Vous avez un point de destin !")
                        self.pv = 1000
                        self.game_instance.run = False
                        self.dead = False
                    else:
                        print("De la merde, toujours de la merde")

    def comportement(self):
        self.move()
        if self.dead:
            self.prend_degat(0.01)
            self.dig()

    def affiche(self):
        super().affiche()
        self.game_instance.affiche_pv(self)
