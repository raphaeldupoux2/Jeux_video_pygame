import pygame
from acteur import Acteur


class Player(Acteur):

    def __init__(self, game_instance):
        super().__init__(game_instance, 100, 100, 0.5, 20, 20, (0, 0, 255))
        self.hidden = False
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

    def comportement(self):
        self.move()
        if self.dead:
            self.prend_degat(0.01)

    def affiche(self):
        super().affiche()
        self.game_instance.affiche_pv(self)
