from django.db import models

class Game(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Player(models.Model):
    username = models.CharField(max_length=50, unique=True)
    score = models.IntegerField(default=0)
    games_played = models.ManyToManyField(Game, related_name='players')

    def __str__(self):
        return self.username

class GameSession(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    players = models.ManyToManyField(Player, related_name='sessions')
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Session for {self.game.title} with {self.players.count()} players"