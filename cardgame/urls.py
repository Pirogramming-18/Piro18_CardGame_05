from django.urls import path
from . import views

app_name = "cardgame"

urlpatterns= [
    path("game/list", views.game_list, name="list"),
    path("game/ranking", views.user_ranking, name="ranking"),
]