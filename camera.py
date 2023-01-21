from acteur import Acteur


class Camera(Acteur):

    def __init__(self, game_instance, x, y):
        super().__init__(game_instance, x, y, 0, 0, 0, (0, 0, 0), 0)
        self.cible = None

    def comportement(self):
        if self.cible is not None:
            self.x = self.cible.x - self.game_instance.width / 2 + self.cible.sizeX / 2
            self.y = self.cible.y - self.game_instance.hidth / 2 + self.cible.sizeY / 2
