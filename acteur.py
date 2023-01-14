from abc import ABC, abstractmethod


class Acteur(ABC):

    def __init__(self, game_instance, x, y, vel):
        self.x: float = x
        self.y: float = y
        self.vel: float = vel
        self.game_instance = game_instance
        self.game_instance.acteurs.append(self)
        self.pv = 1000

    def limit(self):
        if self.x < 0:
            self.x = 0
        if self.x + self.game_instance.player[0].sizeX > self.game_instance.width:
            self.x = self.game_instance.width - self.game_instance.player[0].sizeX
        if self.y < 0:
            self.y = 0
        if self.y + self.game_instance.player[0].sizeY > self.game_instance.hidth:
            self.y = self.game_instance.hidth - self.game_instance.player[0].sizeY

    def prend_degat(self, degat: float):
        self.pv -= degat

    @abstractmethod
    def comportement(self):
        pass

    @abstractmethod
    def affiche(self):
        pass
