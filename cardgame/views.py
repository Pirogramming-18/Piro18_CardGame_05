from django.shortcuts import render, redirect
from cardgame.models import Card, User, CardGame
from django.http.request import HttpRequest

# Create your views here.

def game_list(request, *args, **kwargs):
    cardgames = CardGame.objects.all()

    return render(request, "game_list.html", {"cardgames":cardgames})
    

def user_ranking(request:HttpRequest, *args, **kwargs):
    users = User.objects.all().order_by("-score")


    return render(request, "game_ranking.html", {"Users":users})