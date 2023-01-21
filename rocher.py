from acteur import Acteur


class Rocher(Acteur):
    def __init__(self, game_instance, x=0, y=0, sizeX=20, sizeY=20):
        super().__init__(game_instance, x, y, 0, sizeX, sizeY, (150, 150, 150), True, False)

    def comportement(self):
        pass
