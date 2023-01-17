from acteur import Acteur


class Rocher(Acteur):
    def __init__(self, game_instance, x, y):
        super().__init__(game_instance, x, y, 0, 20, 20, (150, 150, 150), True)

    def comportement(self):
        pass
