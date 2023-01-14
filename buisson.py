from random import randint
from acteur import Acteur


class Buisson(Acteur):
    def __init__(self, game_instance):
        super().__init__(game_instance, randint(300, 1000), randint(200, 450), 0)
        self.sizeX = game_instance.size_buissonX
        self.sizeY = game_instance.size_buissonY

    def hide(self, acteur_affecte: list):
        for acteur in acteur_affecte:
            if acteur.x < self.x + self.game_instance.size_buissonX and acteur.x > self.x - self.game_instance.size_playerX and acteur.y < self.y + self.game_instance.size_buissonY and acteur.y > self.y - self.game_instance.size_playerY:
                acteur.hidden = True
            else:
                acteur.hidden = False

    def comportement(self):
        self.hide(self.game_instance.etre_vivant)

    def affiche(self):
        pass
