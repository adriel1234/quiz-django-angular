from django.db import models

class Player(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    score = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

class Game(models.Model):
    player1 = models.ForeignKey(Player, related_name='player1_games', on_delete=models.CASCADE)
    player2 = models.ForeignKey(Player, related_name='player2_games', on_delete=models.CASCADE)
    winner = models.ForeignKey(Player, related_name='won_games', on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Game between {self.player1} and {self.player2}"