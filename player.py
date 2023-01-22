import math
import random

import pygame
from acteur import Acteur


class Player(Acteur):

    def __init__(self, game_instance):
        super().__init__(game_instance, 100, 100, 0.5, 20, 20, (0, 0, 255), True, True)

    def move(self):
        keys = pygame.key.get_pressed()
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

    @property
    def dead(self):
        return self.pv <= 0

    def prend_degat(self, degat: float):
        super().prend_degat(degat)

    def dig(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if pygame.key.get_focused() and pygame.key.get_pressed()[pygame.K_SPACE]:
                    dug = random.randint(0, 5)
                    if dug == 0:
                        print("Vous avez un point de destin !")
                        self.pv = 1000
                        self.game_instance.run = False

                    else:
                        print("De la merde, toujours de la merde")

    def comportement(self):
        self.move()
        if self.dead:
            if self.game_instance.monde != self.game_instance.paradis_des_bouseux:
                self.game_instance.rejoint_monde(self.game_instance.paradis_des_bouseux)

        if self.pv <= -1000:
            if self.game_instance.monde == self.game_instance.paradis_des_bouseux:
                self.game_instance.rejoint_monde(self.game_instance.monde_normal)
                self.pv = 1000


    def affiche(self):
        super().affiche()
        self.game_instance.affiche_pv(self)
