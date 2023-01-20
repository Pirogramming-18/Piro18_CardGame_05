from django.shortcuts import render, redirect

from .models import Attack
from .models import Defense
from .models import User

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
    
    return render(request, template_name="AD/attack.html", context=context)


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
    
    return render(request, template_name="AD/defense.html", context=context)