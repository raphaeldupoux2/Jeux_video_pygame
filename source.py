from random import randint

from acteur import Acteur


class Source(Acteur):
    def __init__(self, game_instance, x=0, y=0):
        super().__init__(game_instance, x, y, 0, 100, 100, (0, 180, 255), False, True)

    def heal(self, acteur):
        if self.touche(acteur):
            acteur.pv += 1

    def comportement(self):
        for player in self.game_instance.players:
            self.heal(player)
