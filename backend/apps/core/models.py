from django.db import models

class Player(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

class Game(models.Model):
    title = models.CharField(max_length=255)
    players = models.ManyToManyField(Player, related_name='games')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Score(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    score = models.IntegerField()

    def __str__(self):
        return f"{self.player.username} - {self.score} in {self.game.title}"