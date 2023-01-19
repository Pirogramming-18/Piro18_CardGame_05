from django.contrib import admin
from .models import CardGame, User, Card, Attack, Defense
# Register your models here.

admin.site.register(CardGame)
admin.site.register(User)
admin.site.register(Card)
admin.site.register(Attack)
admin.site.register(Defense)