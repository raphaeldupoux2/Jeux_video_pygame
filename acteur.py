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
        if self.x + self.game_instance.size_playerX > self.game_instance.width:
            self.x = self.game_instance.width - self.game_instance.size_playerX
        if self.y < 0:
            self.y = 0
        if self.y + self.game_instance.size_playerY > self.game_instance.hidth:
            self.y = self.game_instance.hidth - self.game_instance.size_playerY

    def prend_degat(self, degat: int):
        self.pv -= degat

    @abstractmethod
    def comportement(self):
        pass

    def affiche(self):
        pass