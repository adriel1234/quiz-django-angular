from django.test import TestCase
from .models import Game

class GameModelTest(TestCase):
    def setUp(self):
        Game.objects.create(name="Test Game", description="A game for testing.")

    def test_game_creation(self):
        game = Game.objects.get(name="Test Game")
        self.assertEqual(game.description, "A game for testing.")

    def test_game_str(self):
        game = Game.objects.get(name="Test Game")
        self.assertEqual(str(game), "Test Game")