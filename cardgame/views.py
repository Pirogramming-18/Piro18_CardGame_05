from django.shortcuts import render, redirect, get_object_or_404
from django.http.request import HttpRequest

from .models import Attack
from .models import Defense
from .models import User
from .models import *
import random

from .models import Attack
from .models import Defense
from .models import User

# Create your views here.
def game_list(request, *args, **kwargs):
    cardgames = CardGame.objects.all()

    return render(request, "cardgame/game_list.html", {"cardgames":cardgames})

def user_ranking(request:HttpRequest, *args, **kwargs):
    users = User.objects.all().order_by("-score")

    return render(request, "cardgame/game_ranking.html", {"users":users})

def list_game(request):
    if request.user.is_authenticated:
        # 현재 로그인한 유저가 속하는 게임들
        end_attack_games = CardGame.objects.filter(
            attack__attack_user__username=request.user.username, status='끝')
        proceed_attack_games = CardGame.objects.filter(
            attack__attack_user__username=request.user.username, status='진행중')
        end_defense_games = CardGame.objects.filter(
            defense__defense_user__username=request.user.username, status='끝')
        proceed_defense_games = CardGame.objects.filter(
            defense__defense_user__username=request.user.username, status='진행중')

        end_games = end_attack_games.union(end_defense_games)
        proceed_games = proceed_attack_games.union(proceed_defense_games)

        ctx = {
            'end_games': end_games,
            'proceed_games': proceed_games,
            'current_user': request.user,
            'count' : 1,
        }
        return render(request, 'cardgame/list_game.html', context=ctx)

def delete_game(request, pk):
    game = CardGame.objects.get(id=pk)
    game.delete()
    return redirect('cardgame:list_game')


def game_win(attack, defense, pk, game):
    
    if game.mode == '큰 수':
        if attack.num.card_num >= defense.num.card_num:
            win_user = attack.attack_user 
            attack.attack_user.point += attack.num.card_num
            defense.defense_user.point -= defense.num.card_num
        
        else:
            win_user = defense.defense_user
            attack.attack_user.point -= attack.num.card_num
            defense.defense_user.point += defense.num.card_num

    else:
        if attack.num.card_num <= defense.num.card_num:
            win_user = attack.attack_user
            attack.attack_user.point += attack.num.card_num
            defense.defense_user.point -= defense.num.card_num

        else:
            win_user = defense.defense_user
            attack.attack_user.point -= attack.num.card_num
            defense.defense_user.point += defense.num.card_num

    game.attack.attack_user.save()
    game.defense.defense_user.save()

    return [win_user, attack.attack_user.point, defense.defense_user.point]

def detail_game(request,pk):
    game=get_object_or_404(CardGame,id=pk)
    
    if game.status=="끝":
        ctx={'game':game,
        'current_user':request.user
        }
        return render(request,template_name='cardgame/detail_end.html',context=ctx)
    if game.status=="진행중":
        ctx={'game':game,
        'current_user':request.user
        }
        return render(request,template_name='cardgame/detail_progress.html',context=ctx)

def attack_game(request):

    if request.user.is_authenticated:
        Attack.objects.create( attack_user = request.user.username )
            
    card_num = request.GET.get('card_num')
    attacked = request.GET.get('attacked')
    
    users = User.objects.all()
    attack = Attack.objects.all()
    
    if request.method == 'POST':
        
        card_num = request.POST["card_num"]
        attacked = request.POST["attacked"]

        
        Attack.objects.get( attack_user = request.user.username ).num = card_num
        Defense.objects.create( defense_user = attacked )
        return redirect("/")    
    
    
    context = {
        "users":users
    }
    
    return render(request, template_name="cardgame/attack.html", context=context)


def defense_game(request):
    
        
    card_num = request.GET.get('card_num')
        
    users = User.objects.all()
    attack = Attack.objects.all()
    defense = Defense.objects.all()
    
    if request.method == 'POST':
        
        card_num = request.POST["card_num"]

        
        Defense.objects.get(defense_user = request.user.username).num = card_num
        return redirect("/")        
    
    
    context = {
        "attack": attack
    }
    
    return render(request, template_name="cardgame/defense.html", context=context)
