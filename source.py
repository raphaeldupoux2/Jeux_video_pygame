from random import randint

from acteur import Acteur


class Source(Acteur):
    def __init__(self, game_instance):
        super().__init__(game_instance, randint(300, 1000), randint(200, 450), 0, 100, 100, (0, 180, 255), False, True)

    def heal(self, acteur):
        if self.touche(acteur):
            acteur.pv += 1

    def comportement(self):
        for player in self.game_instance.players:
            self.heal(player)
