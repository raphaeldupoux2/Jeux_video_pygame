from random import randint

from acteur import Acteur


class Source(Acteur):
    def __init__(self, game_instance):
        super().__init__(game_instance, randint(300, 1000), randint(200, 450), 0, 100, 100, (0, 180, 255))

    def heal(self, acteur_affecte: list):
        for acteur in acteur_affecte:
            if self.touche(acteur):
                acteur.pv += 1

    def comportement(self):
        self.heal(self.game_instance.player)
