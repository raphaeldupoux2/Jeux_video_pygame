from random import randint
from acteur import Acteur


class Source(Acteur):
    def __init__(self, game_instance):
        super().__init__(game_instance, randint(300, 1000), randint(200, 450), 0)
        self.sizeX = game_instance.size_sourceX
        self.sizeY = game_instance.size_sourceY

    def heal(self, acteur_affecte: list):
        for acteur in acteur_affecte:
            if acteur.x < self.x + self.game_instance.size_sourceX and acteur.x > self.x - self.game_instance.size_playerX and acteur.y < self.y + self.game_instance.size_sourceY and acteur.y > self.y - self.game_instance.size_playerY:
                acteur.pv += 1
                # print(acteur.pv)

    def comportement(self):
        self.heal(self.game_instance.player)

