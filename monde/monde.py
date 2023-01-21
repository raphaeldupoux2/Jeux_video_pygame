from abc import ABC, abstractmethod
from random import random, randint

from rocher import Rocher


class Monde(ABC):

    def __init__(self, game_instance):
        self.game_instance = game_instance
        self.terrains = []

    @abstractmethod
    def spawn_terrain(self):
        self.sort()

    @abstractmethod
    def spawn_mobs(self):
        pass

    def set_color(self, color):
        self.game_instance.color = color

    def random_spawn(self, object, n):
        for i in range(n):
            terrain = object(self.game_instance, x=randint(-1000, 1000), y=randint(-1000, 1000))
            self.terrains.append(terrain)

    def sort(self):
        for terrain in self.terrains:
            self.game_instance.acteurs.remove(terrain)

    def rentre(self):
        self.game_instance.acteurs += self.terrains

