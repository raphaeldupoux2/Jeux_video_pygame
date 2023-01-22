import math

import pygame

from camera import Camera
from monde.monde_normal import MondeNormal
from monde.paradis_des_bouseux import ParadisDesBouseux
from player import Player


class Game_instance:

    def __init__(self, titre, width=1280, hidth=720):
        self.titre = titre
        self.width = width
        self.hidth = hidth
        self.color = (0, 0, 0)
        self.win = pygame.display.set_mode((self.width, self.hidth))
        pygame.display.set_caption(self.titre)
        self.run = True
        self.acteurs = []
        self.monde_normal = MondeNormal(self)
        self.paradis_des_bouseux = ParadisDesBouseux(self)
        player1 = Player(self)
        self.players = [player1]
        self.camera = Camera(self, 100, 100, cible=player1)
        self.monde = None
        self.rejoint_monde(self.monde_normal)

    def rejoint_monde(self, monde):
        if self.monde is not None:
            self.monde.desactive()

        self.monde = monde
        self.monde.active()

    def init_game(self):
        self.monde_normal.spawn_mobs()

    @property
    def vivants(self):
        return filter(lambda x: x.vivant, self.acteurs)

    @property
    def non_vivants(self):
        return filter(lambda x: not x.vivant, self.acteurs)

    @property
    def solides(self):
        return filter(lambda x: x.solide, self.acteurs)

    def affiche_pv(self, acteur):
        font = pygame.font.Font('freesansbold.ttf', 16)
        text = font.render(str(round(acteur.pv)), True, (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (acteur.x_rel + 10, acteur.y_rel - 10)
        self.win.blit(text, textRect)

    def draw_game(self):
        self.win.fill(self.color)
        for acteur in self.acteurs:
            acteur.affiche()

        pygame.display.update()

    def update(self):
        for acteur in self.acteurs:
            acteur.hidden = False

        for acteur in self.non_vivants:
            acteur.comportement()

        for acteur in self.vivants:
            acteur.comportement()

        self.draw_game()
