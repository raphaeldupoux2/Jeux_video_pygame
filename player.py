import pygame
from acteur import Acteur


class Player(Acteur):

    def __init__(self, game_instance):
        super().__init__(game_instance, 100, 100, 0.5)
        self.hidden = False
        self.sizeX = game_instance.size_playerX
        self.sizeY = game_instance.size_playerY

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

    def prend_degat(self, degat: int):
        super().prend_degat(degat)
        if self.pv <= 0:
            self.game_instance.run = False

    def comportement(self):
        self.move()

    def affiche(self):
        pass
