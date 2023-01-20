from turtle import title
from random import choice
from django.db import models


class User(models.Model):
	name = models.CharField(max_length=64)
	score = models.IntegerField()


class Attack(models.Model):
	attack_user = models.CharField(max_length=64)
	num = models.IntegerField(null=True, blank=True)


class Defense(models.Model):
	defense_user = models.CharField(max_length=64)
	num = models.IntegerField(null=True, blank=True)


MODE_CHOICES = {('큰 수', '큰 수'), ('작은 수', '작은 수')}
STATUS_CHOICES = {('진행 중', '진행 중'), ('끝', '끝')}
class CardGame(models.Model):
	mode = models.CharField(max_length=30, choices = MODE_CHOICES) # 큰 수가 이기는 게임 혹은 작은 수가 이기는 게임
	status = models.CharField(max_length=30, choices = STATUS_CHOICES) # 게임 상태값
	attack = models.OneToOneField(Attack, on_delete=models.CASCADE, related_name="cardgame_attack")
	defense = models.OneToOneField(Defense, on_delete=models.CASCADE, related_name="cardgame_defense")
	win_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="cardgame_user")