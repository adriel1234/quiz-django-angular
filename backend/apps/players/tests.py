from django.test import TestCase
from .models import Player

class PlayerModelTest(TestCase):
    def setUp(self):
        Player.objects.create(name="Player 1", score=0)
        Player.objects.create(name="Player 2", score=0)

    def test_player_creation(self):
        player1 = Player.objects.get(name="Player 1")
        player2 = Player.objects.get(name="Player 2")
        self.assertEqual(player1.score, 0)
        self.assertEqual(player2.score, 0)

    def test_player_string_representation(self):
        player = Player(name="Player 1")
        self.assertEqual(str(player), player.name)