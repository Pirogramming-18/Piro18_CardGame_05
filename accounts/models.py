from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    
	first_name=None
	last_name=None #필드 삭제
    
	email=models.EmailField(null=True)
	name = models.CharField(max_length=64)
	#score = models.IntegerField()
	#card = models.ForeignKey(Card, on_delete=models.CASCADE, related_name="User_game")

    #USERNAME_FIELD = 'email'
