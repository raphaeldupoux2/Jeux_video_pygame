from buisson import Buisson
from mechant import Mechant
from monde.monde import Monde
from rocher import Rocher
from source import Source

BROWN = (120, 80, 35)


class ParadisDesBouseux(Monde):

    def __init__(self, game_instance):
        super().__init__(game_instance)

    def spawn_terrain(self):
        super().spawn_terrain()
        self.random_spawn(Buisson, 10)
        self.random_spawn(Source, 5)
        self.random_spawn(Rocher, 50)

    def spawn_mobs(self):
        mechant1 = Mechant(self.game_instance, self.game_instance.players[0])
        mechant2 = Mechant(self.game_instance, self.game_instance.players[0])

    def rentre(self):
        super().rentre()
        self.set_color(BROWN)
