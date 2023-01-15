import random

import pygame
from acteur import Acteur


class Player(Acteur):

    def __init__(self, game_instance):
        super().__init__(game_instance, 100, 100, 0.5)
        self.hidden = False
        self.sizeX = game_instance.size_playerX
        self.sizeY = game_instance.size_playerY
        self.dead = False

    def move(self):
        keys = pygame.key.get_pressed()
        self.limit()
        if keys[pygame.K_LEFT]:
            self.x -= self.vel
        if keys[pygame.K_RIGHT]:
            self.x += self.vel
        if keys[pygame.K_UP]:
            self.y -= self.vel
        if keys[pygame.K_DOWN]:
            self.y += self.vel

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
