from random import randint

from acteur import Acteur


class Buisson(Acteur):
    def __init__(self, game_instance):
        super().__init__(game_instance, randint(300, 1000), randint(200, 450), 0, 80, 40, (0, 255, 0), False, False)

    def hide(self, vivant):
        if self.touche(vivant):
            vivant.hidden = True

    def comportement(self):
        for vivant in self.game_instance.vivants:
            self.hide(vivant)
