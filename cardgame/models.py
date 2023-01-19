from random import choice
from django.db import models

class Card(models.Model):
	card_num = models.IntegerField()

	def __str__(self):
		return str(self.card_num)

class User(models.Model):
	name = models.CharField(max_length=64)
	score = models.IntegerField()
	card = models.ForeignKey(Card, on_delete=models.CASCADE, related_name="user_card")

class Attack(models.Model):
	attack_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="attack_user_user")
	num = models.ForeignKey(Card, on_delete=models.CASCADE, related_name="attack_card")
	attacked_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="attacked_user_user")

class Defense(models.Model):
	defense_user = models.ForeignKey(Attack, on_delete=models.CASCADE, related_name="defense_attack")
	num = models.ForeignKey(Card, on_delete=models.CASCADE, null=True, blank=True, related_name="defense_num")

MODE_CHOICES = {('큰 수', '큰 수'), ('작은 수', '작은 수')}
STATUS_CHOICES = {('진행 중', '진행 중'), ('끝', '끝')}
class CardGame(models.Model):
	mode = models.CharField(max_length=30, choices = MODE_CHOICES) # 큰 수가 이기는 게임 혹은 작은 수가 이기는 게임
	status = models.CharField(max_length=30, choices = STATUS_CHOICES) # 게임 상태값
	attack = models.OneToOneField(Attack, on_delete=models.CASCADE, related_name="cardgame_attack")
	defense = models.OneToOneField(Defense, on_delete=models.CASCADE, related_name="cardgame_defense")
	win_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="cardgame_user")