from django.urls import path 

from . import views

app_name="cardgame"

urlpatterns = [
    path('attack', views.attack_game, name="attack"),
    path('defense', views.defense_game, name="defense"),
]