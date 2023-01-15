from random import randint

from acteur import Acteur


class Buisson(Acteur):
    def __init__(self, game_instance):
        super().__init__(game_instance, randint(300, 1000), randint(200, 450), 0, 80, 40, (0, 255, 0))

    def hide(self, acteur_affecte: list):
        for acteur in acteur_affecte:
            acteur.hidden = self.touche(acteur)

    def comportement(self):
        self.hide(self.game_instance.etre_vivant)
