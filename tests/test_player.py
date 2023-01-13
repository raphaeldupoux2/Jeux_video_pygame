from unittest import TestCase

from game_instance import Game_instance
from player import Player


class TestPlayer(TestCase):

    def test_prends_degat(self):
        game_instance = Game_instance()
        player = Player(game_instance)
        self.assertEqual(player.pv, 1000)
        player.prend_degat(20)
        self.assertEqual(player.pv, 980)
        self.assertEqual(game_instance.run, True)
        player.prend_degat(1000)
        self.assertEqual(game_instance.run, False)





