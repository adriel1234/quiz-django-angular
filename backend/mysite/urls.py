from django.urls import path
from apps.players import views as player_views
from apps.game import views as game_views

urlpatterns = [
    path('players/', player_views.PlayerList.as_view(), name='player-list'),
    path('players/<int:pk>/', player_views.PlayerDetail.as_view(), name='player-detail'),
    path('games/', game_views.GameList.as_view(), name='game-list'),
    path('games/<int:pk>/', game_views.GameDetail.as_view(), name='game-detail'),
]