from acteur import Acteur

DARK_BROWN = (100, 65, 28)


class Bouse(Acteur):

    def __init__(self, game_instance, x=0, y=0, sizeX=50, sizeY=50):
        super().__init__(game_instance, x, y, 0, sizeX, sizeY, DARK_BROWN, True, False)

    def comportement(self):
        pass
